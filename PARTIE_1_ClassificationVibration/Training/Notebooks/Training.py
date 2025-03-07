import tensorflow as tf
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

data = pd.read_csv("Training_data.csv")

X = data.iloc[:, :-1].values   
y = data.iloc[:, -1].values  

# Normalisation des données
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Separation des données à des données pour le test et la validation
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

# Un réseau de neuron simple :
model = tf.keras.Sequential([
    tf.keras.layers.Dense(16, activation='relu', input_shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(8, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Parametrer le réseau de neurons
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Entrainemen du réseau
model.fit(X_train, y_train, epochs=10, batch_size=8)


# Évaluer le modèle sur les données de test

test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=2)

# Afficher la précision et la perte sur les données de test

print(f"Test Loss: {test_loss}")

print(f"Test Accuracy: {test_accuracy}")


# Le code suivant est généré par ChatGPT pour la conversion d'un model tflite a un fichier .h avec les parametres du modèle
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Save the TensorFlow Lite model as a .tflite file
with open('model.tflite', 'wb') as f:
    f.write(tflite_model)

# Convert the .tflite model to a C array format (uint8_t)
model_array = ', '.join(f'0x{byte:02x}' for byte in tflite_model)

header_text = f"""
const uint8_t model[] = {{
    {model_array}
}};

"""

# Save the header file
with open('model.h', 'w') as f:
    f.write(header_text)

print("model.h has been generated!")
