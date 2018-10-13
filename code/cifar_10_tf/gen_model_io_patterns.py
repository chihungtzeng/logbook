# -*- coding: utf-8 -*-
"""
Convolutional Network for classifying CIFAR-10 Images.
Current result: {'accuracy': 0.4537, 'loss': 1.5074927, 'global_step': 200}
"""
import numpy as np
import json
import io
import tensorflow as tf
from cifar_reader import load_cifar_from_pickle

def get_training_data(file_name):
    """
    Get training data and the corresponding categories.
    """
    x_data, y_data = load_cifar_from_pickle(file_name)
    return x_data, y_data


def cifar_cnn_model(features, labels, mode):
    """
    Model for CNN.
    """
    input_layer = tf.reshape(features, [-1, 32, 32, 3])
    conv1_64 = tf.layers.conv2d(
        inputs=input_layer, filters=64, kernel_size=[5, 5], padding="same",
        activation=tf.nn.relu, name="conv1_64")
    pool1 = tf.layers.max_pooling2d(inputs=conv1_64,
                                    pool_size=[2, 2], strides=2)
    conv2_64 = tf.layers.conv2d(
        inputs=pool1, filters=64, kernel_size=[5, 5], padding="same",
        activation=tf.nn.relu, name="conv2_64")
    pool2 = tf.layers.max_pooling2d(inputs=conv2_64,
                                    pool_size=[2, 2], strides=2)

    pool2_flat = tf.reshape(pool2, [-1, 8 * 8 * 64])

    dense = tf.layers.dense(inputs=pool2_flat, units=128, activation=tf.nn.relu)
    dropout = tf.layers.dropout(inputs=dense, rate=0.4,
                                training=mode == tf.estimator.ModeKeys.TRAIN)
    logits = tf.layers.dense(inputs=dropout, units=10, name="logits")
    predictions = {"classes": tf.argmax(logits, axis=1),
                   "probabilities": tf.nn.softmax(logits, name="softmax_tensor")}

    if mode == tf.estimator.ModeKeys.PREDICT:
        return tf.estimator.EstimatorSpec(mode=mode, predictions=predictions)
    loss = tf.losses.sparse_softmax_cross_entropy(
        labels=labels, logits=logits)
    if mode == tf.estimator.ModeKeys.TRAIN:
        optimizer = tf.train.AdamOptimizer(learning_rate=0.001)
        train_op = optimizer.minimize(loss=loss,
                                      global_step=tf.train.get_global_step())
        return tf.estimator.EstimatorSpec(mode=mode, loss=loss,
                                          train_op=train_op)
    eval_metric_ops = {
        "accuracy": tf.metrics.accuracy(
            labels=labels, predictions=predictions["classes"])}
    return tf.estimator.EstimatorSpec(mode=mode, loss=loss, eval_metric_ops=eval_metric_ops)


def main(_):
    """
    Prog entry.
    """
    model = tf.estimator.Estimator(model_fn=cifar_cnn_model, model_dir="./model_export")
    test_x, test_y = get_training_data("test_batch")

# Predict
    def _predict_input_fn(i):
        _test_x = test_x[i:i+1]
        dataset = tf.data.Dataset.from_tensor_slices(_test_x)
        return dataset
    for i in range(0, 3):
        results = list(model.predict(input_fn=lambda: _predict_input_fn(i)))
        in_out = {"in": test_x[i], "out": results[0]["probabilities"]}
        fname = "in_out_{}".format(i)
        np.savez_compressed(fname, in_out)
        print("Write {}".format(fname))


if __name__ == "__main__":
    tf.logging.set_verbosity(tf.logging.INFO)
    tf.app.run(main)
