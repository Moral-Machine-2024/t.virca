
############################ Feature Engineering ############################

# %%
# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
### Create binary matrix for computing abstract features ###
# Define abstract features and characters/characteristics
abstract_features = ['Intervene', 'Male', 'Female', 'Young', 'Old', 'Infancy', 'Pregnancy',
                     'Fat', 'Fit', 'Working', 'Medical', 'Homelessness', 'Criminality', 'Human',
                     'Non-human']
characters = ['Intervention', 'Man', 'Woman', 'Boy', 'Girl', 'OldMan', 'OldWoman', 'Stroller', 'Pregnant',
              'LargeMan', 'LargeWoman', 'MaleAthlete', 'FemaleAthlete', 'MaleExecutive', 'FemaleExecutive',
              'MaleDoctor', 'FemaleDoctor', 'Homeless', 'Criminal', 'Dog', 'Cat']

# Create empty binary matrix
binary_matrix = np.zeros((len(abstract_features), len(characters)), dtype=int)

# Define mappings between abstract features and characters/characteristics
mappings = {
    'Intervene': ['Intervention'],
    'Male': ['Man', 'OldMan', 'Boy', 'LargeMan', 'MaleExecutive', 'MaleAthlete', 'MaleDoctor'],
    'Female': ['Woman', 'Pregnant', 'OldWoman', 'Girl', 'LargeWoman', 'FemaleExecutive', 'FemaleAthlete',
               'FemaleDoctor'],
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
    'Human': ['Man', 'Woman', 'Pregnant', 'Stroller', 'OldMan', 'OldWoman', 'Boy', 'Girl', 'Homeless', 'LargeWoman',
              'LargeMan',
              'Criminal', 'MaleExecutive', 'FemaleExecutive', 'FemaleAthlete', 'MaleAthlete', 'FemaleDoctor',
              'MaleDoctor'],
    'Non-human': ['Cat', 'Dog'],
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
### Visualize bianary_df ###

# Reorder characters
reordered_characters = ['Intervention', 'Man', 'Woman', 'Boy', 'Girl', 'OldMan', 'OldWoman', 'Stroller', 'Pregnant',
                        'LargeMan', 'LargeWoman', 'MaleAthlete', 'FemaleAthlete', 'MaleExecutive', 'FemaleExecutive',
                        'MaleDoctor', 'FemaleDoctor', 'Homeless', 'Criminal', 'Dog', 'Cat']

# Visualize the binary matrix with matplotlib
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

# %%
### Define calculate_abstract_features function ###

def calculate_abstract_features(sample, binary_matrix):
    """
    Calculate abstract features based on the latent feature space binary matrix and add them as columns
    to the original samples

    Arguments:
    - sample (pd.DataFrame): 6 samples collecting responses within each continent
    - binary_matrix (pd.DataFrame): binary matrix containing abstract features as rows and characters as columns

    Returns:
    - The updated sample pd.DataFrame with 18 additional columns containing abstract features counts.
    """

    # Create empty dictionary to store feature counts
    abstract_features_counts = {}

    # Iterate over each abstract feature
    for feature in binary_matrix.index:
        # Initialize count for the current feature to 0
        count = 0

        # Check if the feature is present in the binary matrix
        if feature in binary_matrix.index:
            # Create empty list to store relevant characters for the current feature
            relevant_characters = []
            # Iterate over each character
            for char in binary_matrix.columns:
                # Check if the character has the current feature
                if binary_matrix.loc[feature, char] == 1:
                    # Add the character to the relevant characters list
                    relevant_characters.append(char)
            # Calculate the count of characters with the current feature
            count = sum(sample[char].values for char in relevant_characters)
            # sample[char].values: retrieve value of the column corresponding to the current char in the df
            # for char in relevant_characters: iterate over each char in the list relevant_characters

        # Store the count in the dictionary
        abstract_features_counts[feature] = count

    # Create new columns for the abstract features in the original df
    # Iterate over abstract feature counts
    for feature, count in abstract_features_counts.items():
        # Create a new column for each feature and assign its count
        sample[feature] = count

    # Calculate additional abstract feature counts directly from original df
    # Calculate count of passengers
    sample['Passenger'] = sample['Barrier'] * sample['NumberOfCharacters']
    # Calculate count of characters crossing with a green light
    sample['Law Abiding'] = sample['CrossingSignal_1'] * sample['NumberOfCharacters']
    # Calculate count of characters crossing with a red light
    sample['Law Violating'] = sample['CrossingSignal_2'] * sample['NumberOfCharacters']

    # Return the updated DataFrame
    return sample

# %%
#### Sub-sample: Africa ###
# Load the data
africa = pd.read_csv('Africa_Clean.csv')

# Perform one-hot encoding
africa_encoded = pd.get_dummies(africa['CrossingSignal'], prefix='CrossingSignal')

# Concatenate the one-hot encoded dataframe with the original dataframe
africa = pd.concat([africa, africa_encoded], axis=1)

# Drop the original 'CrossingSignal' column
africa.drop(columns=['CrossingSignal'], inplace=True)

# %%
# Apply function to Africa sample
new_africa = calculate_abstract_features(africa, binary_df)

# %%
# Check columns
print(new_africa.info())

# %%
# Export new_africa
new_africa.to_csv('New_Africa.csv')
