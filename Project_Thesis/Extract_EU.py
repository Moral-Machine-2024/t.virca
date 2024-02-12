# Extract EU respondents data from SharedResponses
# Import libraries
import pandas as pd

# Check that all EU countries are present (Use SharedResponsesFullFirstSessions instead of SharedResponses
# for ease of computation)
FFS = pd.read_csv('SharedResponsesFullFirstSessions.csv')

# UserCountry3 unique values and sort
countries_ISO3 = sorted(FFS['UserCountry3'].astype(str).unique())

# Print complete list of countries (ISO3) in alphabetical order
print(countries_ISO3)

# Extract EU countries data from SharedResponses and make new csv file
# Set chunk size
chunk_size = 100000

# Initialize empty df
SharedResponsesEU = pd.DataFrame()
#
# I understand that there is missing Data from Cyprus in this data set. Please do confirm if this is indeed the case.
#
eu_countries = ['AUT', 'BEL', 'BGR', 'HRV', 'CYP', 'CZE', 'DNK', 'EST', 'FIN', 'FRA',
                'DEU', 'GRC', 'HUN', 'IRL', 'ITA', 'LVA', 'LTU', 'LUX', 'MLT', 'NLD',
                'POL', 'PRT', 'ROU', 'SVK', 'SVN', 'ESP', 'SWE']

# Read csv in chunks
for chunk in pd.read_csv('SharedResponses.csv', chunksize=chunk_size, dtype=str, low_memory=False):
    # Filter rows where user country is EU
    eu_chunk = chunk[chunk['UserCountry3'].isin(eu_countries)]

    # Append filtered chunk to empty df
    SharedResponsesEU = pd.concat([SharedResponsesEU, eu_chunk], ignore_index=True)

# Save resulting df to new csv file
SharedResponsesEU.to_csv('SharedResponsesEU.csv', sep=',', index=False)

# Head
print(SharedResponsesEU.head())

# Info
print(SharedResponsesEU.info())
