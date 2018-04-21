import warnings
with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=FutureWarning)
    import numpy
    from keras.models import Sequential
    from keras.layers import Dense
    from keras.layers import Dropout
    from keras.layers import LSTM
    from keras.callbacks import ModelCheckpoint
    from keras.utils import np_utils


def main():
    # load data
    filename = "data/final/mystery.txt"
    raw_text = open(filename).read().lower()

    # create mapping of unique chars to integers
    chars = sorted(list(set(raw_text)))
    char_to_int = dict((c, i) for i, c in enumerate(chars))

    # summarize the loaded data
    n_chars = len(raw_text)
    n_vocabulary = len(chars)
    print("Total Characters: ", n_chars)
    print("Total Vocabulary: ", n_vocabulary)

    # prepare the dataset of input to output pairs encoded as integers
    sequence_length = 100
    x_data = []
    y_data = []

    for i in range(0, n_chars - sequence_length, 1):
        seq_in = raw_text[i:i + sequence_length]
        seq_out = raw_text[i + sequence_length]
        x_data.append([char_to_int[char] for char in seq_in])
        y_data.append(char_to_int[seq_out])
    n_patterns = len(x_data)
    print("Total Patterns: ", n_patterns)

    # reshape X to be [samples, time steps, features]
    x = numpy.reshape(x_data, (n_patterns, sequence_length, 1))

    # normalize
    x = x / float(n_vocabulary)

    # one hot encode the output variable
    y = np_utils.to_categorical(y_data)

    # define the LSTM model
    model = Sequential()
    model.add(LSTM(256, input_shape=(x.shape[1], x.shape[2]), return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(256))
    model.add(Dropout(0.2))
    model.add(Dense(y.shape[1], activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam')

    # define the checkpoint
    file_path = "models/mystery/mystery-{epoch:02d}-{loss:.4f}.hdf5"
    checkpoint = ModelCheckpoint(file_path, monitor='loss', verbose=1, save_best_only=True, mode='min')
    callbacks_list = [checkpoint]

    # fit the model
    model.fit(x, y, epochs=20, batch_size=50, callbacks=callbacks_list)


if __name__ == "__main__":
    main()
