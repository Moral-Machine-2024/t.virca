
############### Visualize distributions ###############

#%%
# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %%
# Load FINAL_DF

# For computational efficiency when loading the data:
# Define a dictionary specifying the data types for each column
dtypes = {
    'Intervene': 'int16',
    'Male': 'int16',
    'Female': 'int16',
    'Young': 'int16',
    'Old': 'int16',
    'Infancy': 'int16',
    'Pregnancy': 'int16',
    'Fat': 'int16',
    'Fit': 'int16',
    'Working': 'int16',
    'Medical': 'int16',
    'Homelessness': 'int16',
    'Criminality': 'int16',
    'Human': 'int16',
    'Non-human': 'int16',
    'Passenger': 'int16',
    'Law Abiding': 'int16',
    'Law Violating': 'int16',
    'ResponseID': 'category',
    'Intervention': 'int16',
    'PedPed': 'int16',
    'Barrier': 'int16',
    'AttributeLevel': 'category',
    'ScenarioTypeStrict': 'category',
    'NumberOfCharacters': 'int16',
    'DiffNumberOFCharacters': 'int16',
    'Saved': 'int16',
    'UserCountry3': 'category',
    'Man': 'int16',
    'Woman': 'int16',
    'Pregnant': 'int16',
    'Stroller': 'int16',
    'OldMan': 'int16',
    'OldWoman': 'int16',
    'Boy': 'int16',
    'Girl': 'int16',
    'Homeless': 'int16',
    'LargeWoman': 'int16',
    'LargeMan': 'int16',
    'Criminal': 'int16',
    'MaleExecutive': 'int16',
    'FemaleExecutive': 'int16',
    'FemaleAthlete': 'int16',
    'MaleAthlete': 'int16',
    'FemaleDoctor': 'int16',
    'MaleDoctor': 'int16',
    'Dog': 'int16',
    'Cat': 'int16',
    'Cultures': 'category',
    'CrossingSignal_0': 'int16',
    'CrossingSignal_1': 'int16',
    'CrossingSignal_2': 'int16'
}

# Load the df with the specified data types
df = pd.read_csv('FINAL_DF.csv', dtype=dtypes)

# %%
# View info
print(df.info())

# %%
# Plot the distribution of 'Saved'
plt.figure(figsize=(8, 6))
sns.countplot(x='Saved', data=df, palette='viridis')
plt.title('Distribution of Saved')
plt.xlabel('Saved')
plt.ylabel('Count')
plt.show()

# There is no class imbalance
# Since complete scenarios were considered, half of the rows were saved and half where spared

# %%
# Check how many individual respondents (based on user ID)
respondents = df['UserID'].nunique()
print("Number of individual respondents: ", respondents)
# 2.017.369 individual respondents

# Since there are roughly 16 million scenarios, on average, each respondent answered 8 scenarios
# or, definitely, many users answered multiple scenarios

# %%
# Check country representation (106 countries, a bar plot would have too many bars)
countries_counts = df['UserCountry3'].value_counts()
print(countries_counts)
# Max 1 -> USA 8.615.374
# Max 2 -> DEU 2.220.146
# Max 3 -> BRA 1.930.618
# Min -> NCL 2.692

# %%
# Check culture representation per respondent (unique UserID)
# Count unique users per culture
user_counts = df.groupby('Cultures')['UserID'].nunique().reset_index()

# Sort
user_counts = user_counts.sort_values(by='UserID', ascending=False)

# Plot culture representation per unique UserID
plt.figure(figsize=(12, 6))
sns.barplot(x='Cultures', y='UserID', data=user_counts, order=user_counts['Cultures'])
plt.title('Distribution of Unique Users per Cultures')
plt.xlabel('Cultures')
plt.ylabel('Number of Unique Users')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
