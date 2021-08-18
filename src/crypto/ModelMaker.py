import tensorflow as tf

inp = tf.keras.Input(shape=(10,))
dense1 = tf.keras.layers.Dense(10, activation=tf.keras.activations.relu)(inp)
dense2 = tf.keras.layers.Dense(5, activation=tf.keras.activations.relu)(dense1)
outp = tf.keras.layers.Dense(3, activation=tf.keras.activations.sigmoid)(dense2)
model = tf.keras.Model(inputs=inp, outputs=outp)

model.compile(optimizer=tf.keras.optimizers.Adam(), loss=tf.keras.losses.mean_squared_error, metrics=[tf.keras.metrics.Precision(),tf.keras.metrics.Recall(),tf.keras.metrics.MeanSquaredError()])

print(model.output_shape)
