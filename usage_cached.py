'''
ELMo usage example to write biLM embeddings for an entire dataset to
a file.
'''

import os
import h5py
from bilm import dump_bilm_embeddings


# Create the dataset file.
dataset_file = 'data/raw_sentences.txt'

# Location of pretrained LM.  Here we use the test fixtures.
datadir = os.path.join('tests', 'fixtures', 'model')
vocab_file = 'data/blm-output-result/bilm-output-result/vocab-train.txt'
options_file = 'data/blm-output-result/bilm-output-result/options.json'
weight_file = 'data/blm-output-result/bilm-output-result/weights.hdf5'

# Dump the embeddings to a file. Run this once for your dataset.
embedding_file = 'elmo_embeddings.hdf5'
dump_bilm_embeddings(
    vocab_file, dataset_file, options_file, weight_file, embedding_file
)

# Load the embeddings from the file -- here the 2nd sentence.
with h5py.File(embedding_file, 'r') as fin:
    second_sentence_embeddings = fin['1'][...]

