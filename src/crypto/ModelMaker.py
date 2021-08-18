import tensorflow as tf

inp = tf.keras.Input(shape=(10,1))
dense = tf.keras.layers.Dense(5, activation=tf.keras.activations.relu)(inp)
outp = tf.keras.layers.Dense(3, activation=tf.keras.activations.sigmoid)(dense)
model = tf.keras.Model(inputs=inp, outputs=outp)

model.compile(optimizer=tf.keras.optimizers.Adam(), loss=tf.keras.losses.mean_squared_error, metrics=[tf.keras.metrics.Precision(),tf.keras.metrics.Recall(),tf.keras.metrics.MeanSquaredError()])

print(model.output_shape)
