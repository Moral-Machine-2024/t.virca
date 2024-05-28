# %%
# Import pandas
import pandas as pd

# Read cultures file
cult = pd.read_csv('cultures.csv')

# %%
# Head and info
print(cult.head())
print()
print(cult.info())
# --> There is one missing value

# %%
# View row with missing value
null_row = cult[cult['categories'].isnull()]
print(null_row)
# index: 46, countries: ISR, categories: NAN

# %%
# Drop row with missing value
cult = cult.dropna(subset=['categories'])
print(cult.info())

# %%
# View countries, place in list
print(cult['countries'].to_list())

# %%
# Cultures
print(cult['categories'].unique())
# ['Orthodox' 'Islamic' 'LatinAmerica' 'English' 'Catholic' 'Protestant'
# 'Confucian' 'Baltic' 'SouthAsia']

# Number of cultures
print(cult['categories'].nunique())
# 9

# %%
# Visualize countries with culture
# Import libraries
import geopandas as gpd
import matplotlib.pyplot as plt

# Read in the world map data
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# List of ISO3 country codes to be highlighted in the map
countries = ['ALB', 'ARE', 'ARG', 'ARM', 'AUS', 'AUT', 'AZE', 'BEL', 'BGD', 'BGR',
                      'BIH', 'BLR', 'BOL', 'BRA', 'CAN', 'CHE', 'CHL', 'CHN', 'COL', 'CRI',
                      'CYP', 'CZE', 'DEU', 'DNK', 'DOM', 'DZA', 'ECU', 'EGY', 'ESP', 'EST',
                      'FIN', 'FRA', 'GBR', 'GEO', 'GRC', 'GTM', 'HKG', 'HND', 'HRV', 'HUN',
                      'IDN', 'IND', 'IRL', 'IRN', 'IRQ', 'ISL', 'ITA', 'JAM', 'JOR', 'JPN',
                      'KAZ', 'KEN', 'KHM', 'KOR', 'KWT', 'LBN', 'LKA', 'LTU', 'LUX', 'LVA',
                      'MAC', 'MAR', 'MDA', 'MEX', 'MKD', 'MLT', 'MNG', 'MNE', 'MUS', 'MYS',
                      'NCL', 'NLD', 'NOR', 'NPL', 'NZL', 'PAK', 'PAN', 'PER', 'PHL', 'POL',
                      'PRI', 'PRT', 'PRY', 'PSE', 'QAT', 'REU', 'ROU', 'RUS', 'SAU', 'SGP',
                      'SLV', 'SRB', 'SVK', 'SVN', 'SWE', 'THA', 'TTO', 'TUN', 'TUR', 'TWN',
                      'UKR', 'URY', 'USA', 'VEN', 'VNM', 'ZAF']

# Create a new column in the 'world' df to mark countries to color
world['color'] = ['green' if country in countries else 'lightgray' for country in world['iso_a3']]

# Plot the map
fig, ax = plt.subplots(figsize=(10, 6))
world.plot(ax=ax, color=world['color'])
plt.title('Countries to be included in the sample')
plt.axis('off')
plt.show()

# %%
import pycountry_convert as pc

# Create a dictionary to store countries by continent
continent_countries = {
    'Africa': [],
    'Asia': [],
    'Europe': [],
    'North America': [],
    'South America': [],
    'Oceania': []
}

# Categorize countries by continent
for country_code in countries:
    try:
        country_alpha2 = pc.country_alpha3_to_country_alpha2(country_code)
        continent_code = pc.country_alpha2_to_continent_code(country_alpha2)
        continent_name = pc.convert_continent_code_to_continent_name(continent_code)
        continent_countries[continent_name].append(country_code)
    except KeyError:
        print(f"Could not find continent for country code: {country_code}")

# Lists for each continent
africa = continent_countries['Africa']
asia = continent_countries['Asia']
europe = continent_countries['Europe']
north_america = continent_countries['North America']
south_america = continent_countries['South America']
oceania = continent_countries['Oceania']

# %%
print('Countries in Africa: ', africa)
print('Number: ', len(africa))
print()
print('Countries in Asia', asia)
print('Number: ', len(asia))
print()
print('Countries in Europe', europe)
print('Number: ', len(europe))
print()
print('Countries in North America', north_america)
print('Number: ', len(north_america))
print()
print('Countries in South America', south_america)
print('Number: ', len(south_america))
print()
print('Countries in Oceania', oceania)
print('Number: ', len(oceania))
