import requests, time, json, os, shutil
import tensorflow as tf

# model = tf.keras.models.load_model('myModel.h5')

DatasetFolder = os.path.join("D:\\Users","Paul","Documents","VS Code Workspace","btcTrainingDatasets")
FileName  = "Data_7_8_2021.txt"
FullInputFilePath = os.path.join(DatasetFolder, FileName)

file = open(FullInputFilePath, "r")

watchedValues = json.load(file)
inputs = watchedValues["inputs"]
results = watchedValues["outputs"]

print(len(inputs))
print(len(results))

file.close()

inp = tf.keras.Input(shape=(10,))
dense = tf.keras.layers.Dense(5, activation=tf.keras.activations.relu)(inp)
outp = tf.keras.layers.Dense(3, activation=tf.keras.activations.sigmoid)(dense)
model = tf.keras.Model(inputs=inp, outputs=outp)

model.compile(optimizer=tf.keras.optimizers.Adam(), loss=tf.keras.losses.mean_squared_error, metrics=[tf.keras.metrics.Precision(),tf.keras.metrics.Recall(),tf.keras.metrics.MeanSquaredError()])

model.fit(inputs, results, epochs=5, shuffle=False)
