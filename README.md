# bilm-tf for E2E-German with TüBa-D/Z
Tensorflow implementation of the pretrained biLM used to compute ELMo
representations from ["Deep contextualized word representations"](http://arxiv.org/abs/1802.05365).

This repository supports both training biLMs and using pre-trained models for prediction.

We also have a pytorch implementation available in [AllenNLP](http://allennlp.org/).

You may also find it easier to use the version provided in [Tensorflow Hub](https://www.tensorflow.org/hub/modules/google/elmo/2) if you just like to make predictions.

Citation:

```
@inproceedings{Peters:2018,
  author={Peters, Matthew E. and  Neumann, Mark and Iyyer, Mohit and Gardner, Matt and Clark, Christopher and Lee, Kenton and Zettlemoyer, Luke},
  title={Deep contextualized word representations},
  booktitle={Proc. of NAACL},
  year={2018}
}
```


## Installing
Install python version 3.5 or later, tensorflow version 1.2 and h5py:

```
pip3 install tensorflow-gpu==1.2 h5py
python3 setup.py install
```

Ensure the tests pass in your environment by running:
```
python3 -m unittest discover tests/
```

## Using bilm-tf for E2E-German and TüBa-D/Z
First download the pretrained german elmo model from https://github.com/t-systems-on-site-services-gmbh/german-elmo-model

Then use the *parse_tuebadz.py* script to convert your CoNLL Data from TüBa-D/Z into raw text. The scripts were applied on the TüBa-D/Z version 9.1 datasets in CoNLL Format. Output name should be 'raw_text.txt' and must be in the folder *data/raw_text.txt*. Otherwise the *usage_cached.py* needs to be edited.
```
python3 parse_tuebadz.py --conll-input-name-- --output-name--
```
Afterwards use the *usage_cached.py* script to create the Elmo Embeddings for the raw text input file.
```
python3 usage_cached.py
```
This creates a *elmo_embeddings.hdf5* file, which has the wrong data format. To convert it to the E2E format use the *key_mapper.py* script, which takes the CoNLL data, the created elmo embeddings from usage_cached and the new name of the elmo embedding file as arguments.
```
python3 key_mapper.py --conll-input-name-- --elmo-input-name-- --elmo-output-name--
```

The created *--elmo-output-name--* file can now be used for E2E-German.

