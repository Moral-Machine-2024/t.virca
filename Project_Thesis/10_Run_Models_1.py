
#################### Run Models 1  ####################
### Test the effect of increasing dataset size on model accuracy

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# %%
# %%
# For computational efficiency when loading the data:
# Define a dictionary specifying the data types for each column
dtypes = {
    'Intervene': 'int16',
    'Male': 'int16',
    'Female': 'int16',
    'Young': 'int16',
    'Old': 'int16',
    'Infancy': 'int16',
    'Pregnancy': 'int16',
    'Fat': 'int16',
    'Fit': 'int16',
    'Working': 'int16',
    'Medical': 'int16',
    'Homelessness': 'int16',
    'Criminality': 'int16',
    'Human': 'int16',
    'Non-human': 'int16',
    'Passenger': 'int16',
    'Law Abiding': 'int16',
    'Law Violating': 'int16',
    'ResponseID': 'category',
    'Intervention': 'int16',
    'PedPed': 'int16',
    'Barrier': 'int16',
    'AttributeLevel': 'category',
    'ScenarioTypeStrict': 'category',
    'NumberOfCharacters': 'int16',
    'DiffNumberOFCharacters': 'int16',
    'Saved': 'int16',
    'UserCountry3': 'category',
    'Man': 'int16',
    'Woman': 'int16',
    'Pregnant': 'int16',
    'Stroller': 'int16',
    'OldMan': 'int16',
    'OldWoman': 'int16',
    'Boy': 'int16',
    'Girl': 'int16',
    'Homeless': 'int16',
    'LargeWoman': 'int16',
    'LargeMan': 'int16',
    'Criminal': 'int16',
    'MaleExecutive': 'int16',
    'FemaleExecutive': 'int16',
    'FemaleAthlete': 'int16',
    'MaleAthlete': 'int16',
    'FemaleDoctor': 'int16',
    'MaleDoctor': 'int16',
    'Dog': 'int16',
    'Cat': 'int16',
    'Cultures': 'category',
    'CrossingSignal_0': 'int16',
    'CrossingSignal_1': 'int16',
    'CrossingSignal_2': 'int16'
}

# Load the df with the specified data types
df_S = pd.read_csv('df_S', dtype=dtypes)
df_M = pd.read_csv('df_M', dtype=dtypes)
df_L = pd.read_csv('df_L', dtype=dtypes)

# %%
print(df_S.info())
print(df_M.info())
print(df_L.info())

# %%
# Select only necessary columns
select_columns = [ 'ResponseID', 'Saved', 'Intervene', 'Male', 'Female', 'Young', 'Old',
                  'Infancy', 'Pregnancy', 'Fat', 'Fit', 'Working', 'Medical', 'Homelessness',
                  'Criminality', 'Human', 'Non-human', 'Passenger', 'Law Abiding','Law Violating',
                  'Cultures']

df_S = df_S[select_columns]
df_M = df_M[select_columns]
df_L = df_L[select_columns]

# %%
#--------------------------- df_S ---------------------------#
# Size = 3.332 rows
############################ Pre-processing
# Split the dataset into training and test sets (80-20)
# Stratify based on culture (maintain proportions of various cultures in the three sets)
train_df, test_df = train_test_split(df_S, test_size=0.2, stratify=df_S['Cultures'], random_state=42)

# Extract target variable 'Saved' and independent variables
y_train_S = train_df['Saved']
X_train_S = train_df.drop(columns=['ResponseID', 'Saved', 'Cultures'])
y_test_S = test_df['Saved']
X_test_S = test_df.drop(columns=['ResponseID', 'Saved', 'Cultures'])

# %%
######################### Random Forests model

# Train the Random Forests model
rf_model_S = RandomForestClassifier(random_state=42)
rf_model_S.fit(X_train_S, y_train_S)

# Predict on the test set
y_test_pred_rf_S = rf_model_S.predict(X_test_S)

# Calculate accuracy
accuracy_rf_S = accuracy_score(y_test_S, y_test_pred_rf_S)
print("Random Forests Model Accuracy for df_S:", accuracy_rf_S)

######################### SVM model

# Train the SVM model
svm_model_S = SVC(random_state=42)
svm_model_S.fit(X_train_S, y_train_S)

# Predict on the test set
y_test_pred_svm_S = svm_model_S.predict(X_test_S)

# Calculate accuracy
accuracy_svm_S = accuracy_score(y_test_S, y_test_pred_svm_S)
print("SVM Model Accuracy for df_S:", accuracy_svm_S)

######################### KNN model

# Train the KNN model
knn_model_S = KNeighborsClassifier()
knn_model_S.fit(X_train_S, y_train_S)

# Predict on the test set
y_test_pred_knn_S = knn_model_S.predict(X_test_S)

# Calculate accuracy
accuracy_knn_S = accuracy_score(y_test_S, y_test_pred_knn_S)
print("KNN Model Accuracy for df_S:", accuracy_knn_S)

# %%
#--------------------------- df_M ---------------------------#
# Size = 33.310 rows

############################ Pre-processing
# Split the dataset into training and test sets (80-20)
# Stratify based on culture (maintain proportions of various cultures in the three sets)
train_df, test_df = train_test_split(df_M, test_size=0.2, stratify=df_M['Cultures'], random_state=42)

# Extract target variable 'Saved' and independent variables
y_train_M = train_df['Saved']
X_train_M = train_df.drop(columns=['ResponseID', 'Saved', 'Cultures'])
y_test_M = test_df['Saved']
X_test_M = test_df.drop(columns=['ResponseID', 'Saved', 'Cultures'])

# %%
######################### Random Forests model

# Train the Random Forests model
rf_model_M = RandomForestClassifier(random_state=42)
rf_model_M.fit(X_train_M, y_train_M)

# Predict on the test set
y_test_pred_rf_M = rf_model_M.predict(X_test_M)

# Calculate accuracy
accuracy_rf_M = accuracy_score(y_test_M, y_test_pred_rf_M)
print("Random Forests Model Accuracy for df_M:", accuracy_rf_M)

######################### SVM model

# Define and train the SVM model
svm_model_M = SVC(random_state=42)
svm_model_M.fit(X_train_M, y_train_M)

# Predict on the test set
y_test_pred_svm_M = svm_model_M.predict(X_test_M)

# Calculate accuracy
accuracy_svm_M = accuracy_score(y_test_M, y_test_pred_svm_M)
print("SVM Model Accuracy for df_M:", accuracy_svm_M)

######################### KNN model

# Train the KNN model
knn_model_M = KNeighborsClassifier()
knn_model_M.fit(X_train_M, y_train_M)

# Predict on the test set
y_test_pred_knn_M = knn_model_M.predict(X_test_M)

# Calculate accuracy
accuracy_knn_M = accuracy_score(y_test_M, y_test_pred_knn_M)
print("KNN Model Accuracy for df_M:", accuracy_knn_M)

# %%
#--------------------------- df_L ---------------------------#
# Size = 333.100 rows

############################ Pre-processing
# Split the dataset into training and test sets (80-20)
# Stratify based on culture (maintain proportions of various cultures in the three sets)
train_df, test_df = train_test_split(df_L, test_size=0.2, stratify=df_L['Cultures'], random_state=42)

# Extract target variable 'Saved' and independent variables
y_train_L = train_df['Saved']
X_train_L = train_df.drop(columns=['ResponseID', 'Saved', 'Cultures'])
y_test_L = test_df['Saved']
X_test_L = test_df.drop(columns=['ResponseID', 'Saved', 'Cultures'])

# %%
######################### Random Forests model

# Train the Random Forests model
rf_model_L = RandomForestClassifier(random_state=42)
rf_model_L.fit(X_train_L, y_train_L)

# Predict on the test set
y_test_pred_rf_L = rf_model_L.predict(X_test_L)

# Calculate accuracy
accuracy_rf_L = accuracy_score(y_test_L, y_test_pred_rf_L)
print("Random Forests Model Accuracy for df_L:", accuracy_rf_L)

######################### SVM model

# Define and train the SVM model
svm_model_L = SVC(random_state=42)
svm_model_L.fit(X_train_L, y_train_L)

# Predict on the test set
y_test_pred_svm_L = svm_model_L.predict(X_test_L)

# Calculate accuracy
accuracy_svm_L = accuracy_score(y_test_L, y_test_pred_svm_L)
print("SVM Model Accuracy for df_L:", accuracy_svm_L)

######################### KNN model

# Train the KNN model
knn_model_L = KNeighborsClassifier()
knn_model_L.fit(X_train_L, y_train_L)

# Predict on the test set
y_test_pred_knn_L = knn_model_L.predict(X_test_L)

# Calculate accuracy
accuracy_knn_L = accuracy_score(y_test_L, y_test_pred_knn_L)
print("KNN Model Accuracy for df_L:", accuracy_knn_L)

# %%
####### Plot graph

# Sample names and sizes
samples = ['Dataset size = (3.332)', 'Dataset size = (33.310)', 'Dataset size = (333.100)']

# Model names
models = ['Random Forests', 'SVM', 'KNN']

# Accuracy values for df_S, df_M, and df_L
accuracy_values = [
    [accuracy_rf_S, accuracy_rf_M, accuracy_rf_L],
    [accuracy_svm_S, accuracy_svm_M, accuracy_svm_L],
    [accuracy_knn_S, accuracy_knn_M, accuracy_knn_L]
]

# Plot figure
plt.figure(figsize=(10, 6))

# Plot for each model
plt.plot(samples, accuracy_values[0], marker='o', label='Random Forests')
plt.plot(samples, accuracy_values[1], marker='o', label='SVM')
plt.plot(samples, accuracy_values[2], marker='o', label='KNN')

# Add labels and title
plt.title('Model Accuracy for Different Dataset Sizes', fontsize=20, pad=20)
plt.xlabel('Sample', fontsize=16)
plt.ylabel('Accuracy', fontsize=16)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.legend(fontsize=14)

# Display the plot
plt.show()
