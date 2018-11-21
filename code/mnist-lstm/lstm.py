# -*- coding: utf-8 -*-
"""
Predict handwritten graph by using RNN model.
"""
import argparse
import tensorflow as tf
from tensorflow.contrib import rnn
import numpy as np

#import mnist dataset
from tensorflow.examples.tutorials.mnist import input_data

#define constants
_NUM_ROWS = 28
_NUM_HIDDEN_STATES = 128  # hidden LSTM units
_NUM_ROW_PIXELS = 28  # rows of 28 pixels
_LEARNING_RATE = 0.001  # learning rate for adam
_NUM_CLASSES = 10  # mnist is meant to be classified in 10 classes(0-9).
_BATCH_SIZE = 128 # size of batch

#defining placeholders
#input image placeholder
_X = tf.placeholder("float", [None, _NUM_ROWS, _NUM_ROW_PIXELS])
#input label placeholder
_Y = tf.placeholder("float", [None, _NUM_CLASSES])


def __init_graph():
    # weights and biases of appropriate shape to accomplish above task
    weights = {
        "out": tf.Variable(tf.random_normal([_NUM_HIDDEN_STATES, _NUM_CLASSES]), name="weights_out")
    }

    biases = {
        "out": tf.Variable(tf.random_normal([_NUM_CLASSES]), name="biases_out")
    }
    def _rnn_model(_weights, _biases):
        # processing the input tensor from [_BATCH_SIZE,n_steps,_NUM_ROW_PIXELS]
        # to "_NUM_ROWS" number of [_BATCH_SIZE,_NUM_ROW_PIXELS] tensors
        _input = tf.unstack(_X, _NUM_ROWS, 1, name="rnn_input")

        # defining the network
        lstm_layer = rnn.BasicLSTMCell(_NUM_HIDDEN_STATES, forget_bias=1)
        outputs, _ = rnn.static_rnn(lstm_layer, _input, dtype="float32")

        # converting last output of dimension [_BATCH_SIZE,_NUM_HIDDEN_STATES] to
        # [_BATCH_SIZE,_NUM_CLASSES] by out_weight multiplication
        return tf.matmul(outputs[-1], weights["out"]) + biases["out"]

    prediction = _rnn_model(weights, biases)
    # loss_function
    loss = tf.reduce_mean(
        tf.nn.softmax_cross_entropy_with_logits(logits=prediction, labels=_Y))
    # optimization
    opt = tf.train.AdamOptimizer(learning_rate=_LEARNING_RATE).minimize(loss)

    # model evaluation
    correct_prediction = tf.equal(tf.argmax(prediction, 1), tf.argmax(_Y, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

    # initialize variables
    init = tf.global_variables_initializer()
    return init, opt, accuracy, loss


def train():
    """
    train and save model.
    """
    init, opt, accuracy, loss = __init_graph()
    mnist = input_data.read_data_sets("data", one_hot=True)
    with tf.Session() as sess:
        sess.run(init)
        loop_count = 1
        while loop_count < 800:
            batch_x, batch_y = mnist.train.next_batch(batch_size=_BATCH_SIZE)
            batch_x = batch_x.reshape(
                (_BATCH_SIZE, _NUM_ROWS, _NUM_ROW_PIXELS))
            sess.run(opt, feed_dict={_X: batch_x, _Y: batch_y})

            if loop_count % 10 == 0:
                acc = sess.run(accuracy, feed_dict={_X: batch_x, _Y: batch_y})
                los = sess.run(loss, feed_dict={_X: batch_x, _Y: batch_y})
                print("For loop_count ", loop_count)
                print("Accuracy: {}, Loss: {}".format(acc, los))
                print("-" * 20)
            loop_count += 1
        saver = tf.train.Saver()
        save_path = saver.save(sess, "model_export/model.ckpt")
        print("save model to ", save_path)
        writer = tf.summary.FileWriter('model_export/', sess.graph)
        writer.close()


def evaluate():
    """ Evaluate the accuracy of the model."""
    mnist = input_data.read_data_sets("data", one_hot=True)
    _, _, accuracy, _ = __init_graph()
    with tf.Session() as sess:
        saver = tf.train.Saver()
        print("restore from model.ckpt")
        saver.restore(sess, "model_export/model.ckpt")
        # calculating test accuracy
        test_data = mnist.test.images.reshape(
            (-1, _NUM_ROWS, _NUM_ROW_PIXELS))
        test_label = mnist.test.labels
        print("Testing Accuracy:", sess.run(
            accuracy, feed_dict={_X: test_data, _Y: test_label}))


def dump_var():
    """ Evaluate the accuracy of the model."""
    __init_graph()
    trainable_weights = {}
    with tf.Session() as sess:
        saver = tf.train.Saver()
        print("restore from model.ckpt")
        saver.restore(sess, "model_export/model.ckpt")
        for _v in tf.trainable_variables():
            print(_v.name, _v.shape)
            trainable_weights[_v.name] = _v.eval()
    np.savez_compressed("var_weights", trainable_weights=trainable_weights)


def main():
    """
    Prog entry.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--train", action="store_true")
    parser.add_argument("--evaluate", action="store_true")
    parser.add_argument("--dump-var", action="store_true")
    args = parser.parse_args()
    if args.train:
        train()
    elif args.evaluate:
        evaluate()
    elif args.dump_var:
        dump_var()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
