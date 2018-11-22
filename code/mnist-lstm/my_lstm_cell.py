# -*- coding: utf-8 -*-
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


class MyLSTMCell(object):
    def __init__(self, num_hidden_state):
        self.kernel = None
        self.bias = None
        self.hidden_state = np.zeros(num_hidden_state)
        self.cell_state = np.zeros(num_hidden_state)

    def set_kernel_and_bias(self, kernel, bias):
        """kernel is a 2d matrix"""
        self.kernel = kernel
        self.bias = bias

    def reset(self):
        self.hidden_state = np.zeros_like(self.hidden_state)
        self.cell_state = np.zeros_like(self.cell_state)

    def call(self, inputs):
#        print(inputs.shape)
#        print(self.hidden_state.shape)
        inputs_h = np.concatenate((inputs, self.hidden_state))
        gate_inputs = np.dot(inputs_h, self.kernel) + self.bias
        _i, _g, _f, _o = np.split(gate_inputs, 4)
        self.cell_state = self.cell_state * sigmoid(_f + 1) + sigmoid(_i) * np.tanh(_g)
        self.hidden_state = np.tanh(self.cell_state) * sigmoid(_o)


def load_npz(file_name):
    """Returns:
        weights_out:0 (128, 10)
        biases_out:0 (10,)
        rnn/basic_lstm_cell/kernel:0 (156, 512)
        rnn/basic_lstm_cell/bias:0 (512,)
    """
    return np.load(file_name)["trainable_weights"][()]


def main():
    """Prog entry"""
    weights = load_npz("var_weights.npz")
    lstm_cell = MyLSTMCell(128)
    lstm_cell.set_kernel_and_bias(weights["rnn/basic_lstm_cell/kernel:0"],
                                  weights["rnn/basic_lstm_cell/bias:0"])
    why = weights["weights_out:0"]
    bhy = weights["biases_out:0"]
    mnist = input_data.read_data_sets("data", one_hot=True)
    test_data = mnist.test.images.reshape((-1, 28, 28))
    test_label = mnist.test.labels
    num_accuracy = 0
    num_samples = test_data.shape[0]
    for nth_img in range(num_samples):
        lstm_cell.reset()
        img = test_data[nth_img]
        ground_truth = np.argmax(test_label[nth_img])
        for row in range(28):
            lstm_cell.call(img[row])
        _y = np.dot(lstm_cell.hidden_state, why) + bhy
        actual_label = np.argmax(_y)
        if ground_truth == actual_label:
            num_accuracy += 1

    print("Accuacy: {:.2f} ({}/{})".format(
        num_accuracy / num_samples, num_accuracy, num_samples))



if __name__ == "__main__":
    main()
