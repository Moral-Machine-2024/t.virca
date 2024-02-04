# Import libraries
import pandas as pd

# File 1: CountriesChangePr.csv
# File 2: SharedResponse.csv (excluded here)
# File 3: SharedResponsesFullFirstSessions.csv
# File 4: SharedResponseSurvey.csv

# Info file 1
file_1 = pd.read_csv('CountriesChangePr.csv')
print(file_1.info())

# Info file 3
file_3 = pd.read_csv('SharedResponsesFullFirstSessions.csv')
print(file_3.info())

# Info file 4
file_4 = pd.read_csv('SharedResponsesSurvey.csv')
print(file_4.info())





