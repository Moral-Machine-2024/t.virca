# The Moral Machine Experiment: Predicting Decisions Based on Moral Principles
This repository contains code and instructions to replicate the thesis project *"The Moral Machine Experiment: Predicting Decisions Based on Moral Principles"* conducted for the partial fulfilment of the MSc Data Science & Society at Tilburg University. 

The abstract of the thesis reads as follows:

*This research employs the dataset of the Moral Machine Experiment (MME) provided by Awad et al. (2018) to investigate the influence of moral principles on decisions within the context of autonomous vehicle (AV) moral dilemmas. Unlike previous works, which primarily focus on culturally homogeneous groups, this study examines responses within a culturally diverse sample in order to explore universal ethical considerations. Building on the computational model for extracting abstract features devised by Kim et al. (2018), this research investigates the predictive performance of Random Forest (RF), Support Vector Machine (SVM), and K-Nearest Neighbors (KNN), alongside a dummy classifier, as their potential in relation to the MME remains understudied. The findings suggest that all three models are able to identify patterns in the relationship between moral principles and moral judgements, in particular considering factors such as species, legality and age. Moreover, predictive performance improves with increased sample size and in culturally homogeneous samples. This study contributes to the interdisciplinary field of cognitive modeling and to the academic and policy discussion surrounding mandatory ethics setting for AVs.*

## Dataset
The datasets used in this project can be retrieved at https://goo.gl/JXRrBP
1. **cultures.csv** : contains two columns namely countries' ISO3 values and their respective culture according to the Inglehart-Welzel Cultural Map. 
2. **SharedResponses.csv** : contains responses to the Moral Machine Experiment. 

## Files:
### 1_Read_Cultures
- The **cultures.csv** dataset is explored in this file. 
- The following 9 cultures are identified: 'Orthodox', 'Islamic', 'LatinAmerica', 'English', 'Catholic', 'Protestant', 'Confucian', 'Baltic', 'SouthAsia'.
- A map of all countries which are assigned a culture in the dataset is created using the libraries matplotlib and geopandas. Only these countries are going to be considered in the project.
- The considered countries (ISO3) are then categorized by continent with the library pycountry_convert. A list of countries is made for each continent. 

### 2_Sampling_Per_Continent 
- 6 lists are defined, one for each continent, containing countries' ISO3 values. 
- A for loop is used to read the dataset **SharedResponses.csv** in chunks (due to the large size), extract observations from a specified continent, and add a 'Culture' column which specifies the culture of each country according to the **cultures.csv** dataset.
- 6 samples are extracted and saved to csv: 'Africa_sample', 'Asia_sample', 'Europe_sample', 'NorthAmerica_sample', 'SouthAmerica_sample', Oceania_sample'.

### 3_Data_Cleaning_New
The following operations are performed on each of the extracted samples:
1. Check whether there are duplicated rows
2. Delete unneccessary columns
3. Rename column for clarity
4. Delete rows with missing values
5. Delete incomplete scenarios (two rows form a scenario)
6. Export cleaned sample to csv

### 4_Create_Final_Dataframe
Two functions are created:

**create_sub_sample**: takes a dataframe as input and creates a sub-sample amounting to 50% of the original sample. StratifiedShuffleSplit from the scikit-learn library is used to perform stratified sampling based on country. Additionally, the function makes sure to include both sides of a scenario when selecting the indices of the selected rows. 

**verify_proportions**: takes a dataframe and a list 'columns' as input. The specified columns include 'saved' (the target variable), 'UserCountry3' (countries), and 'Cultures'. The function prints a table containing the count and proportion of each value in the specified columns. This is used to verify that the sub-samples created by **create_sub_sample** respect the proportions of the larger samples. 

**For example:**
Proportions and counts in the entire continent sample:

### Column: 'Saved'

| Count   | Proportion |
|---------|------------|
| 1       | 0.5        |
| 0       | 0.5        |

### Column: 'UserCountry3'

| Country | Count   | Proportion |
|---------|---------|------------|
| ZAF     | 129424  | 0.414964   |
| MAR     | 49870   | 0.159895   |
| EGY     | 45754   | 0.146698   |
| DZA     | 30718   | 0.098489   |
| TUN     | 23650   | 0.075828   |
| REU     | 15746   | 0.050485   |
| KEN     | 8428    | 0.027022   |
| MUS     | 8302    | 0.026618   |

### Column: 'Cultures'

| Culture  | Count   | Proportion |
|----------|---------|------------|
| Islamic  | 287844  | 0.922896   |
| Catholic | 15746   | 0.050485   |
| SouthAsia| 8302    | 0.026618   |

- The two functions are applied to each continent sample to halve their sizes and compare the proportions. 
- Finally, the halved sub-samples are merged into a new dataframe and exported to csv. The number of rows in the merged dataframe is 33.309.960, which means that 16.654.980 scenarios are inlcuded. 

### 5_Latent_Feature_Space
- A binary matrix is created to visually represent the latent feature space as presented in the paper *"A computational model of commonsense moral decision making"* by Kim, Kleiman-Weiner, Abeliuk, Awad, Dsouza, Tenenbaum and Rahwan (2018). 

### 6_Feature_Engineering
- The binary matrix used to visualize the latent feature space is here modified to accomodate the feature engineering process. The abstarct features 'Passenger', 'Law Abiding', 'Law Violating' are removed.
- A function is defined to perform feature engineering on the merged dataframe:

*calculate_abstract_features*: the function takes as argument two dataframes, the merged dataframe and the binary matrix. It calculates abstract feature counts based on the information contained in both dataframe, and returns the merged dataframe with 18 additional columns corresponding to the 18 abstract features.
- The function is applied to the merged dataframe and the outcome is exported to csv. This represents the final dataset to be used for the project. 

### 7_Sanity_Check
- 10 random rows are generate for each abstract feature and other relevant columns used to compute their respective counts. By running the code multiple times on randomly sampled rows it is possible to verify that the computed values of the abstract features are correct.

### 8_Visualize_Distributions
- A bar plot is used to visualize the distribution of the target variable. This confirms that the dataset does not suffer from class imbalance.
- A bar plot is used to visualize the distribution of users across cultures. That is, how many unique users belong to each culture.
- A bar plot per country is not created since it would contain 106 bars. However, the value counts suggest that the United States, Germany and Brazil are the most represented countries. 

## References
Awad, E., Dsouza, S., Kim, R., Henrich, J., Shariff, A., Bonnefon, J.-F., & Rahwan, I. (2018). The moral machine experiment. *Nature*, *563*(7729), 59–64.

Kim, R., Kleiman-Weiner, M., Abeliuk, A., Awad, E., Dsouza, S., Tenen- baum, J., & Rahwan, I. (2018). A computational model of common- sense moral decision making. *Proceedings of the 2018 AAAI/ACM Conference on AI, Ethics, and Society*, 197–2013.


