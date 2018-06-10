import warnings
with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=FutureWarning)
    import numpy as np
    import pandas as pd
    from keras.models import Sequential
    from keras.layers import Dense
    from keras.layers import Dropout
    from keras.layers import LSTM
    from keras.utils import np_utils


def main():
    # loading of data
    text = (open("../data/final/fantasy.txt").read())
    text = text.lower()

    # creating character/word mappings
    characters = sorted(list(set(text)))
    char_to_n = {char: n for n, char in enumerate(characters)}

    # data pre-processing
    x = []
    y = []
    length = len(text)
    seq_length = 100

    for i in range(0, length - seq_length, 1):
        sequence = text[i:i + seq_length]
        label = text[i + seq_length]
        x.append([char_to_n[char] for char in sequence])
        y.append(char_to_n[label])

    x_modified = np.reshape(x, (len(x), seq_length, 1))
    x_modified = x_modified / float(len(characters))
    y_modified = np_utils.to_categorical(y)

    # train the model
    model = Sequential()
    model.add(LSTM(256, input_shape=(x_modified.shape[1], x_modified.shape[2]), return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(256))
    model.add(Dropout(0.2))
    model.add(Dense(y_modified.shape[1], activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam')

    model.fit(x_modified, y_modified, epochs=20, batch_size=50)
    model.save_weights('../models/fantasy/standard_cpu2/fantasy.h5')


if __name__ == "__main__":
    main()
