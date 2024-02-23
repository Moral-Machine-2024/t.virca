# %%
### EDA/pre-processing on EU respondents data ###
# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
# Delete unnecessary columns containing missing values
drop_columns = ['Template', 'DescriptionShown', 'LeftHand']
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
# Drop 30 NaN rows ScenarioType, NumberOfCharacters, DiffNumberOFCharacters + 4017 NaN UserID
data_EU = data_EU.dropna(subset=['ScenarioType', 'UserID'])
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
print('Should be equal to legth above: ', double_unique)

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

session_ID_nunique = data_EU['ExtendedSessionID'].nunique()
print(session_ID_nunique)
# 1.252.961 (number of sessions)

attributelevel_unique = data_EU['AttributeLevel'].unique()
print(attributelevel_unique)
# ['Rand' 'More' 'Old' 'Fat' 'Less' 'Fit' 'Female' 'Young' 'Pets' 'Hoomans' 'Male' 'Low' 'High']

scenario_strict_unique = data_EU['ScenarioTypeStrict'].unique()
print(scenario_strict_unique)
# ['Random' 'Utilitarian' 'Age' 'Fitness' 'Gender' 'Species' 'Social Status']

scenario_type_unique = data_EU['ScenarioType'].unique()
print(scenario_type_unique)
# ['Random' 'Utilitarian' 'Age' 'Fitness' 'Gender' 'Species' 'Social Status']

country_nunique = data_EU['UserCountry3'].nunique()
print(country_nunique)
# 27 as expected

# %%
# Dtype object to categorical
categorical_col = ['AttributeLevel', 'ScenarioTypeStrict', 'ScenarioType', 'DefaultChoice', 'NonDefaultChoice', 'UserCountry3']
data_EU[categorical_col] = data_EU[categorical_col].astype('category')
print(data_EU.info())
# --> 'ResponseID' and 'ExtendedSessionID' momentarily kept object

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

# Order the dataframe by user counts in descending order
user_counts = user_counts.sort_values(by='UserID', ascending=False)

# Plotting the bar chart using Seaborn
plt.figure(figsize=(12, 6))
sns.barplot(x='UserCountry3', y='UserID', data=user_counts, order=user_counts['UserCountry3'])
plt.title('Distribution of Unique Users per Country')
plt.xlabel('Countries')
plt.ylabel('Number of Unique Users')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


