# The Moral Machine Experiment: Predicting Moral Decision-Making Based on Personal Values
This repository contains code and instructions to replicate the thesis project *"The Moral Machine Experiment: Predicting Moral Decision-Making Based on Personal Values"* conducted for the partial fulfilment of the MSc Data Science & Society at Tilburg University. 

The abstract of the thesis reads as follows:

*"This research employs the dataset of the Moral Machine Experiment by Awad et al. (2018) to investigate the influence of personal values on decisions within the context of autonomous vehicle moral dilemmas. Unlike previous works, which primarily focus on culturally homogeneous groups, this study examines responses within a culturally diverse sample. This makes it possible to isolate personal values from cultural values when predicting moral decisions, as this separation is fundamental according to value scholars (Hofstede, 1984; Schwartz, 2006). Building on the computational model for extracting abstract features devised by Kim et al. (2018), this research investigates the predictive performance of Random Forest, Support Vector Machine, and K-Nearest Neighbors, alongside a dummy classifier, as their potential in relation to the MME remains understudied. The findings suggest that all three models are able to identify patterns in the relationship between personal values and moral decisions, in particular considering factors such as species, legality and age. Moreover, predictive performance improves with increased sample size and in culturally homogeneous samples. This last finding suggests that when studying culturally homogeneous groups, predictions should be understood as the product of both personal and cultural values. This thesis contributes to existing research on values and moral decision-making, as well as to the data science domain."*

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

### 3_Data_Cleaning
The following operations are performed on each of the extracted samples:
1. Check whether there are duplicated rows
2. Delete unneccessary columns
3. Rename column for clarity
4. Delete rows with missing values
5. Delete incomplete scenarios (two rows form a scenario)
6. Export cleaned sample to csv

### 4_Create_Final_Dataframe
Two functions are created:

**create_sub_sample**: takes a dataframe as input and creates a sub-sample amounting to a specified proportion of the original sample. StratifiedShuffleSplit from the scikit-learn library is used to perform stratified sampling based on country. Additionally, the function makes sure to include both sides of a scenario when selecting the indices of the selected rows. 

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

- The two functions are applied to each continent sample to halve their sizes (proportion = 0.5) and compare the proportions. 
- Finally, the halved sub-samples are merged into a new dataframe and exported to csv. The number of rows in the merged dataframe is 33.309.960, which means that 16.654.980 scenarios are inlcuded. 

### 5_Latent_Feature_Space
- A binary matrix is created to visually represent the latent feature space as presented in the paper *"A computational model of commonsense moral decision making"* by Kim et al. (2018). 

### 6_Feature_Engineering
- The binary matrix used to visualize the latent feature space is here modified to accomodate the feature engineering process. The abstarct features 'Passenger', 'Law Abiding', 'Law Violating' are removed, as in the following steps they are not computed in relation to the matrix.
- A function is defined to perform feature engineering on the merged dataframe:

*calculate_abstract_features*: the function takes as argument two dataframes, the merged dataframe and the binary matrix. It calculates abstract feature counts based on the information contained in both dataframes, and returns the merged dataframe with 18 additional columns corresponding to the 18 abstract features.
- The function is applied to the merged dataframe and the outcome is exported to csv. This represents the final dataset to be used for the project. 

### 7_Sanity_Check
- 10 random rows are generate for each abstract feature and other relevant columns used to compute their respective counts. By running the code multiple times on randomly sampled rows it is possible to verify that the computed values of the abstract features are correct.

### 8_Visualize_Distributions
- A bar plot is used to visualize the distribution of the target variable. This confirms that the dataset does not suffer from class imbalance.
- A bar plot is used to visualize the distribution of users across cultures. That is, how many unique users belong to each culture.
- A bar plot per country is not created since it would contain 106 bars. However, the value counts suggest that the United States, Germany and Brazil are the most represented countries.

### 9_Create_Sub-samples
The functions **create_sub_sample** and **verify_proportions** are called in this file to create further sub-samples to be used for modeling. 
- **create_sub_sample** is used three times with the proportion argument set to 0.0001, 0.001 and 0.01, thus creating three sub-samples (df_S, df_M and df_L) with 3.332, 33.310 and 333.100 rows respectively.
- Three further sub-samples are made by extracting responses from the Netherlands, Japan and Singapore.

### 10_Modeling_1
A simple instance of Random Forests, SVM and KNN is created and fit on three samples of increasing size (df_S, df_M and df_L), using an 80-20 training-test split. The accuracy values obtained are then plotted to visualize the effect of increasing dataset size on model accuracy for all three models. 

### 11_Modeling_2
- The function *plot_confusion_matrix* is defined, which produces a confusion matrix indicating both count and percentage in each cell.
- The sub-sample df_S, containing 333.100 rows, is used to train a dummy classifier, a Random Forest Classifier, an SVM classifier, and a KNN classifier, with a 60-20-20 training-validation-test split.
- The hyperparameters of the three latter models are tuned using RandomizedSearchCV from the Scikit-learn library, and the best models are saved.
- The *plot_confusion_matrix* function is used to produce confusion matrices heatmaps for each model.
- ROC and AUC are computed and plotted for each model.
- The following metrics are computed for each model: Accuracy, Precision, Recall, F1-Score and Specificity. A dataframe containing the metrics for each model is created.
- Finally, permutation feature importance is performed using the best SVM model, and the permutation importance score of each feature is visualized with a barplot.

### 12_Modeling_3
- The three country samples (the Netherlands, Japan, Singapore) previously created are split into a training (80%) and test (20%) set.
- The SVM model is trained on the three samples using the best hyperparameters found previously.
- The *plot_confusion_matrix* function is used to produce confusion matrices for each sample.
- The following metrics are computed for each sample: Accuracy, Precision, Recall, F1-Score and Specificity. 

## References
Awad, E., Dsouza, S., Kim, R., Henrich, J., Shariff, A., Bonnefon, J.-F., & Rahwan, I. (2018). The moral machine experiment. *Nature*, *563*(7729), 59–64.

Kim, R., Kleiman-Weiner, M., Abeliuk, A., Awad, E., Dsouza, S., Tenen- baum, J., & Rahwan, I. (2018). A computational model of common- sense moral decision making. *Proceedings of the 2018 AAAI/ACM Conference on AI, Ethics, and Society*, 197–2013.


