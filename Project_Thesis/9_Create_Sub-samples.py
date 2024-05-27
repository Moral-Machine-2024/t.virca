
#################### Create various sub-samples ####################

# Import libraries / functions
import pandas as pd
from Create_Final_Dataframe import create_sub_sample
from Create_Final_Dataframe import verify_proportions

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
###################### Create three sub-samples of increasing size ######################

# "proportion" argument in create_sub_sample function
size_S = 0.0001
size_M = 0.001
size_L = 0.01

# "Columns" argument in verify_proportions function
columns_to_verify = ['Saved', 'UserCountry3', 'Cultures']

# %%
# Run function with size_S
df_S = create_sub_sample(df, size_S)

print(df_S.info())
print()
print(df_S.head())

# %%
# Run function with size_M
df_M = create_sub_sample(df, size_M)

print(df_M.info())
print()
print(df_M.head())

# %%
# Run function with size_L
df_L = create_sub_sample(df, size_L)

print(df_L.info())
print()
print(df_L.head())

# %%
# Verify proportions in the sub-samples
print("Proportions and counts in sub-sample with size_S:")
verify_proportions(df_S, columns_to_verify)
print("Proportions and counts in sub-sample with size_M:")
verify_proportions(df_M, columns_to_verify)
print("Proportions and counts in sub-sample with size_L:")
verify_proportions(df_L, columns_to_verify)

# %%
# Export reduced dfs
df_S.to_csv('df_S_New', index=False)
df_M.to_csv('df_M_New', index=False)
df_M.to_csv('df_L_New', index=False)

# %%
##################### Samples: Netherlands, Japan, Singapore #####################
## Extract a sample with all responses from the Netherlands
# Extract rows with 'NLD' in the 'UserCountry3' column
nld_sample = df[df['UserCountry3'] == 'NLD']

# Display the sample
print(nld_sample.info())
print()
print(nld_sample.head())

# %%
# Only use half of the rows for the Netherlands sample
nld_sample_sub = nld_sample.sample(frac=0.5)
print(nld_sample_sub.info())
# 254.554 rows

# %%
# Export to csv
nld_sample_sub.to_csv('Netherlands_sample_sub.csv', index=False)

# %%
# Extract a sample with all responses from Japan
# Extract rows with 'JPN' in the 'UserCountry3' column
jpn_sample = df[df['UserCountry3'] == 'JPN']

# Display the sample
print(jpn_sample.info())
print()
print(jpn_sample.head())

# %%
# Only use half of the rows for Japan sample
jpn_sample_sub = jpn_sample.sample(frac=0.5)
print(jpn_sample_sub.info())

# %%
# Export to csv
jpn_sample_sub.to_csv('Japan_sample_sub.csv', index=False)

# %%
# Extract a sample with all responses from Singapore
# Extract rows with 'SGP' in the 'UserCountry3' column
sgp_sample = df[df['UserCountry3'] == 'SGP']

# Display the sample
print(sgp_sample.info())
print()
print(sgp_sample.head())

# %%
# Export to csv
sgp_sample.to_csv('Singapore_sample.csv', index=False)
