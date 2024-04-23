# %%
### Perform sanity check for each abstract feature on the final dataframe sampled ###

# Import libraires
import pandas as pd
import random

# %%
# Load FINAL_DF (final merged df, after adding columns with feature engineering)

# For computational efficieny when loading the data:
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
# Print df
print(df.info())

# %%
# Set random seed
random.seed(42)

# %%
# 'Intervention'
# Print 10 random rows with columns relevant for 'Intervention'
print(df[['Intervene', 'Intervention']].sample(10))

# %%
# 'Male'
# Print 10 random rows with columns relevant for 'Male'
print(df[['Man', 'OldMan', 'Boy', 'LargeMan', 'MaleExecutive', 'MaleAthlete', 'MaleDoctor',
                  'Male']].sample(10))

# %%
# 'Female'
# Print 10 random rows with columns relevant for 'Female'
print(df[['Woman', 'Pregnant', 'OldWoman', 'Girl', 'LargeWoman', 'FemaleExecutive', 'FemaleAthlete',
                  'FemaleDoctor', 'Female']].sample(10))

# %%
# 'Young'
# Print 10 random rows with columns relevant for 'Young'
print(df[['Boy', 'Girl', 'Stroller', 'Young']].sample(10))

# %%
# 'Old'
# Print 10 random rows with columns relevant for 'Old'
print(df[['OldMan', 'OldWoman', 'Old']].sample(10))

# %%
# 'Infancy'
# Print 10 random rows with columns relevant for 'Infancy'
print(df[['Stroller', 'Infancy']].sample(10))

# %%
# 'Pregnancy'
# Print 10 random rows with columns relevant for 'Pregnancy'
print(df[['Pregnant', 'Pregnancy']].sample(10))

# %%
# 'Fat'
# Print 10 random rows with columns relevant for 'Fat'
print(df[['LargeWoman', 'LargeMan', 'Fat']].sample(10))

# %%
# 'Fit'
# Print 10 random rows with columns relevant for 'Fit'
print(df[['MaleAthlete', 'FemaleAthlete', 'Fit']].sample(10))

# %%
# 'Working'
# Print 10 random rows with columns relevant for 'Working'
print(df[['FemaleExecutive', 'MaleExecutive', 'Working']].sample(10))

# %%
# 'Medical'
# Print 10 random rows with columns relevant for 'Medical'
print(df[['FemaleDoctor', 'MaleDoctor', 'Medical']].sample(10))

# %%
# 'Homelessness'
# Print 10 random rows with columns relevant for 'Homelessness'
print(df[['Homeless', 'Homeless']].sample(10))

# %%
# 'Criminality'
# Print 10 random rows with columns relevant for 'Criminality'
print(df[['Criminal', 'Criminal']].sample(10))

# %%
# 'Human'
# Print 10 random rows with columns relevant for 'Human'
print(df[['Man', 'Woman', 'Pregnant', 'Stroller', 'OldMan', 'OldWoman', 'Boy', 'Girl',
                  'Homeless', 'LargeWoman', 'LargeMan', 'Criminal', 'MaleExecutive', 'FemaleExecutive',
                  'FemaleAthlete', 'MaleAthlete', 'FemaleDoctor', 'MaleDoctor', 'Human']].sample(10))

# %%
# 'Non-human'
# Print 10 random rows with columns relevant for 'Non-Human'
print(df[['Cat', 'Dog', 'Non-human']].sample(10))

# %%
# 'Passenger'
# Print 10 random rows with columns relevant for 'Passenger'
print(df[['NumberOfCharacters', 'Barrier', 'Passenger']].sample(10))

# %%
# 'Law Abiding' and 'Law Violating'
# Print 10 random rows with columns relevant for 'Law Abiding', and 'Law Violating'
print(df[['CrossingSignal_1', 'CrossingSignal_2', 'NumberOfCharacters', 'Law Abiding', 'Law Violating']].sample(10))
