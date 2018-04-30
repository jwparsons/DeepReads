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
    text = (open("data/final/fantasy.txt").read())
    text = text.lower()

    # creating character/word mappings
    characters = sorted(list(set(text)))
    n_to_char = {n: char for n, char in enumerate(characters)}
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
    model.load_weights('models/fantasy/standard_cpu2/fantasy.h5')
    model.compile(loss='categorical_crossentropy', optimizer='adam')

    string_mapped = x[99]
    full_string = [n_to_char[value] for value in string_mapped]
    print(''.join(full_string))
    # generating characters
    for i in range(400):
        x = np.reshape(string_mapped, (1, len(string_mapped), 1))
        x = x / float(len(characters))

        pred_index = np.argmax(model.predict(x, verbose=0))
        seq = [n_to_char[value] for value in string_mapped]
        full_string.append(n_to_char[pred_index])

        string_mapped.append(pred_index)
        string_mapped = string_mapped[1:len(string_mapped)]

    # combining text
    txt = ""
    for char in full_string:
        txt = txt + char
    print(txt)


if __name__ == "__main__":
    main()
