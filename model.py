import keras
import numpy as np
import pandas as pd
from keras.layers import Dense, Dropout
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

input_cols = [
    # 'anger', 'contempt', 'disgust', 'fear', 'happiness', 'neutral', 'sadness', 'surprise',
    # 'picture_arousal', 'sound_valence', 'sound_arousal', 'ans_time', 'emotion_ans',
    'valence_ans',
    'arousal_ans'
]
output_cols = ['picture_valence']

dataset = pd.read_csv("preprocessed/ALL-DATA-2.csv")

dataset = dataset.where(dataset["emotion_ans"] == -1)
dataset = dataset.dropna()

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
model.add(Dense(2, input_shape=(2,)))
model.add(Dropout(0.4))
model.add(Dense(1))
model.compile(loss='mse', optimizer='adam', metrics=['mse'])

model.fit(X_train, y_train, validation_data=(X_test, y_test), batch_size=200, epochs=100)
