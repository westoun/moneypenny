#!/usr/bin/env python3

from os import path


class SimilarityUtilsFactory():

    def get_similarity_utils(self):
        if self._infersent_exists():
            return self._get_infersent_similarity_utils()
        else:
            raise NotImplementedError(
                "An alternative similarity engine has not been implemented!")

    def _get_infersent_similarity_utils(self):
        from utils.similarity.infersent_similarity_utils import InfersentSimilarityUtils
        infersent_similarity_utils = InfersentSimilarityUtils()
        return infersent_similarity_utils

    def _infersent_exists(self):
        return path.exists("infersent")
