#!/usr/bin/env python3

import numpy as np
import spacy
from spacy.lang.en import English
import torch

from infersent.models import InferSent

MODEL_VERSION = 1
MODEL_PATH = "infersent/encoder/infersent%s.pkl" % MODEL_VERSION
MODEL_PARAMS = {'bsize': 64, 'word_emb_dim': 300, 'enc_lstm_dim': 2048,
                'pool_type': 'max', 'dpout_model': 0.0, 'version': MODEL_VERSION}
W2V_PATH = 'infersent/GloVe/glove.840B.300d.txt'


class InfersentSimilarityUtils:

    def __init__(self):
        self.model = InferSent(MODEL_PARAMS)
        self.model.load_state_dict(torch.load(MODEL_PATH))
        self.model.set_w2v_path(W2V_PATH)
        self.model.build_vocab_k_words(K=100000)

    def sentencize(self, input_string):
        """Produces a list of sentences"""
        nlp = English()
        nlp.add_pipe(nlp.create_pipe('sentencizer'))
        doc = nlp(input_string)
        sentences = [s.text.strip() for s in doc.sents if s.text.strip() != '']
        return sentences

    def cosine(self, u, v):
        return np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))

    def get_similarity(self, sentence1, sentence2):
        encoding1 = self.model.encode([sentence1])[0]
        encoding2 = self.model.encode([sentence2])[0]
        similarity = self.cosine(encoding1, encoding2)
        return similarity 