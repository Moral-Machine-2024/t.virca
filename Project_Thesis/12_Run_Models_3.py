
#################### Run models 3 ####################
### Country Samples / culturally homogeneous samples

# Import necessary libraries and previously defined functions
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from Run_Models_2 import plot_confusion_matrix

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

# %%
nld = pd.read_csv('Netherlands_sample_sub.csv', dtype=dtypes)
jpn = pd.read_csv('Japan_sample_sub.csv', dtype=dtypes)
sgp = pd.read_csv('Singapore_sample_sub.csv', dtype=dtypes)

# %%
print(nld.info())
print(jpn.info())
print(sgp.info())

# %%
# Select only necessary columns
select_columns = ['ResponseID', 'Saved', 'Intervene', 'Male', 'Female', 'Young', 'Old',
                  'Infancy', 'Pregnancy', 'Fat', 'Fit', 'Working', 'Medical', 'Homelessness',
                  'Criminality', 'Human', 'Non-human', 'Passenger', 'Law Abiding', 'Law Violating',
                  'Cultures']

nld = nld[select_columns]
jpn = jpn[select_columns]
sgp = sgp[select_columns]

# %%
#### Use best SVM model to train and make predictions in the three country samples

####################### Pre-processing
### The Netherlands
# Separate features and target variable
X_nld = nld.drop(columns=['ResponseID', 'Saved', 'Cultures'])
y_nld = nld['Saved']

# Split into training and testing sets
X_train_nld, X_test_nld, y_train_nld, y_test_nld = train_test_split(X_nld, y_nld, test_size=0.2, random_state=42)

### Japan
# Separate features and target variable
X_jpn = jpn.drop(columns=['ResponseID', 'Saved', 'Cultures'])
y_jpn = jpn['Saved']

# Split into training and testing sets
X_train_jpn, X_test_jpn, y_train_jpn, y_test_jpn = train_test_split(X_jpn, y_jpn, test_size=0.2, random_state=42)

### Singapore
# Separate features and target variable
X_sgp = sgp.drop(columns=['ResponseID', 'Saved', 'Cultures'])
y_sgp = sgp['Saved']

# Split into training and testing sets
X_train_sgp, X_test_sgp, y_train_sgp, y_test_sgp = train_test_split(X_sgp, y_sgp, test_size=0.2, random_state=42)


####################### Netherlands - Train and make predictions
# Initialize SVM classifier with tuned parameters
svm_clf_nld = SVC(kernel='rbf', gamma='auto', C=10)

# Train the model
svm_clf_nld.fit(X_train_nld, y_train_nld)

# Make predictions on the test set
y_test_pred_svm_nld = svm_clf_nld.predict(X_test_nld)

# Calculate metrics
accuracy_svm_nld = accuracy_score(y_test_nld, y_test_pred_svm_nld)
precision_svm_nld = precision_score(y_test_nld, y_test_pred_svm_nld, average='macro')
recall_svm_nld = recall_score(y_test_nld, y_test_pred_svm_nld, average='macro')
f1_svm_nld = f1_score(y_test_nld, y_test_pred_svm_nld, average='macro')

# Calculate specificity
tn_svm_nld, fp_svm_nld, fn_svm_nld, tp_svm_nld = confusion_matrix(y_test_nld, y_test_pred_svm_nld).ravel()
specificity_svm_nld = tn_svm_nld / (tn_svm_nld + fp_svm_nld)

# Print evaluation metrics
print("Accuracy (Netherlands SVM):", accuracy_svm_nld)
print("Precision (Netherlands SVM):", precision_svm_nld)
print("Recall (Netherlands SVM):", recall_svm_nld)
print("F1 Score (Netherlands SVM):", f1_svm_nld)
print("Specificity (Netherlands SVM):", specificity_svm_nld)

# Plot confusion matrix
plot_confusion_matrix(y_test_nld, y_test_pred_svm_nld, labels=[0, 1], title="Confusion Matrix - Netherlands (SVM)")

# %%
####################### Japan - Train and make predictions
# Initialize the SVM classifier with tuned parameters
svm_clf_jpn = SVC(kernel='rbf', gamma='auto', C=10)

# Train the model
svm_clf_jpn.fit(X_train_jpn, y_train_jpn)

# Make predictions on the test set
y_test_pred_svm_jpn = svm_clf_jpn.predict(X_test_jpn)

# Calculate metrics
accuracy_svm_jpn = accuracy_score(y_test_jpn, y_test_pred_svm_jpn)
precision_svm_jpn = precision_score(y_test_jpn, y_test_pred_svm_jpn, average='macro')
recall_svm_jpn = recall_score(y_test_jpn, y_test_pred_svm_jpn, average='macro')
f1_svm_jpn = f1_score(y_test_jpn, y_test_pred_svm_jpn, average='macro')

# Calculate specificity
tn_svm_jpn, fp_svm_jpn, fn_svm_jpn, tp_svm_jpn = confusion_matrix(y_test_jpn, y_test_pred_svm_jpn).ravel()
specificity_svm_jpn = tn_svm_jpn / (tn_svm_jpn + fp_svm_jpn)

# Print evaluation metrics
print("Accuracy:", accuracy_svm_jpn)
print("Precision:", precision_svm_jpn)
print("Recall:", recall_svm_jpn)
print("F1 Score:", f1_svm_jpn)
print("Specificity:", specificity_svm_jpn)

# Plot confusion matrix
plot_confusion_matrix(y_test_jpn, y_test_pred_svm_jpn, labels=[0, 1], title="Confusion Matrix - Japan (SVM)")

####################### Singapore - Train and make predictions
# Initialize the SVM classifier with tuned parameters
svm_clf_sgp = SVC(kernel='rbf', gamma='auto', C=10)

# Train the model
svm_clf_sgp.fit(X_train_sgp, y_train_sgp)

# Make predictions on the test set
y_test_pred_svm_sgp = svm_clf_sgp.predict(X_test_sgp)

# Calculate metrics
accuracy_svm_sgp = accuracy_score(y_test_sgp, y_test_pred_svm_sgp)
precision_svm_sgp = precision_score(y_test_sgp, y_test_pred_svm_sgp, average='macro')
recall_svm_sgp = recall_score(y_test_sgp, y_test_pred_svm_sgp, average='macro')
f1_svm_sgp = f1_score(y_test_sgp, y_test_pred_svm_sgp, average='macro')

# Calculate specificity
tn_svm_sgp, fp_svm_sgp, fn_svm_sgp, tp_svm_sgp = confusion_matrix(y_test_sgp, y_test_pred_svm_sgp).ravel()
specificity_svm_sgp = tn_svm_sgp / (tn_svm_sgp + fp_svm_sgp)

# Print evaluation metrics
print("Accuracy:", accuracy_svm_sgp)
print("Precision:", precision_svm_sgp)
print("Recall:", recall_svm_sgp)
print("F1 Score:", f1_svm_sgp)
print("Specificity:", specificity_svm_sgp)

# Plot confusion matrix
plot_confusion_matrix(y_test_sgp, y_test_pred_svm_sgp, labels=[0, 1], title="Confusion Matrix - Singapore (SVM)")
