from textgenrnn import textgenrnn

fantasy_gen_1 = textgenrnn('../models/fantasy/fantasy_char_100e_dim500_uni_sz512_lay2_weights.hdf5')
fantasy_gen_1.generate_samples(temperatures=[0.5, 0.5, 0.5, 0.5, 0.5])
