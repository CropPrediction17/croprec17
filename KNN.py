import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("Crop_recommendation.csv")

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
y=le.fit_transform(y)
print(y)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.085, random_state = 1)



from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski')
classifier.fit(X_train, y_train)

import pickle
file=open("model.pkl",'wb')
pickle.dump(classifier,file)

