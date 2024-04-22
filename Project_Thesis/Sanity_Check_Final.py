
### Perform sanity check for each abstract feature on the first sub-sample (Africa) ###

# %%
# Import libraries
import pandas as pd
import random

# %%
# Load New_Africa sample (sub-sample after applying the function calculate_abstract_features)
new_africa = pd.read_csv('New_Africa.csv')

# %%
# Set random seed
random.seed(42)

# %%
# 'Intervention'
# Print 10 random rows with columns relevant for 'Intervention'
print(new_africa[['Intervene', 'Intervention']].sample(10))

# %%
# 'Male'
# Print 10 random rows with columns relevant for 'Male'
print(new_africa[['Man', 'OldMan', 'Boy', 'LargeMan', 'MaleExecutive', 'MaleAthlete', 'MaleDoctor',
                  'Male']].sample(10))

# %%
# 'Female'
# Print 10 random rows with columns relevant for 'Female'
print(new_africa[['Woman', 'Pregnant', 'OldWoman', 'Girl', 'LargeWoman', 'FemaleExecutive', 'FemaleAthlete',
                  'FemaleDoctor', 'Female']].sample(10))

# %%
# 'Young'
# Print 10 random rows with columns relevant for 'Young'
print(new_africa[['Boy', 'Girl', 'Stroller', 'Young']].sample(10))

# %%
# 'Old'
# Print 10 random rows with columns relevant for 'Old'
print(new_africa[['OldMan', 'OldWoman', 'Old']].sample(10))

# %%
# 'Infancy'
# Print 10 random rows with columns relevant for 'Infancy'
print(new_africa[['Stroller', 'Infancy']].sample(10))

# %%
# 'Pregnancy'
# Print 10 random rows with columns relevant for 'Pregnancy'
print(new_africa[['Pregnant', 'Pregnancy']].sample(10))

# %%
# 'Fat'
# Print 10 random rows with columns relevant for 'Fat'
print(new_africa[['LargeWoman', 'LargeMan', 'Fat']].sample(10))

# %%
# 'Fit'
# Print 10 random rows with columns relevant for 'Fit'
print(new_africa[['MaleAthlete', 'FemaleAthlete', 'Fit']].sample(10))

# %%
# 'Working'
# Print 10 random rows with columns relevant for 'Working'
print(new_africa[['FemaleExecutive', 'MaleExecutive', 'Working']].sample(10))

# %%
# 'Medical'
# Print 10 random rows with columns relevant for 'Medical'
print(new_africa[['FemaleDoctor', 'MaleDoctor', 'Medical']].sample(10))

# %%
# 'Homelessness'
# Print 10 random rows with columns relevant for 'Homelessness'
print(new_africa[['Homeless', 'Homeless']].sample(10))

# %%
# 'Criminality'
# Print 10 random rows with columns relevant for 'Criminality'
print(new_africa[['Criminal', 'Criminal']].sample(10))

# %%
# 'Human'
# Print 10 random rows with columns relevant for 'Human'
print(new_africa[['Man', 'Woman', 'Pregnant', 'Stroller', 'OldMan', 'OldWoman', 'Boy', 'Girl',
                  'Homeless', 'LargeWoman', 'LargeMan', 'Criminal', 'MaleExecutive', 'FemaleExecutive',
                  'FemaleAthlete', 'MaleAthlete', 'FemaleDoctor', 'MaleDoctor', 'Human']].sample(10))

# %%
# 'Non-human'
# Print 10 random rows with columns relevant for 'Non-Human'
print(new_africa[['Cat', 'Dog', 'Non-human']].sample(10))

# %%
# 'Passenger'
# Print 10 random rows with columns relevant for 'Passenger'
print(new_africa[['NumberOfCharacters', 'Barrier', 'Passenger']].sample(10))

# %%
# 'Law Abiding' and 'Law Violating'
# Print 10 random rows with columns relevant for 'Law Abiding', and 'Law Violating'
print(new_africa[['CrossingSignal_1', 'CrossingSignal_2', 'NumberOfCharacters', 'Law Abiding', 'Law Violating']].sample(10))
