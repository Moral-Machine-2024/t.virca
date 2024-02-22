#%%
# EDA on EU respondents data
# Import libraries
import pandas as pd

# Read SharedResponses EU users
data_EU = pd.read_csv('SharedResponsesEU.csv')

#%%
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

#%%
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
# Delete unnecessary columns containing missing values
drop_columns = ['Template', 'DescriptionShown', 'LeftHand']
data_EU = data_EU.drop(columns=drop_columns, axis=1)
print(data_EU.isnull().sum())

# %%
# Drop 30 NaN rows ScenarioType + all characters encoding
data_EU = data_EU.dropna(subset=['ScenarioType', 'UserID'])
print(data_EU.isnull().sum())
print(len(data_EU))

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

# Save current length dataset
length_2 = len(data_EU)

#%%
# Proportion of rows deleted
change_in_length = initial_length - length_2
proportion_deleted = (change_in_length / initial_length) * 100
print("Proportion deleted: ", proportion_deleted)
# 0.01633 -> 1.63% of the total dataset

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
# --> 'ResponseID' and 'ExtendedSessionID' momentarily kept object (?)

# %%
# Check how many individual respondents (based on user ID)
respondents = data_EU['UserID'].nunique()
print("Number of individual respondents: ", respondents)
# 794.636

# %%

