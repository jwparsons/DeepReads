from textgenrnn import textgenrnn

fantasy_gen = textgenrnn(name="mystery_char_200e_dim500_sz512_lay2")
fantasy_gen.train_from_file('../data/mystery_big.txt',
                            num_epochs=200,
                            word_level=False,
                            rnn_bidirectional=False,
                            dim_embeddings=500,
                            rnn_size=512,
                            rnn_layers=2)
