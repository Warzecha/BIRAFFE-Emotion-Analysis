import keras
import numpy as np
import pandas as pd
from keras.layers import Dense, Dropout
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

input_cols = ['ANGER', 'CONTEMPT', 'DISGUST', 'FEAR', 'HAPPINESS', 'NEUTRAL', 'SADNESS', 'SURPRISE', 'ValenceMean-IAPS',
              'ArousalMean-IAPS', 'ValenceMean_IADS', 'ArousalMean_IADS', 'ANS-TIME', 'EMO-ANS', 'VALENCE-ANS',
              'AROUSAL-ANS']
output_cols = ['EXTRAVERSION']

dataset = pd.read_csv("preprocessed/ALL-DATA.csv")

print("Dataset isnull", dataset.isnull().any())

x = dataset[input_cols].values
y = dataset[output_cols].values
y = np.reshape(y, (-1, 1))
scaler_x = preprocessing.MinMaxScaler()
scaler_y = preprocessing.MinMaxScaler()
xscale = scaler_x.fit_transform(x)
yscale = scaler_y.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(xscale, yscale)

# print(X_train[1, :].shape)
# print(y_train[1, :].shape)
#
# print("Is nan")
# print(np.isnan(X_train).any())

model = keras.models.Sequential()
model.add(Dense(8, input_shape=(16,)))
model.add(Dropout(0.4))
model.add(Dense(1))
model.compile(loss='mse', optimizer='adam', metrics=['mse'])

model.fit(X_train, y_train, validation_data=(X_test, y_test), batch_size=100, epochs=50)
