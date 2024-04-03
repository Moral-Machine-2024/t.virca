# %%
# Import libraries
import pandas as pd
import numpy as np
from itertools import combinations

# %%
# Import cleaned EU_data2
df = pd.read_csv('EU_df2.csv')

# %%
# Check - The same ResponseID pairs share the same ScenarioTypeStrict
# Print 5 random unique values of ResponseID
array_RID = df['ResponseID'].unique()
extract_5RID = np.random.choice(array_RID, size=5, replace=False)
print(extract_5RID)

# Check ScenarioType and ScenarioTypeStrict of 5 random ResponseID + duplicate
rows_5RID = df[df['ResponseID'].isin(extract_5RID)]
print(rows_5RID[['ResponseID', 'ScenarioTypeStrict']])
# --> Correct

# %%
## Head and Info
print(df.head())
print()
print(df.info())

# %%
# Dtype object to categorical
categorical_col = ['AttributeLevel', 'ScenarioTypeStrict', 'UserCountry3']
df[categorical_col] = df[categorical_col].astype('category')
print(df.info())
# --> 'ResponseID' momentarily kept object

# %%
# Function for pairwise comparison of rows + extract preferences into new df
def pairwise_comparison(df):
    pairwise_data = []

    # Group df by ResponseID
    grouped_df = df.groupby('ResponseID')

    # Loop through each unique ResponseID
    for response, pair in grouped_df:
        # Generate all possible pairs of indices
        for idx1, idx2 in combinations(pair.index, 2):
            # Extract rows of the current pair of indices
            row1, row2 = df.loc[idx1], df.loc[idx2]

            # Determine the winning outcome based on Saved
            winner = 'Outcome1' if row1['Saved'] == 1 else 'Outcome2'

            # Compute preferences
            intervention_pref = np.nan
            ped_pref = np.nan
            law_pref = np.nan
            more_pref = np.nan

            # Intervention preference
            if row1['Intervention'] != row2['Intervention']:
                if row1['Intervention'] == 1 and row1['Saved'] == 0:
                    intervention_pref = 0
                elif row1['Intervention'] == 1 and row1['Saved'] == 1:
                    intervention_pref = 1
                elif row1['Intervention'] == 0 and row1['Saved'] == 1:
                    intervention_pref = 0
                elif row1['Intervention'] == 0 and row1['Saved'] == 0:
                    intervention_pref = 1

            # Barrier preference (pedestrian vs passenger)
            if row1['Barrier'] != row2['Barrier']:
                if row1['Barrier'] == 1 and row1['Saved'] == 0:
                    ped_pref = 1
                elif row1['Barrier'] == 1 and row1['Saved'] == 1:
                    ped_pref = 0
                elif row1['Barrier'] == 0 and row1['Saved'] == 1:
                    ped_pref = 1
                elif row1['Barrier'] == 0 and row1['Saved'] == 0:
                    ped_pref = 0

            # Law Preference
            if row1['CrossingSignal'] != 0 or row2['CrossingSignal'] != 0:
                if row1['CrossingSignal'] == 1 and row1['Saved'] == 1:
                    law_pref = 1
                elif row1['CrossingSignal'] == 1 and row1['Saved'] == 0:
                    law_pref = 0
                elif row1['CrossingSignal'] == 2 and row1['Saved'] == 1:
                    law_pref = 0
                elif row1['CrossingSignal'] == 2 and row1['Saved'] == 0:
                    law_pref = 1
                elif row2['CrossingSignal'] == 1 and row2['Saved'] == 1:
                    law_pref = 1
                elif row2['CrossingSignal'] == 1 and row2['Saved'] == 0:
                    law_pref = 0
                elif row2['CrossingSignal'] == 2 and row2['Saved'] == 1:
                    law_pref = 0
                elif row2['CrossingSignal'] == 2 and row2['Saved'] == 0:
                    law_pref = 1

            # Utilitarian Preference
            if row1['NumberOfCharacters'] != row2['NumberOfCharacters']:
                if row1['NumberOfCharacters'] > row2['NumberOfCharacters'] and row1['Saved'] == 0:
                    more_pref = 0
                elif row1['NumberOfCharacters'] < row2['NumberOfCharacters'] and row1['Saved'] == 1:
                    more_pref = 1

            # Append the current pair of indices, winner, and preferences to the result list
            pairwise_data.append([idx1, idx2, winner, intervention_pref, ped_pref, law_pref, more_pref])

    # Create new df with pairwise comparison data
    columns = ['Outcome1', 'Outcome2', 'Winner', 'Intervention_Preference', 'Ped_Preference', 'Law_Preference',
               'More_Preference']
    pairwise_df = pd.DataFrame(pairwise_data, columns=columns)

    return pairwise_df


pairwise_df = pairwise_comparison(df)

# %%
# Check result
print(pairwise_df.head())

# Print info
print(pairwise_df.info())

# %%
# Intervention Preference value counts
print('Intervention_Preference value counts and NaN: ')
print(pairwise_df['Intervention_Preference'].value_counts())
# 1    6.466.877
# 0    5.490.978
print(pairwise_df['Intervention_Preference'].isnull().sum())
# 0 NaN
print()

# Pedestrians vs passengers preference value count
print('Ped_Preference value counts and NaN: ')
print(pairwise_df['Ped_Preference'].value_counts())
# 1.0    3.462.163
# 0.0    3.130.423
print(pairwise_df['Ped_Preference'].isnull().sum())
# 5.365.269 NaN
print()

# Abide by the law preference value counts
print('Law_Preference value counts and NaN: ')
print(pairwise_df['Law_Preference'].value_counts())
# 1.0    4.259.745
# 0.0    2.331.795
print(pairwise_df['Law_Preference'].isnull().sum())
# 5.366.315 NaN
print()

# Utilitarian preference value counts
print('More_Preference value counts and NaN: ')
print(pairwise_df['More_Preference'].value_counts())
# 0.0    412.352
# 1.0    339.402
print(pairwise_df['More_Preference'].isnull().sum())
# 11.206.101 NaN

# %%
# Export pairwise_df
pairwise_df.to_csv('Pairwise_df.csv', index=False)

# %%