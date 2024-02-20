#%% import necesary libraries
import pandas as pd
import numpy as np
from scipy import stats

#%% reading the dataset
# reading the dataset skipping the 2 initial rows
df = pd.read_excel("dataset1.xlsx", skiprows=2)
# dropping the first column (indexes in the original dataset)
df.drop(df.columns[0], axis=1, inplace = True)
# changing the name of a column"
df.columns.values[5] = "MontoPrestamo"
df.columns.values[4] = "segundo"
df.head(3)

#%% question 2

dfna = df[pd.isnull(df.MontoPrestamo)]
df = df.drop(dfna.index)
df.shape
# check if values are within 0.1 standard deviations from the mean
df[np.abs(stats.zscore(df["MontoPrestamo"])) < 0.1]

#%% question 3
df.segundo.count()

#%% question 4
from keras.models import Sequential
from keras.layers import Dense

model = Sequential([
    Dense(2, activation="relu", input_dim = 8),
    Dense(2**3, activation="relu"),
    Dense(8**4, activation="relu"),
    Dense(2**5, activation="relu"),
    Dense(19**2, activation="relu"),
    Dense(2+56, activation="relu"),
    Dense(12+0, activation="relu"),
    Dense(6**2, activation="relu"),
    Dense(30, activation="relu"),
    Dense(1, activation="relu"),
    Dense(1, activation="sigmoid")
])

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

#%% question 4

model.summary()

#%% question 5
np.quantile(df['MontoPrestamo'], 0.25)

#%% question 8
df[df["SECTOR ECONÓMICO"] == "CONSTRUCCION"].shape[0]