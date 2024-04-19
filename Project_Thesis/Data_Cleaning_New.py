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
### Change dtypes for computational efficiency ###
# Convert object variables to categorical
object_cols = ['ResponseID', 'AttributeLevel', 'ScenarioTypeStrict', 'UserCountry3', 'Cultures']
Africa_df[object_cols] = Africa_df[object_cols].astype('category')

# List of numerical column names
numerical_cols = ['Intervention', 'PedPed', 'Barrier', 'CrossingSignal',
                  'NumberOfCharacters', 'DiffNumberOFCharacters', 'Saved', 'Man',
                  'Woman', 'Pregnant', 'Stroller', 'OldMan', 'OldWoman', 'Boy',
                  'Girl', 'Homeless', 'LargeWoman', 'LargeMan', 'Criminal',
                  'MaleExecutive', 'FemaleExecutive', 'FemaleAthlete', 'MaleAthlete',
                  'FemaleDoctor', 'MaleDoctor', 'Dog', 'Cat']

# Set dtype of numerical columns to int16 (range -32768 to 32767; 2 as opposed to 8 bytes)
Africa_df[numerical_cols] = Africa_df[numerical_cols].astype('int16')

# Check the updated dtypes
print(Africa_df.dtypes)

# %%
# Export cleaned Africa_df
Africa_df.to_csv('Africa_Clean.csv', index=False)

# %%
#--------------------------## ASIA ##--------------------------#
# Info
print(Asia_df.info())
# RangeIndex: 6.676.416