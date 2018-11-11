# -*- coding: utf-8 -*-
"""
Dump one mnist instance into a image file.
"""
from PIL import Image
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data


def __dump_one():
    """ Evaluate the accuracy of the model."""
    mnist = input_data.read_data_sets("data", one_hot=True)
    test_data = mnist.test.images.reshape(
        (-1, 28, 28))
    single = test_data[0]
    dest = np.zeros((28, 28, 3))
    color = np.array([255, 255, 255])
    for i in range(28):
        for j in range(28):
            dest[i][j] = color * single[i][j]
    img = Image.fromarray(dest.astype("uint8"))
    img.save("mnist-example.png")

def main():
    """
    Prog entry.
    """
    __dump_one()


if __name__ == "__main__":
    main()
