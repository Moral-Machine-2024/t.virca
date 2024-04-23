# Moral Machine Experiment - Studying the influence of moral principles on decisions
Brief description...

## Dataset
The datasets used in this project can be retrieved at https://goo.gl/JXRrBP
1. **cultures.csv** : contains two columns namely countries' ISO3 values and their respective culture according to the Inglehart-Welzel Cultural Map. 
2. **SharedResponses.csv** : contains responses to the Moral Machine Experiment. 

## Files:
### 1_Read_Cultures
- The **cultures.csv** dataset is explored in this file. 
- The following 9 cultures are identified: 'Orthodox', 'Islamic', 'LatinAmerica', 'English', 'Catholic', 'Protestant', 'Confucian', 'Baltic', 'SouthAsia'.
- A map of all countries which are assigned a culture in the dataset was created using the libraries matplotlib and geopandas. Only these countries are going to be considered in the project.
- The considered countries (ISO3) are then categorized by continent with the library pycountry_convert. A list of countries is made for each continent. 

### 2_Sampling_Per_Continent 
- 6 lists are defined, one for each continent, containing countries' ISO3 values. 
- A for loop is used to read the dataset **SharedResponses.csv** in chunks (due to the large size), extract observations from a specified continent, and add a 'Culture' column which specifies the culture of each country according to the **cultures.csv** dataset.
- 6 samples are extracted and saved to csv: 'Africa_sample', 'Asia_sample', 'Europe_sample', 'NorthAmerica_sample', 'SouthAmerica_sample', Oceania_sample'.

### 3_Data_Cleaning_New

### 4_Create_Final_Dataframe

### 5_Latent_Feature_Space

### 6_Feature_Engineering

### 7_Sanity_Check

### 8_Visualize_Distributions


