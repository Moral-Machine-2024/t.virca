# %%
# Latent Feature Space - Binary Matrix Visualization
## Mapping of charcaters to abstract features
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Define abstract features and characters/characteristics
abstract_features = ['Intervene', 'Male', 'Female', 'Young', 'Old', 'Infancy', 'Pregnancy',
                     'Fat', 'Fit', 'Working', 'Medical', 'Homelessness', 'Criminality', 'Human',
                     'Non-human', 'Passenger', 'Law Abiding', 'Law Violating']
characters = ['Intervention', 'Man', 'Woman', 'Boy', 'Girl', 'OldMan', 'OldWoman', 'Stroller', 'Pregnant',
              'LargeMan', 'LargeWoman', 'MaleAthlete', 'FemaleAthlete', 'MaleExecutive', 'FemaleExecutive',
              'MaleDoctor', 'FemaleDoctor', 'Homeless', 'Criminal', 'Dog', 'Cat', 'Barrier',
              'CrossingSignal_1', 'CrossingSignal_2']

# Create empty binary matrix
binary_matrix = np.zeros((len(abstract_features), len(characters)), dtype=int)

# Define mappings between abstract features and characters/characteristics
mappings = {
    'Intervene': ['Intervention'],
    'Male': ['Man', 'OldMan', 'Boy', 'LargeMan', 'MaleExecutive', 'MaleAthlete', 'MaleDoctor'],
    'Female': ['Woman', 'Pregnant', 'OldWoman', 'Girl', 'LargeWoman', 'FemaleExecutive', 'FemaleAthlete', 'FemaleDoctor'],
    'Young': ['Boy', 'Girl', 'Stroller'],
    'Old': ['OldMan', 'OldWoman'],
    'Infancy': ['Stroller'],
    'Pregnancy': ['Pregnant'],
    'Fat': ['LargeWoman', 'LargeMan'],
    'Fit': ['MaleAthlete', 'FemaleAthlete'],
    'Working': ['FemaleExecutive', 'MaleExecutive'],
    'Medical': ['FemaleDoctor', 'MaleDoctor'],
    'Homelessness': ['Homeless'],
    'Criminality': ['Criminal'],
    'Human': ['Man', 'Woman', 'Pregnant', 'Stroller', 'OldMan', 'OldWoman', 'Boy', 'Girl', 'Homeless', 'LargeWoman', 'LargeMan',
              'Criminal', 'MaleExecutive', 'FemaleExecutive', 'FemaleAthlete', 'MaleAthlete', 'FemaleDoctor', 'MaleDoctor'],
    'Non-human': ['Cat', 'Dog'],
    'Passenger': ['Barrier'],
    'Law Abiding': ['CrossingSignal_1'],
    'Law Violating': ['CrossingSignal_2']
}

# Populate the binary matrix based on the mappings
for i, feature in enumerate(abstract_features):
    # i: index of the current feature in the abstract_features list
    # feature: value of the current feature being iterated over
    # enumerate: used to iterate over abstract_features list
    for j, character in enumerate(characters):
        # j: index of the current character in the characters list
        # character: value of the current character being iterated over
        # enumerate: used to iterate over characters list
        if character in mappings[feature]:
        # Check if the current character is present in the list of characters mapped to the current feature
            binary_matrix[i, j] = 1
            # If so, set the value of the element at the specific row and column to 1
            # [the feature is present in the character]

# Store binary matrix in a df
binary_df = pd.DataFrame(binary_matrix, index=abstract_features, columns=characters)

# %%
# Reorder characters
reordered_characters = ['Intervention', 'Man', 'Woman', 'Boy', 'Girl', 'OldMan', 'OldWoman', 'Stroller', 'Pregnant',
                        'LargeMan', 'LargeWoman', 'MaleAthlete', 'FemaleAthlete', 'MaleExecutive', 'FemaleExecutive',
                        'MaleDoctor', 'FemaleDoctor', 'Homeless', 'Criminal', 'Dog', 'Cat', 'Barrier',
                        'CrossingSignal_1', 'CrossingSignal_2']

# Visualize the binary matrix
plt.figure(figsize=(15, 10))
plt.imshow(binary_df.loc[:, reordered_characters], cmap='binary', aspect='auto')
plt.xlabel('Characters/Characteristics')
plt.ylabel('Abstract Features')
plt.title('Binary Matrix Decomposing Characters into Abstract Features')
plt.xticks(np.arange(len(reordered_characters)), reordered_characters, rotation=45, ha='right')
plt.yticks(np.arange(len(abstract_features)), abstract_features)
plt.show()

# %%
# View binary dataframe
print(binary_df)

