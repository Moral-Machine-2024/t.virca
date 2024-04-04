# %%
### Sampling per continent ###
# Import libraries
import pandas as pd

# Set chunk size
chunk_size = 100000

# Initialize empty dfs
africa = pd.DataFrame()
asia = pd.DataFrame()
europe = pd.DataFrame()
north_america = pd.DataFrame()
south_america = pd.DataFrame()
oceania = pd.DataFrame()

# Lists of ISO3 countries per continent
countries_africa = ['DZA', 'EGY', 'KEN', 'MAR', 'MUS', 'REU', 'TUN', 'ZAF']
countries_asia = ['ARE', 'ARM', 'AZE', 'BGD', 'CHN', 'CYP', 'GEO', 'HKG', 'IDN', 'IND',
                  'IRN', 'IRQ', 'JOR', 'JPN', 'KAZ', 'KHM', 'KOR', 'KWT', 'LBN', 'LKA',
                  'MAC', 'MNG', 'MYS', 'NPL', 'PAK', 'PHL', 'PSE', 'QAT', 'SAU', 'SGP',
                  'THA', 'TUR', 'TWN', 'VNM']
countries_europe = ['ALB', 'AUT', 'BEL', 'BGR', 'BIH', 'BLR', 'CHE', 'CZE', 'DEU', 'DNK',
                    'ESP', 'EST', 'FIN', 'FRA', 'GBR', 'GRC', 'HRV', 'HUN', 'IRL', 'ISL',
                    'ITA', 'LTU', 'LUX', 'LVA', 'MDA', 'MKD', 'MLT', 'MNE', 'NLD', 'NOR',
                    'POL', 'PRT', 'ROU', 'RUS', 'SRB', 'SVK', 'SVN', 'SWE', 'UKR']
countries_north_america = ['CAN', 'CRI', 'DOM', 'GTM', 'HND', 'JAM', 'MEX', 'PAN', 'PRI', 'SLV',
                           'TTO', 'USA']
countries_south_america = ['ARG', 'BOL', 'BRA', 'CHL', 'COL', 'ECU', 'PER', 'PRY', 'URY', 'VEN']
countries_oceania = ['AUS', 'NCL', 'NZL']

# %%
# Read culture file
cult = pd.read_csv('cultures.csv')

# Drop row with missing value and print info
cult = cult.dropna(subset=['categories'])

# Info
print(cult.info())
print()

# Head
print(cult.head())

# %%
# Rename column 'countries' to 'UserCountry3'
cult.rename(columns={'countries': 'UserCountry3'}, inplace=True)

print(cult.info())

# %%
### Extract responses from AFRICA ###
# Read csv in chunks
for chunk in pd.read_csv('SharedResponses.csv', chunksize=chunk_size, dtype=str, low_memory=False):
    # Filter rows where user country is in Africa
    africa_chunk = chunk[chunk['UserCountry3'].isin(countries_africa)]

    # Append filtered chunk to empty df
    africa = pd.concat([africa, africa_chunk], ignore_index=True)

# Add culture column to Africa sample
print('Now adding culture column')
print()

africa = pd.merge(africa, cult[['UserCountry3', 'categories']], on='UserCountry3', how='left')

# Save resulting df to new csv file
africa.to_csv('Africa_sample.csv', sep=',', index=False)

# Head
print(africa.head())
print()

# Info
print(africa.info())
# RangeIndex: 323.066 entries
print()

# Unique cultures in the Africa sample
print(africa['categories'].unique())
# ['Islamic' 'Catholic' 'SouthAsia']

# %%
# Read Africa_sample
Africa_df = pd.read_csv('Africa_sample.csv')

# Check - South Asian culture
south_asia_rows = Africa_df.loc[Africa_df['categories'] == 'SouthAsia', ['UserCountry3', 'categories']]
print(south_asia_rows['UserCountry3'].unique())
# ['MUS'] -> Mauritius (island in East Africa)

# %%
### Extract responses from ASIA ###
# Read csv in chunks
for chunk in pd.read_csv('SharedResponses.csv', chunksize=chunk_size, dtype=str, low_memory=False):
    # Filter rows where user country is in Asia
    asia_chunk = chunk[chunk['UserCountry3'].isin(countries_asia)]

    # Append filtered chunk to empty df
    asia = pd.concat([asia, asia_chunk], ignore_index=True)

# Add culture column to Asia sample
print('Now adding culture column')
print()

asia = pd.merge(asia, cult[['UserCountry3', 'categories']], on='UserCountry3', how='left')

# Save resulting df to new csv file
asia.to_csv('Asia_sample.csv', sep=',', index=False)

# Head
print(asia.head())
print()

# Info
print(asia.info())
# RangeIndex: 6.676.416
print()

# Unique cultures in the Asia sample
print(asia['categories'].unique())
# ['Islamic' 'LatinAmerica' 'SouthAsia' 'Confucian' 'Orthodox']

# %%
# Read Asia_sample
Asia_df = pd.read_csv('Asia_sample.csv')

# %%
# Check Latin America culture in Asia
latin_american_rows = Asia_df.loc[Asia_df['categories'] == 'LatinAmerica', ['UserCountry3', 'categories']]
print(latin_american_rows['UserCountry3'].unique())
# ['PHL'] -> Philippines

# %%
# Double check that Philippines is LatinAmerica culture
print(cult.loc[cult['UserCountry3'] == 'PHL', ['UserCountry3', 'categories']])
# --> Correct

# %%
### Extract responses from EUROPE ###
# Read csv in chunks
for chunk in pd.read_csv('SharedResponses.csv', chunksize=chunk_size, dtype=str, low_memory=False):
    # Filter rows where user country is in Europe
    europe_chunk = chunk[chunk['UserCountry3'].isin(countries_europe)]

    # Append filtered chunk to empty df
    europe = pd.concat([europe, europe_chunk], ignore_index=True)

# Add culture column to Europe sample
print('Now adding culture column')
print()

europe = pd.merge(europe, cult[['UserCountry3', 'categories']], on='UserCountry3', how='left')

# Save resulting df to new csv file
europe.to_csv('Europe_sample.csv', sep=',', index=False)

# Head
print(europe.head())
print()

# Info
print(europe.info())
# RangeIndex: 32.935.386
print()

# Unique cultures in the Europe sample
print(europe['categories'].unique())
# ['Catholic' 'Protestant' 'Orthodox' 'English' 'Baltic']

# %%
### Extract responses from NORTH AMERICA ###
# Read csv in chunks
for chunk in pd.read_csv('SharedResponses.csv', chunksize=chunk_size, dtype=str, low_memory=False):
    # Filter rows where user country is in North America
    north_america_chunk = chunk[chunk['UserCountry3'].isin(countries_north_america)]

    # Append filtered chunk to empty df
    north_america = pd.concat([north_america, north_america_chunk], ignore_index=True)

# Add culture column to North America sample
print('Now adding culture column')
print()

north_america = pd.merge(north_america, cult[['UserCountry3', 'categories']], on='UserCountry3', how='left')

# Save resulting df to new csv file
north_america.to_csv('NorthAmerica_sample.csv', sep=',', index=False)

# Head
print(north_america.head())
print()

# Info
print(north_america.info())
# RangeIndex: 21.475.167
print()

# Unique cultures in North America sample
print(north_america['categories'].unique())
# ['English' 'LatinAmerica']

# %%
# Read NorthAmerica_sample
NorthAmerica_df = pd.read_csv('NorthAmerica_sample.csv')

# %%
### Extract responses from SOUTH AMERICA ###
# Read csv in chunks
for chunk in pd.read_csv('SharedResponses.csv', chunksize=chunk_size, dtype=str, low_memory=False):
    # Filter rows where user country is in South America
    south_america_chunk = chunk[chunk['UserCountry3'].isin(countries_south_america)]

    # Append filtered chunk to empty df
    south_america = pd.concat([south_america, south_america_chunk], ignore_index=True)

# Add culture column to South America sample
print('Now adding culture column')
print()

south_america = pd.merge(south_america, cult[['UserCountry3', 'categories']], on='UserCountry3', how='left')

# Save resulting df to new csv file
south_america.to_csv('SouthAmerica_sample.csv', sep=',', index=False)

# Head
print(south_america.head())
print()

# Info
print(south_america.info())
# RangeIndex: 5.329.471
print()

# Unique cultures in South America sample
print(south_america['categories'].unique())
# ['LatinAmerica']

# %%
### Extract responses from OCEANIA ###
# Read csv in chunks
for chunk in pd.read_csv('SharedResponses.csv', chunksize=chunk_size, dtype=str, low_memory=False):
    # Filter rows where user country is in Oceania
    oceania_chunk = chunk[chunk['UserCountry3'].isin(countries_oceania)]

    # Append filtered chunk to empty df
    oceania = pd.concat([oceania, oceania_chunk], ignore_index=True)

# Add culture column to Oceania sample
print('Now adding culture column')
print()

oceania = pd.merge(oceania, cult[['UserCountry3', 'categories']], on='UserCountry3', how='left')

# Save resulting df to new csv file
oceania.to_csv('Oceania_sample.csv', sep=',', index=False)

# Head
print(oceania.head())
print()

# Info
print(oceania.info())
# RangeIndex: 2.269.192
print()

# Unique cultures in Oceania sample
print(oceania['categories'].unique())
# ['English' 'Catholic']
