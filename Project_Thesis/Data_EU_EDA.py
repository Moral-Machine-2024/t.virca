# %%
### EDA/pre-processing on EU respondents data ###
# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from itertools import combinations

# %%
# Read SharedResponses EU users
data_EU = pd.read_csv('SharedResponsesEU.csv')

# %%
# Head
print(data_EU.head())

# Info
print(data_EU.info())
# rows 24.773.480 x 41 columns
# dtypes - object, float, int

# Summary statistics
print(data_EU.describe())

# Save initial length dataset
initial_length = len(data_EU)

# %%
# Are there missing values?
print(data_EU.isnull().sum())
print()
# ScenarioType, NumberOfCharacters, DiffNumberOFCharacters, all 20 character encoding (30)
# UserID (4017)
# DefaultChoice, NonDefaultChoice, DefaultChoiceIsOmission (2.644.444)
# Template, DescriptionShown, LeftHand (4.144.841)

# Are there any duplicated rows?
duplicates = data_EU.duplicated()
print(duplicates.any())
# False - No duplicate rows

# %%
### Delete columns
# Delete encoding of character features - not used in the analysis
data_EU = data_EU.drop(data_EU.columns[21:40+1], axis=1)
print(data_EU.info())

# %%
# Delete unnecessary columns also containing missing values
drop_columns = ['Template', 'DescriptionShown', 'LeftHand', 'ScenarioType', 'ExtendedSessionID', 'PedPed', 'ScenarioOrder']
data_EU = data_EU.drop(columns=drop_columns, axis=1)
print(data_EU.isnull().sum())

# %%
# Check DefaultChoice, NonDefaultChoice, DefaultChoiceIsOmission (2.644.414 NaN)
default_unique = data_EU['DefaultChoice'].unique()
print('Unique values of DefaultChoice: ')
print(default_unique)
print()
# [nan 'More' 'Young' 'Fit' 'Male' 'Hoomans' 'High']

nondefault_unique = data_EU['NonDefaultChoice'].unique()
print('Unique values of NonDefaultChoice: ')
print(nondefault_unique)
print()
# [nan 'Less' 'Old' 'Fat' 'Female' 'Pets' 'Low']

omission_unique = data_EU['DefaultChoiceIsOmission'].unique()
print('Unique values of DefaultChoiceIsOmission: ')
print(omission_unique)
# [nan  1.  0.]

# --> how to deal with these missing values? Will I need these variable?
# DefaultChoiceIsOmission = 1 -> characters that hold the default choice will be killed if the AV does nothing
# DefaultChoiceIsOmission = 0 -> characters that hold the non-default choice will be killed if the AV does nothing
# Distinction between default and non-default is not relevant for my purposes -> delete columns

# %%
# Delete DefaultChoice, NonDefaultChoice, DefaultChoiceIsOmission
drop_columns_2 = ['DefaultChoice', 'NonDefaultChoice', 'DefaultChoiceIsOmission']
data_EU = data_EU.drop(columns=drop_columns_2, axis=1)
print(data_EU.isnull().sum())

# %%
### Delete rows
# Drop 30 NaN rows NumberOfCharacters, DiffNumberOFCharacters + 4017 NaN UserID
data_EU = data_EU.dropna(subset=['NumberOfCharacters', 'UserID'])
print(data_EU.isnull().sum())
print('Current length: ', len(data_EU))

# %%
# Delete responseID with no pair (incomplete scenario)
# Mark rows with duplicates
data_EU['is_duplicate'] = data_EU.duplicated(subset='ResponseID', keep=False)
print(data_EU.info())

# Filter based on 'is_duplicate' column
data_EU = data_EU[data_EU['is_duplicate']]
print(data_EU.info())

# Drop 'is_duplicate' column
data_EU.drop(columns='is_duplicate', inplace=True)

# Reset index after filtering
data_EU.reset_index(drop=True, inplace=True)

# %%
# Save current length dataset
length_2 = len(data_EU)
print('Length without unpaired rows: ', length_2)

# Check that unique values are half of length
double_unique = data_EU['ResponseID'].nunique() * 2
print('Should be equal to length above: ', double_unique)

# %%
# Proportion of sampled rows deleted
print('Initial length: ', initial_length)
print('Current length: ', length_2)
change_in_length = initial_length - length_2
proportion_deleted = (change_in_length / initial_length) * 100
print("Proportion deleted: ", proportion_deleted)
# 3.462 -> 3.46% of rows have been deleted from the sample

# %%
# Examine other object dtype columns
response_ID_nunique = data_EU['ResponseID'].nunique()
print(response_ID_nunique)
# 12.813.663 (number of scenarios, roughly half of the observations, as expected)

attributelevel_unique = data_EU['AttributeLevel'].unique()
print(attributelevel_unique)
# ['Rand' 'More' 'Old' 'Fat' 'Less' 'Fit' 'Female' 'Young' 'Pets' 'Hoomans' 'Male' 'Low' 'High']

scenario_strict_unique = data_EU['ScenarioTypeStrict'].unique()
print(scenario_strict_unique)
# ['Random' 'Utilitarian' 'Age' 'Fitness' 'Gender' 'Species' 'Social Status']

country_nunique = data_EU['UserCountry3'].nunique()
print(country_nunique)
# 27 as expected

# %%
# Export cleaned dataframe to csv (intermediate)
data_EU.to_csv('EU_df2.csv.csv')

# %%
# Check how many individual respondents (based on user ID)
respondents = data_EU['UserID'].nunique()
print("Number of individual respondents: ", respondents)
# 793.035

# %%
# Check country representation
countries_counts = data_EU['UserCountry3'].value_counts()
print(countries_counts)
# Max -> DEU 4.440.290
# Min -> MLT 19.254

# %%
# Country representation bar plot - Visualize relative count distribution
plt.figure(figsize=(12, 6))
sns.barplot(x = countries_counts.index, y = countries_counts.values / len(data_EU), order=countries_counts.index)
plt.xlabel('Countries')
plt.ylabel('Proportion of observations')
plt.title('Distribution of UserCountry3 Values')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# %%
# Check country representation per respondent (unique UserID)
# Count unique users per country
user_counts = data_EU.groupby('UserCountry3')['UserID'].nunique().reset_index()

# Sort
user_counts = user_counts.sort_values(by='UserID', ascending=False)

# Plot country representation per unique UserID
plt.figure(figsize=(12, 6))
sns.barplot(x='UserCountry3', y='UserID', data=user_counts, order=user_counts['UserCountry3'])
plt.title('Distribution of Unique Users per Country')
plt.xlabel('Countries')
plt.ylabel('Number of Unique Users')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

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
