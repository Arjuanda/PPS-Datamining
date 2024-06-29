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