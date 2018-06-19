from textgenrnn import textgenrnn

fantasy_gen = textgenrnn(name="character_based_100e_dim500_sz512_lay2")
fantasy_gen.train_from_file('../data/fantasy.txt',
                            num_epochs=100,
                            word_level=False,
                            rnn_bidirectional=False,
                            dim_embeddings=500,
                            rnn_size=512,
                            rnn_layers=2)
