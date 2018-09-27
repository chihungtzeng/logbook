# -*- coding: utf-8 -*-
"""
Handle the Input of CIFAR-10 dataset.
"""
import pickle
import numpy as np


def load_cifar_from_pickle(file_name):
    """
    Load CIFAR-10 Images from pickled files.

    Returns:
    data -- An array of shape (10000, 32, 32, 3). Each (32, 32, 3) is an image.
    categories -- An array of shape (10000,) denoting the corresponding
                  image category.

    Args:
    file_name -- A pickled cifar-10 file name, like data_batch_1.
    """
    with open("cifar-10-batches-py/" + file_name, "rb") as _fp:
        contents = pickle.load(_fp, encoding="bytes")

    data = contents[b"data"]
    data = data.reshape(10000, 3, 32, 32).transpose(0, 2, 3, 1).astype("float")
    categories = np.array(contents[b"labels"])
    return data, categories
