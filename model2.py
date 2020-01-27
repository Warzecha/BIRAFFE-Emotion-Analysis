from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
from keras.layers import Dense, Dropout
from sklearn import preprocessing
import matplotlib.pyplot as plt


input_cols = ['anger', 'contempt', 'disgust', 'fear', 'happiness', 'neutral', 'sadness', 'surprise', 'picture_valance',
              'picture_arousal', 'sound_valance', 'sound_arousal', 'ans_time', 'emotion_ans', 'valence_ans',
              'arousal_ans']

dataset = pd.read_csv("preprocessed/ALL-DATA.csv")

print(dataset.head())

print("Dataset isnull", dataset.isnull().any())

x = dataset[input_cols].values
scaler_x = preprocessing.MinMaxScaler()
X_scale = scaler_x.fit_transform(x)


kmeans = KMeans(n_clusters=2, random_state=0).fit(X_scale)

y_kmeans = kmeans.predict(X_scale)

plt.scatter(X_scale[:, 0], X_scale[:, 1], c=y_kmeans, s=50, cmap='viridis')

centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)
plt.show()
plt.savefig("cluster.png")
