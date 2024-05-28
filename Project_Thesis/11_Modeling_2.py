
#################### Run models 2 ####################
### Run models and tune hyperparameters

# %%
# Import necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.dummy import DummyClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold, cross_val_score
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_curve, auc
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.inspection import permutation_importance
import joblib

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
df = pd.read_csv('df_S', dtype=dtypes)

# %%
# Select only necessary columns
select_columns = ['ResponseID', 'Saved', 'Intervene', 'Male', 'Female', 'Young', 'Old',
                  'Infancy', 'Pregnancy', 'Fat', 'Fit', 'Working', 'Medical', 'Homelessness',
                  'Criminality', 'Human', 'Non-human', 'Passenger', 'Law Abiding', 'Law Violating',
                  'Cultures']

df = df[select_columns]

# %%
# Define function to plot confusion matrix with count and percentage in each square
def plot_confusion_matrix(y_true, y_pred, labels=None, title=" "):
    """
    Arguments:
    - y_true: true labels
    - y_pred: predicted labels
    - labels: list of class labels to use in the confusion matrix
    - title: title for the plot

    Returns:
    Confusion matrix plot
    """

    # Calculate the confusion matrix
    cm = confusion_matrix(y_true, y_pred, labels=labels)

    # Calculate the total number of observations
    n_total = cm.sum()

    # Calculate the percentage for each cell in the confusion matrix
    cm_percentage = cm / n_total * 100

    # Create heatmap with seaborn
    plt.figure(figsize=(8, 6))

    # Define function that includes count and percentage in each square
    def custom_annotation(data, **kwargs):
        annotation = []
        for i in range(data.shape[0]):
            row_annotation = []
            for j in range(data.shape[1]):
                count = data[i, j]
                percentage = cm_percentage[i, j]
                formatted_annotation = f"{count}\n({percentage:.2f}%)"
                row_annotation.append(formatted_annotation)
            annotation.append(row_annotation)
        return np.array(annotation)

    # Plot the heatmap and use custom_annotation function
    sns.heatmap(cm, annot=custom_annotation(cm), fmt="", cmap="Blues", cbar=True, square=True,
                xticklabels=labels, yticklabels=labels)

    # Add labels and title
    plt.xlabel('Predicted Labels')
    plt.ylabel('True Labels')
    plt.title(title)

    # Show plot
    plt.show()

# %%
# --------------------------- df ---------------------------#
# Size = 333.100 rows

############################ Pre-processing ############################
# Split the dataset into training, validation, and test sets
# Ratio: 60% training, 20% validation, 20% testing
# Stratify based on culture (maintain proportions of various cultures in the three sets)
train_df, temp_df = train_test_split(df, test_size=0.4, stratify=df['Cultures'], random_state=42)
val_df, test_df = train_test_split(temp_df, test_size=0.5, stratify=temp_df['Cultures'], random_state=42)

# Extract target variable 'Saved' and independent variables
y_train = train_df['Saved']
X_train = train_df.drop(columns=['ResponseID', 'Saved', 'Cultures'])
y_val = val_df['Saved']
X_val = val_df.drop(columns=['ResponseID', 'Saved', 'Cultures'])
y_test = test_df['Saved']
X_test = test_df.drop(columns=['ResponseID', 'Saved', 'Cultures'])

# Verify shapes
print('y_train shape: ', y_train.shape)
print('X_train shape: ', X_train.shape)
print('y_val shape: ', y_val.shape)
print('X_val shape: ', X_val.shape)
print('y_test shape: ', y_test.shape)
print('X_test shape: ', X_test.shape)

"""
y_train shape:  (199860,)
X_train shape:  (199860, 18)
y_val shape:  (66620,)
X_val shape:  (66620, 18)
y_test shape:  (66620,)
X_test shape:  (66620, 18)
"""

# %%
############################ Dummy Classifier ############################

# Initialize DummyClassifier - use "uniform" strategy
dummy_clf_uniform = DummyClassifier(strategy="uniform")

# Fit DummyClassifier on training data
dummy_clf_uniform.fit(X_train, y_train)

# Make predictions on validation and test sets
y_val_pred_uniform = dummy_clf_uniform.predict(X_val)
y_test_pred_uniform = dummy_clf_uniform.predict(X_test)

# Calculate accuracy on validation and test sets
val_accuracy_uniform = accuracy_score(y_val, y_val_pred_uniform)
test_accuracy_uniform = accuracy_score(y_test, y_test_pred_uniform)

print(f"Uniform Dummy Classifier - Validation set accuracy: {val_accuracy_uniform}")
print(f"Uniform Dummy Classifier - Test set accuracy: {test_accuracy_uniform}")

# %%
# Confusion matrix - Dummy classifier
# Predict labels for validation and test sets using the dummy classifier
y_val_pred_uniform = dummy_clf_uniform.predict(X_val)
y_test_pred_uniform = dummy_clf_uniform.predict(X_test)

# Plot confusion matrix
print("Dummy Classifier - Validation Set")
plot_confusion_matrix(y_val, y_val_pred_uniform, labels=[0, 1], title='Dummy Classifier - Validation Set')
print("Dummy Classifier - Test Set")
plot_confusion_matrix(y_test, y_test_pred_uniform, labels=[0, 1], title='Dummy Classifier - Test Set')

"""
Uniform Dummy Classifier - Validation set accuracy: 0.5007955568898229
Uniform Dummy Classifier - Test set accuracy: 0.49992494746322425
"""

# %%
############################ Random Forests (RF) ############################

# Instantiate Random Forest classifier
rf_clf = RandomForestClassifier(random_state=42)

# K-fold cross-validation on the training set
kf = KFold(n_splits=5, shuffle=True, random_state=42)
cv_scores_rf = cross_val_score(rf_clf, X_train, y_train, cv=kf)

# Calculate average CV score
average_cv_score_rf = np.mean(cv_scores_rf)

print("RF Cross-validation scores:", cv_scores_rf)
print("Average CV score (RF):", average_cv_score_rf)

"""
RF Cross-validation scores: [0.64712799 0.65063044 0.65275693 0.64955469 0.65045532]
Average CV score (RF): 0.650105073551486
"""

# %%
# Hyperparameter tuning using RandomizedSearchCV

param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'max_features': ['auto', 'log2']
}

# Instantiate RandomizedSearchCV
random_search_RF = RandomizedSearchCV(rf_clf, param_grid, cv=3, scoring='accuracy', random_state=42)

# Fit RandomizedSearchCV on the training data
random_search_RF.fit(X_train, y_train)

# Find best model and hyperparameters
best_rf_clf = random_search_RF.best_estimator_
print("Best hyperparameters:", random_search_RF.best_params_)

# Save the best model
joblib.dump(best_rf_clf, 'best_rf_model.joblib')

# Evaluate the best model on the validation set
y_val_pred = best_rf_clf.predict(X_val)
val_accuracy = accuracy_score(y_val, y_val_pred)
print("Validation accuracy of best model:", val_accuracy)

# Evaluate the best model on the test set
y_test_pred = best_rf_clf.predict(X_test)
test_accuracy = accuracy_score(y_test, y_test_pred)
print("Test accuracy of best model:", test_accuracy)

"""
Best hyperparameters: {'n_estimators': 200, 'min_samples_split': 2, 'min_samples_leaf': 4, 'max_features': 'log2', 'max_depth': 10}
Validation accuracy of best model: 0.667982587811468
Test accuracy of best model: 0.6648153707595317
"""

# %%
# Predict labels using the best random forest classifier
y_val_pred_rf_best = best_rf_clf.predict(X_val)
y_test_pred_rf_best = best_rf_clf.predict(X_test)

# Plot confusion matrix
print("Random Forests (Best Model) - Validation Set")
plot_confusion_matrix(y_val, y_val_pred_rf_best, labels=[0, 1], title='Random Forests (Best Model) - Validation Set')

print("Random Forests (Best Model) - Test Set")
plot_confusion_matrix(y_test, y_test_pred_rf_best, labels=[0, 1], title='Random Forests (Best Model) - Test Set')

# %%
############################ Support Vector Machines (SVM) ############################

# Instantiate SVM classifier
svm_clf = SVC(random_state=42)

# K-fold cross-validation on the training set
cv_scores_svm = cross_val_score(svm_clf, X_train, y_train, cv=kf)

# Calculate average CV score
average_cv_score_svm = np.mean(cv_scores_svm)

print("SVM Cross-validation scores:", cv_scores_svm)
print("Average CV score (SVM):", average_cv_score_svm)

# %%
## Tune hyperparameters SVM

param_dist = {
    'C': [0.01, 0.1, 1, 10, 100],
    'gamma': ['scale', 'auto', 0.01, 0.1, 1, 10, 100],
    'kernel': ['linear', 'rbf']
}

# Instantiate RandomizedSearchCV
random_search_SVM = RandomizedSearchCV(svm_clf, param_distributions=param_dist, n_iter=20, cv=5, random_state=42)

# Fit RandomizedSearchCV on the training data
random_search_SVM.fit(X_train, y_train)

# Find the best model and hyperparameters
best_svm = random_search_SVM.best_estimator_

# Save the best model
joblib.dump(best_svm, 'best_svm_model.joblib')

print("Best parameters:", random_search_SVM.best_params_)
print("Best validation accuracy:", random_search_SVM.best_score_)

# Evaluate the best model on the test set
y_test_pred = best_svm.predict(X_test)
test_accuracy = accuracy_score(y_test, y_test_pred)
print("Test set accuracy of best model:", test_accuracy)

# Evaluate the best model on the validation set
y_val_pred = best_svm.predict(X_val)
val_accuracy = accuracy_score(y_val, y_val_pred)
print("Validation set accuracy of best model:", val_accuracy)

"""
Best parameters: {'kernel': 'rbf', 'gamma': 'auto', 'C': 10}
Best validation accuracy: 0.6701290903632542
Test set accuracy: 0.6684028820174122
Validation set accuracy: 0.6722005403782648
"""

# %%
# Confusion Matrix - SVM
# Predict labels using the best SVM classifier
y_val_pred_svm_best = best_svm.predict(X_val)
y_test_pred_svm_best = best_svm.predict(X_test)

# Plot confusion matrix
print("SVM (Best Model) - Validation Set")
plot_confusion_matrix(y_val, y_val_pred_svm_best, labels=[0, 1], title='SVM (Best Model) - Validation Set')

print("SVM (Best Model) - Test Set")
plot_confusion_matrix(y_test, y_test_pred_svm_best, labels=[0, 1], title='SVM (Best Model) - Test Set')

# %%
############################ k-Nearest Neighbors (KNN) ############################
# Instantiate KNN classifier
knn_clf = KNeighborsClassifier()

# K-fold cross-validation on the training set
cv_scores_knn = cross_val_score(knn_clf, X_train, y_train, cv=kf)

# Calculate average CV score
average_cv_score_knn = np.mean(cv_scores_knn)

print("KNN Cross-validation scores:", cv_scores_knn)
print("Average CV score (KNN):", average_cv_score_knn)

"""
KNN Cross-validation scores: [0.61913339 0.62773942 0.6272891  0.62683879 0.62921545]
Average CV score (KNN): 0.6260432302611829
"""

# %%
## Tune Hyperparameters KNN

param_dist_knn = {
    'n_neighbors': list(range(1, 31)),  # Number of neighbors to test
    'metric': ['euclidean', 'manhattan', 'minkowski'],  # Distance metric
    'weights': ['uniform', 'distance']  # Weighting of neighbors
}

# Instantiate RandomizedSearchCV
random_search_KNN = RandomizedSearchCV(knn_clf, param_distributions=param_dist_knn, n_iter=20, cv=5, random_state=42)

# Fit RandomizedSearchCV on the training data
random_search_KNN.fit(X_train, y_train)

# Find the best model and hyperparameters
best_knn_model = random_search_KNN.best_estimator_
best_knn_params = random_search_KNN.best_params_

print("Best parameters:", random_search_KNN.best_params_)

# Save the best KNN model
joblib.dump(best_knn_model, 'best_knn_model.joblib')

# Evaluate the best model on validation and test sets
val_accuracy_knn = best_knn_model.score(X_val, y_val)
print(f"Best KNN model - Validation set accuracy: {val_accuracy_knn}")

test_accuracy_knn = best_knn_model.score(X_test, y_test)
print(f"Best KNN model - Test set accuracy: {test_accuracy_knn}")

"""
Best parameters: {'weights': 'uniform', 'n_neighbors': 29, 'metric': 'euclidean'}
Best KNN model - Validation set accuracy: 0.658180726508556
Best KNN model - Test set accuracy: 0.6587361152806965
"""

# %%
# Confusion Matrix - KNN
# Predict labels using the best KNN classifier
y_val_pred_knn_best = best_knn_model.predict(X_val)
y_test_pred_knn_best = best_knn_model.predict(X_test)

# Plot confusion matrix
print("KNN (Best Model) - Validation Set")
plot_confusion_matrix(y_val, y_val_pred_knn_best, labels=[0, 1], title='KNN (Best Model) - Validation Set')

print("KNN (Best Model) - Test Set")
plot_confusion_matrix(y_test, y_test_pred_knn_best, labels=[0, 1], title='KNN (Best Model) - Test Set')

# %%
### Compute ROC curve and AUC for each model

# Dummy Classifier
dummy_probs = dummy_clf_uniform.predict_proba(X_test)[:, 1] # probabilities
fpr_dummy, tpr_dummy, _ = roc_curve(y_test, dummy_probs)
auc_dummy = auc(fpr_dummy, tpr_dummy)

# Random Forests
rf_probs = best_rf_clf.predict_proba(X_test)[:, 1] # probabilities
fpr_rf, tpr_rf, _ = roc_curve(y_test, rf_probs)
auc_rf = auc(fpr_rf, tpr_rf)

# SVM
svm_decision_function = best_svm.decision_function(X_test) # decision function!
fpr_svm, tpr_svm, _ = roc_curve(y_test, svm_decision_function)
auc_svm = auc(fpr_svm, tpr_svm)

# KNN
knn_probs = best_knn_model.predict_proba(X_test)[:, 1] # probabilities
fpr_knn, tpr_knn, _ = roc_curve(y_test, knn_probs)
auc_knn = auc(fpr_knn, tpr_knn)

# Plot ROC curve
plt.figure(figsize=(8, 6))
plt.plot(fpr_dummy, tpr_dummy, color='blue', linestyle='--', label=f'Dummy Classifier (AUC = {auc_dummy:.2f})')
plt.plot(fpr_rf, tpr_rf, color='green', label=f'Random Forests (AUC = {auc_rf:.2f})')
plt.plot(fpr_svm, tpr_svm, color='red', label=f'SVM (AUC = {auc_svm:.2f})')
plt.plot(fpr_knn, tpr_knn, color='orange', label=f'KNN (AUC = {auc_knn:.2f})')
plt.plot([0, 1], [0, 1], color='black', linestyle=':', label='Chance line')

plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend()
plt.grid(True)

plt.show()

# %%
# Compute metrics
# Dictionary to store the metrics for each model
metrics_dict = {
    'Model': [],
    'Accuracy': [],
    'Precision': [],
    'Recall': [],
    'F1-Score': [],
    'Specificity': [],
}

# Define a function to calculate specificity
def calculate_specificity(y_true, y_pred):
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
    return tn / (tn + fp)

# Dummy Classifier metrics
metrics_dict['Model'].append('Dummy Classifier')
metrics_dict['Accuracy'].append(accuracy_score(y_test, y_test_pred_uniform))
metrics_dict['Precision'].append(precision_score(y_test, y_test_pred_uniform))
metrics_dict['Recall'].append(recall_score(y_test, y_test_pred_uniform))
metrics_dict['F1-Score'].append(f1_score(y_test, y_test_pred_uniform))
metrics_dict['Specificity'].append(calculate_specificity(y_test, y_test_pred_uniform))

# Random Forests metrics
metrics_dict['Model'].append('Random Forests')
metrics_dict['Accuracy'].append(accuracy_score(y_test, y_test_pred_rf_best))
metrics_dict['Precision'].append(precision_score(y_test, y_test_pred_rf_best))
metrics_dict['Recall'].append(recall_score(y_test, y_test_pred_rf_best))
metrics_dict['F1-Score'].append(f1_score(y_test, y_test_pred_rf_best))
metrics_dict['Specificity'].append(calculate_specificity(y_test, y_test_pred_rf_best))

# SVM metrics
metrics_dict['Model'].append('SVM')
metrics_dict['Accuracy'].append(accuracy_score(y_test, y_test_pred_svm_best))
metrics_dict['Precision'].append(precision_score(y_test, y_test_pred_svm_best))
metrics_dict['Recall'].append(recall_score(y_test, y_test_pred_svm_best))
metrics_dict['F1-Score'].append(f1_score(y_test, y_test_pred_svm_best))
metrics_dict['Specificity'].append(calculate_specificity(y_test, y_test_pred_svm_best))

# KNN metrics
metrics_dict['Model'].append('KNN')
metrics_dict['Accuracy'].append(accuracy_score(y_test, y_test_pred_knn_best))
metrics_dict['Precision'].append(precision_score(y_test, y_test_pred_knn_best))
metrics_dict['Recall'].append(recall_score(y_test, y_test_pred_knn_best))
metrics_dict['F1-Score'].append(f1_score(y_test, y_test_pred_knn_best))
metrics_dict['Specificity'].append(calculate_specificity(y_test, y_test_pred_knn_best))

# Convert dictionary into a DataFrame
metrics_df = pd.DataFrame(metrics_dict)
print(metrics_df)

# %%
################## Permutation feature importance with best SVM model ##################
# Compute permutation importance for each feature
perm_importance = permutation_importance(best_svm, X_val, y_val, n_repeats=10, random_state=42)
feature_importance = perm_importance.importances_mean

# Feature names
feature_names = X_val.columns

# Create a df with feature importance values
importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': feature_importance})
importance_df = importance_df.sort_values(by='Importance', ascending=False)
print(importance_df)

# %%
# Plot results permutation feature importance
plt.figure(figsize=(12, 8))
sns.barplot(x='Importance', y='Feature', data=importance_df, palette='viridis')
plt.xlabel('Mean Decrease in Accuracy', fontsize=18)
plt.ylabel('Features', fontsize=18)
plt.yticks(fontsize=16)
plt.xticks(fontsize=16)
plt.tight_layout()
plt.show()

