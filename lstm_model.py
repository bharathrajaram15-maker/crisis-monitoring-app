import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

def build_model():
    model = Sequential([
        LSTM(50, return_sequences=True, input_shape=(10, 3)),
        LSTM(50),
        Dense(3, activation='softmax')
    ])

    model.compile(optimizer='adam', loss='categorical_crossentropy')
    return model

def predict(model, sequence):
    sequence = np.array(sequence).reshape(1, 10, 3)
    pred = model.predict(sequence)
    return int(np.argmax(pred))
