# Extract USA respondents data from SharedResponses
# Import libraries
import pandas as pd

# Set chunk size
chunk_size = 100000

# Initialize empty df
SharedResponsesUSA = pd.DataFrame()

# Read csv in chunks
for chunk in pd.read_csv('SharedResponses.csv', chunksize=chunk_size, dtype=str, low_memory=False):
    # Filter rows where user country is USA
    usa_chunk = chunk[chunk['UserCountry3'] == 'USA']

    # Append filtered chunk to empty df
    SharedResponsesUSA = pd.concat([SharedResponsesUSA, usa_chunk], ignore_index=True)

# Save resulting df to new csv file
SharedResponsesUSA.to_csv('SharedResponsesUSA.csv', sep=',', index=False)

# Head
print(SharedResponsesUSA.head())

# Info
print(SharedResponsesUSA.info())
