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
# rows 24.773.479 x 41 columns
# dtypes - object, float, int

# Summary statistics
print(data_EU.describe())

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
drop_columns = ['UserID', 'Template', 'DescriptionShown', 'LeftHand']
data_EU = data_EU.drop(columns=drop_columns, axis=1)
print(data_EU.isnull().sum())

# %%
# Drop 30 NaN rows ScenarioType + all characters encoding
data_EU = data_EU.dropna(subset=['ScenarioType'])
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

# --> how to deal with these missing values?

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
# Extract preference for each row based on 'AttributeLevel' and 'Saved'
# Attempt to extract an outcome preference for each scenario (two rows which form scenario merged later)

# Create new column 'Preference'
data_EU['Preference'] = ''

# Iterate over each row in the df
for index, row in data_EU.iterrows():
    if row['Saved'] == 1:
        # If row is saved, row attribute level is preference
        data_EU.at[index, 'Preference'] = row['AttributeLevel']
    else:
        # If row is not saved, opposite attribute level is preference
        if row['AttributeLevel'] == 'Female':
            data_EU.at[index, 'Preference'] = 'Male'
        elif row['AttributeLevel'] == 'Male':
            data_EU.at[index, 'Preference'] = 'Female'
        elif row['AttributeLevel'] == 'Old':
            data_EU.at[index, 'Preference'] = 'Young'
        elif row['AttributeLevel'] == 'Young':
            data_EU.at[index, 'Preference'] = 'Old'
        elif row['AttributeLevel'] == 'Fat':
            data_EU.at[index, 'Preference'] = 'Fit'
        elif row['AttributeLevel'] == 'Fit':
            data_EU.at[index, 'Preference'] = 'Fat'
        elif row['AttributeLevel'] == 'Low':
            data_EU.at[index, 'Preference'] = 'High'
        elif row['AttributeLevel'] == 'High':
            data_EU.at[index, 'Preference'] = 'Low'
        elif row['AttributeLevel'] == 'Pets':
            data_EU.at[index, 'Preference'] = 'Hoomans'
        elif row['AttributeLevel'] == 'Hoomans':
            data_EU.at[index, 'Preference'] = 'Pets'
        elif row['AttributeLevel'] == 'More':
            data_EU.at[index, 'Preference'] = 'Less'
        elif row['AttributeLevel'] == 'Less':
            data_EU.at[index, 'Preference'] = 'More'
        elif row['AttributeLevel'] == 'Rand':
            data_EU.at[index, 'Preference'] = 'Rand'

# Extract preferences: Response ID, ScenarioTypeStrict, AttributeLevel, Saved, Preference columns
columns = ['ResponseID', 'ScenarioTypeStrict', 'AttributeLevel', 'Saved', 'Preference']
preferences_df = data_EU[columns]

print(preferences_df.head(20))
print()
print(preferences_df.info())
print()
print(preferences_df.isna().sum())

# --> How to extract values when AttributeLevel = Rand (?)

# %%
# Combine based on ResponseID
# Drop columns where rows have different values
preferences_df_2 = preferences_df.drop(['AttributeLevel', 'Saved'], axis=1)

# Groupby
preferences_df_2 = preferences_df_2.groupby('ResponseID', as_index=False).first()

print(preferences_df_2.head(20))
print()
print(preferences_df_2.info())
# Roughly half of the entries, as expected

# %%
# ... Univariate / Bivariate analysis
# ... Correlations
# ... Analyze categorical variables / plots
# ... Outliers?
# ... Identify target variable / visualize
