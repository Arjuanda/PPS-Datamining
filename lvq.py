import numpy as np 
import pandas as pd 
from sklearn.preprocessing import LabelEncoder 
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
import os
for dirname, _, filenames in os.walk('/PPS-Datamining/static'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

df = pd.read_csv("static/nilai-dataset/nilai.csv", encoding='ISO-8859-1')
df.head()
# get the number of missing data points per column
missing_values_count = df.isnull().sum()
missing_values_count
# how many total missing values do we have?
total_cells = np.prod(df.shape)
total_missing = missing_values_count.sum()

# percent of data that is missing
(total_missing/total_cells) * 100
df.describe()
df.info()
df.shape
df.dtypes
df = df.rename(columns={'X1': 'Matematika', 'X2': 'BahasaIndonesia', 'X3': 'BahasaInggris', 'X4': 'Fisika', 'X5': 'Kimia', 'X6': 'Biologi', 'X7': 'Ekonomi', 'X8': 'Geografi', 'X9': 'Sosiologi', 'X10': 'Sejarah'})

df
test_data = df[df['Target'].isna()]
test_data = test_data.drop(columns=['No', 'Nama', 'Target'])

test_data

df.dropna(subset=['Target'], inplace=True)
df.Target=df.Target.astype('category').cat.codes
df['Target'] = df['Target'].replace(0, 99)

df

df['Target'].unique()
dfs = {}
for target in df['Target'].unique():
    dfs[target] = df[df['Target'] == target]

# Accessing each dataframe
for target, df_target in dfs.items():
    print(f"Dataframe for Target {target}:")
    print(df_target)
    print("\n")

# Splitting the dataframe based on the "Target" column
dfs = {}
for target in df['Target'].unique():
    dfs[f"df_target_{target}"] = df[df['Target'] == target]

# Assign each dataframe to a variable and extract features and targets
for key, df_target in dfs.items():
    exec(f"{key} = df_target")
    exec(f"X_{key} = {key}.drop(columns=['No', 'Nama', 'Target'])")
    exec(f"y_{key} = {key}['Target']")

# Print all feature and target dataframe names
for key in dfs.keys():
    print(f"Features for {key}: X_{key}")
    print(f"Target for {key}: y_{key}")

# Perform train_test_split and convert to numpy arrays
for key in dfs.keys():
    X = eval(f"X_{key}")
    y = eval(f"y_{key}")

    if len(X) > 1:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        exec(f"X_train_{key} = X_train.to_numpy()")
        exec(f"y_train_{key} = y_train.to_numpy()")
        exec(f"X_test_{key} = X_test.to_numpy()")
        exec(f"y_test_{key} = y_test.to_numpy()")
    else:
        exec(f"X_train_{key} = X.to_numpy()")
        exec(f"y_train_{key} = y.to_numpy()")
        exec(f"X_test_{key} = np.array([])")
        exec(f"y_test_{key} = np.array([])")

# Print the results
for key in dfs.keys():
    print(f"Training features for {key}: X_train_{key}")
    print(f"Training target for {key}: y_train_{key}")
    print(f"Testing features for {key}: X_test_{key}")
    print(f"Testing target for {key}: y_test_{key}")

## sklearn & lvq & preprocess & train & eval
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

## basic
import numpy as np
import pandas as pd

## sklearn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.feature_selection import SelectPercentile, chi2
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

## LVQ
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.utils.validation import check_X_y, check_array, check_is_fitted
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report

class LVQClassifier(BaseEstimator, ClassifierMixin):
    def __init__(self, learning_rate=0.0001, epochs=500, prototype_per_class=1):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.prototype_per_class = prototype_per_class

    def fit(self, X, y):
        X, y = check_X_y(X, y)
        self.prototype_labels, self.prototypes = self.initialize_prototypes(X, y)
        for epoch in range(self.epochs):
            for i, x in enumerate(X):
                closest_prototype_index = self.find_closest_prototype_index(x)
                if y[i] == self.prototype_labels[closest_prototype_index]:
                    self.prototypes[closest_prototype_index] += self.learning_rate * (x - self.prototypes[closest_prototype_index])
                else:
                    self.prototypes[closest_prototype_index] -= self.learning_rate * (x - self.prototypes[closest_prototype_index])
        self.is_fitted_ = True
        return self

    def predict(self, X):
        check_is_fitted(self)
        X = check_array(X)
        y_pred = []
        for x in X:
            closest_prototype_index = self.find_closest_prototype_index(x)
            y_pred.append(self.prototype_labels[closest_prototype_index])
        return np.array(y_pred)

    def initialize_prototypes(self, X, y):
        prototype_labels = np.unique(y)
        prototypes = []
        for label in prototype_labels:
            label_indices = np.where(y == label)[0]
            np.random.shuffle(label_indices)
            label_indices = label_indices[:self.prototype_per_class]
            prototypes.extend(X[label_indices])
        return prototype_labels, np.array(prototypes)

    def find_closest_prototype_index(self, x):
        distances = np.linalg.norm(self.prototypes - x, axis=1)
        return np.argmin(distances)
    
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('lvq', LVQClassifier())
])

pipeline

# Iterate through the target-based dataframes
import pickle
import joblib

for key in dfs.keys():
    X_train = eval(f"X_train_{key}")
    y_train = eval(f"y_train_{key}")
    X_test = eval(f"X_test_{key}")
    y_test = eval(f"y_test_{key}")

    # Check if test set is empty
    if len(X_test) == 0:
        print(f"\nSkipping training and testing for {key} as test set is empty.\n")
        continue

    # Fit the pipeline
    pipeline.fit(X_train, y_train)

    # Predict
    y_pred = pipeline.predict(X_test)

    # Print the classification report
    print(f"Classification Report for {key}:")
    print(classification_report(y_test, y_pred))

    # Define the filename for saving the model
    filename_pickle = f"model_{key}_pickle.pkl"
    filename_joblib = f"model_{key}_joblib.joblib"

    # Save the model using pickle
    with open(filename_pickle, 'wb') as f:
        pickle.dump(pipeline, f)
    print(f"Model for {key} saved using pickle to {filename_pickle}")

    # Save the model using joblib
    joblib.dump(pipeline, filename_joblib)
    print(f"Model for {key} saved using joblib to {filename_joblib}")