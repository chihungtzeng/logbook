# -*- coding: utf-8 -*-
"""
Dump variables in tensorflow model.
"""
import argparse
import tensorflow as tf
import numpy as np


def __dump_vars_by_ckpt(ckpt):
    """
    Args:
    ckpt -- The checkpoint file name (without extensions.)
    """
    saver = tf.train.import_meta_graph(ckpt + ".meta")

    # Use the saver object normally after that.
    trainable_var_weights = {}
    global_vars = {}
    with tf.Session() as sess:
        # Initialize v1 since the saver will not.
        saver.restore(sess, ckpt)
        # print("all values %s" % sess.run(tf.global_variables()))
        print("traiable variables:")
        for _v in tf.trainable_variables():
            trainable_var_weights[_v.name] = _v.eval()
            print(_v.name)
        print("-" * 30)
        print("global variables:")
        for _v in tf.global_variables():
            global_vars[_v.name] = _v.eval()
            print(_v.name)

    np.savez_compressed("var_weights",
                        trainable_var_weights=trainable_var_weights,
                        global_vars=global_vars)
    # Use s=np.load() and s["trainable_var_weights"].item() to access.

def main():
    """
    Prog entry.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--ckpt", default="model_export/model.ckpt-80")
    args = parser.parse_args()
    __dump_vars_by_ckpt(args.ckpt)


if __name__ == "__main__":
    main()
