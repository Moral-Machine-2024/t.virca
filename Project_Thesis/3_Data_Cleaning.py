# %%
### Data cleaning Samples ###
# Import
import pandas as pd

# Read samples
# Read SharedResponses EU users
Africa_df = pd.read_csv('Africa_sample.csv')
Asia_df = pd.read_csv('Asia_sample.csv')
Europe_df = pd.read_csv('Europe_sample.csv')
NorthAmerica_df = pd.read_csv('NorthAmerica_sample.csv')
SouthAmerica_df = pd.read_csv('SouthAmerica_sample.csv')
Oceania_df = pd.read_csv('Oceania_sample.csv')

# %%
#--------------------------## AFRICA ##--------------------------#
# Info
print(Africa_df.info())
# RangeIndex: 323.066 entries

# %%
# Are there any duplicated rows?
print(Africa_df.duplicated().any())
# False

# %%
### Delete unnecessary columns ###
drop_columns = ['ExtendedSessionID', 'ScenarioOrder', 'ScenarioType', 'DefaultChoice', 'NonDefaultChoice',
                'DefaultChoiceIsOmission', 'Template', 'DescriptionShown', 'LeftHand']

Africa_df = Africa_df.drop(columns=drop_columns, axis=1)

# Check
print(Africa_df.isnull().sum())

# %%
# Change name 'categories' to 'Cultures' for consistency
Africa_df = Africa_df.rename(columns={'categories': 'Cultures'})

# Check
print(Africa_df.info())

# %%
### Delete rows with missing values ###
# Drop 23 NaN rows for UserID
Africa_df = Africa_df.dropna(subset=['UserID'])

# Check
print(Africa_df.isnull().sum())

# %%
### Delete incomplete scenarios - ResponseID with no pair ###
# Mark rows with duplicates
Africa_df['is_duplicate'] = Africa_df.duplicated(subset='ResponseID', keep=False)

# Check new 'is_duplicate' column
print(Africa_df.info())

# Filter based on 'is_duplicate' column
Africa_df = Africa_df[Africa_df['is_duplicate']]

# Drop 'is_duplicate' column
Africa_df.drop(columns='is_duplicate', inplace=True)

# Reset index after filtering
Africa_df.reset_index(drop=True, inplace=True)

# Check number of incomplete scenarios
print(Africa_df.info())
# From 323.043 entries to 311.892 entries

# %%
# Export cleaned Africa_df
Africa_df.to_csv('Africa_Clean.csv', index=False)

# %%
#--------------------------## ASIA ##--------------------------#
# Info
print(Asia_df.info())
# RangeIndex: 6.676.416

# %%
# Are there any duplicated rows?
print(Asia_df.duplicated().any())
# False

# %%
### Delete unnecessary columns ###
drop_columns = ['ExtendedSessionID', 'ScenarioOrder', 'ScenarioType', 'DefaultChoice', 'NonDefaultChoice',
                'DefaultChoiceIsOmission', 'Template', 'DescriptionShown', 'LeftHand']

Asia_df = Asia_df.drop(columns=drop_columns, axis=1)

# Check
print(Asia_df.isnull().sum())

# %%
# Change name 'categories' to 'Cultures' for consistency
Asia_df = Asia_df.rename(columns={'categories': 'Cultures'})

# Check
print(Asia_df.info())

# %%
### Delete rows with missing values ###
# Drop 170 NaN rows in UserID and 2 NaN rows in NumberOfCharacters
Asia_df = Asia_df.dropna(subset=['UserID', 'NumberOfCharacters'])

# Check
print(Asia_df.isnull().sum())

# %%
### Delete incomplete scenarios - ResponseID with no pair ###
# Mark rows with duplicates
Asia_df['is_duplicate'] = Asia_df.duplicated(subset='ResponseID', keep=False)

# Check new 'is_duplicate' column
print(Asia_df.info())

# Filter based on 'is_duplicate' column
Asia_df = Asia_df[Asia_df['is_duplicate']]

# Drop 'is_duplicate' column
Asia_df.drop(columns='is_duplicate', inplace=True)

# Reset index after filtering
Asia_df.reset_index(drop=True, inplace=True)

# Check number of incomplete scenarios
print(Asia_df.info())
# From 6.676.244 entries to 6.447.088 entries

# %%
# Export cleaned Asia_df
Asia_df.to_csv('Asia_Clean.csv', index=False)

# %%
#--------------------------## EUROPE ##--------------------------#

# Info
print(Europe_df.info())
# RangeIndex: 32.935.386

# %%
# Are there any duplicated rows?
print(Europe_df.duplicated().any())
# False

# %%
### Delete unnecessary columns ###
drop_columns = ['ExtendedSessionID', 'ScenarioOrder', 'ScenarioType', 'DefaultChoice', 'NonDefaultChoice',
                'DefaultChoiceIsOmission', 'Template', 'DescriptionShown', 'LeftHand']

Europe_df = Europe_df.drop(columns=drop_columns, axis=1)

# Check
print(Europe_df.isnull().sum())

# %%
# Change name 'categories' to 'Cultures' for consistency
Europe_df = Europe_df.rename(columns={'categories': 'Cultures'})

# Check
print(Europe_df.info())

# %%
### Delete rows with missing values ###
# Drop 4789 NaN rows in UserID and 44 NaN rows in NumberOfCharacters
Europe_df = Europe_df.dropna(subset=['UserID', 'NumberOfCharacters'])

# Check
print(Europe_df.isnull().sum())

# %%
### Delete incomplete scenarios - ResponseID with no pair ###
# Mark rows with duplicates
Europe_df['is_duplicate'] = Europe_df.duplicated(subset='ResponseID', keep=False)

# Check new 'is_duplicate' column
print(Europe_df.info())

# Filter based on 'is_duplicate' column
Europe_df = Europe_df[Europe_df['is_duplicate']]

# Drop 'is_duplicate' column
Europe_df.drop(columns='is_duplicate', inplace=True)

# Reset index after filtering
Europe_df.reset_index(drop=True, inplace=True)

# Check number of incomplete scenarios
print(Europe_df.info())
# From 32.930.553 entries to 31.794.814 entries

# %%
# Export cleaned Europe_df
Europe_df.to_csv('Europe_Clean.csv', index=False)

# %%
#--------------------------## NORTH AMERICA ##--------------------------#
# Info
print(NorthAmerica_df.info())
# RangeIndex: 21.475.167

# %%
# Are there any duplicated rows?
print(NorthAmerica_df.duplicated().any())
# False

# %%
### Delete unnecessary columns ###
drop_columns = ['ExtendedSessionID', 'ScenarioOrder', 'ScenarioType', 'DefaultChoice', 'NonDefaultChoice',
                'DefaultChoiceIsOmission', 'Template', 'DescriptionShown', 'LeftHand']

NorthAmerica_df = NorthAmerica_df.drop(columns=drop_columns, axis=1)

# Check
print(NorthAmerica_df.isnull().sum())

# %%
# Change name 'categories' to 'Cultures' for consistency
NorthAmerica_df = NorthAmerica_df.rename(columns={'categories': 'Cultures'})

# Check
print(NorthAmerica_df.info())

# %%
### Delete rows with missing values ###
# Drop 3451 NaN rows in UserID and 26 NaN rows in NumberOfCharacters
NorthAmerica_df = NorthAmerica_df.dropna(subset=['UserID', 'NumberOfCharacters'])

# Check
print(NorthAmerica_df.isnull().sum())

# %%
### Delete incomplete scenarios - ResponseID with no pair ###
# Mark rows with duplicates
NorthAmerica_df['is_duplicate'] = NorthAmerica_df.duplicated(subset='ResponseID', keep=False)

# Check new 'is_duplicate' column
print(NorthAmerica_df.info())

# Filter based on 'is_duplicate' column
NorthAmerica_df = NorthAmerica_df[NorthAmerica_df['is_duplicate']]

# Drop 'is_duplicate' column
NorthAmerica_df.drop(columns='is_duplicate', inplace=True)

# Reset index after filtering
NorthAmerica_df.reset_index(drop=True, inplace=True)

# Check number of incomplete scenarios
print(NorthAmerica_df.info())
# From 21.471.690 entries to 20.730.470 entries

# %%
# Export cleaned NorthAmerica_df
NorthAmerica_df.to_csv('NorthAmerica_Clean.csv', index=False)

# %%
#--------------------------## SOUTH AMERICA ##--------------------------#
# Info
print(SouthAmerica_df.info())
# RangeIndex: 5.329.471

# %%
# Are there any duplicated rows?
print(SouthAmerica_df.duplicated().any())
# False

# %%
### Delete unnecessary columns ###
drop_columns = ['ExtendedSessionID', 'ScenarioOrder', 'ScenarioType', 'DefaultChoice', 'NonDefaultChoice',
                'DefaultChoiceIsOmission', 'Template', 'DescriptionShown', 'LeftHand']

SouthAmerica_df = SouthAmerica_df.drop(columns=drop_columns, axis=1)

# Check
print(SouthAmerica_df.isnull().sum())

# %%
# Change name 'categories' to 'Cultures' for consistency
SouthAmerica_df = SouthAmerica_df.rename(columns={'categories': 'Cultures'})

# Check
print(SouthAmerica_df.info())

# %%
### Delete rows with missing values ###
# Drop 142 NaN rows in UserID
SouthAmerica_df = SouthAmerica_df.dropna(subset=['UserID'])

# Check
print(SouthAmerica_df.isnull().sum())

# %%
### Delete incomplete scenarios - ResponseID with no pair ###
# Mark rows with duplicates
SouthAmerica_df['is_duplicate'] = SouthAmerica_df.duplicated(subset='ResponseID', keep=False)

# Check new 'is_duplicate' column
print(SouthAmerica_df.info())

# Filter based on 'is_duplicate' column
SouthAmerica_df = SouthAmerica_df[SouthAmerica_df['is_duplicate']]

# Drop 'is_duplicate' column
SouthAmerica_df.drop(columns='is_duplicate', inplace=True)

# Reset index after filtering
SouthAmerica_df.reset_index(drop=True, inplace=True)

# Check number of incomplete scenarios
print(SouthAmerica_df.info())
# From 5.329.329 entries to 5.144.964 entries

# %%
# Export cleaned SouthAmerica_df
SouthAmerica_df.to_csv('SouthAmerica_Clean.csv', index=False)

# %%
#--------------------------## OCEANIA ##--------------------------#
# Info
print(Oceania_df.info())
# RangeIndex: 2.269.192

# %%
# Are there any duplicated rows?
print(Oceania_df.duplicated().any())
# False

# %%
### Delete unnecessary columns ###
drop_columns = ['ExtendedSessionID', 'ScenarioOrder', 'ScenarioType', 'DefaultChoice', 'NonDefaultChoice',
                'DefaultChoiceIsOmission', 'Template', 'DescriptionShown', 'LeftHand']

Oceania_df = Oceania_df.drop(columns=drop_columns, axis=1)

# Check
print(Oceania_df.isnull().sum())

# %%
# Change name 'categories' to 'Cultures' for consistency
Oceania_df = Oceania_df.rename(columns={'categories': 'Cultures'})

# Check
print(Oceania_df.info())

# %%
### Delete rows with missing values ###
# Drop 68 NaN rows in UserID
Oceania_df = Oceania_df.dropna(subset=['UserID'])

# Check
print(Oceania_df.isnull().sum())

# %%
### Delete incomplete scenarios - ResponseID with no pair ###
# Mark rows with duplicates
Oceania_df['is_duplicate'] = Oceania_df.duplicated(subset='ResponseID', keep=False)

# Check new 'is_duplicate' column
print(Oceania_df.info())

# Filter based on 'is_duplicate' column
Oceania_df = Oceania_df[Oceania_df['is_duplicate']]

# Drop 'is_duplicate' column
Oceania_df.drop(columns='is_duplicate', inplace=True)

# Reset index after filtering
Oceania_df.reset_index(drop=True, inplace=True)

# Check number of incomplete scenarios
print(Oceania_df.info())
# From 2.269.124 entries to 2.190.686 entries

# %%
# Export cleaned Oceania_df
Oceania_df.to_csv('Oceania_Clean.csv', index=False)
