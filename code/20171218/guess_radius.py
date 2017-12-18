# -*- coding: utf-8 -*-
"""
A toy program that generates points around a circle and try to use deep
learning to figure out the circle.

Note: This program is buggggggy! The target function must be redefined.
"""
from __future__ import print_function
import random
import math
import tensorflow as tf
import matplotlib.pyplot as plt


def gen_approx_points(radius=2.7, num_points=50):
    """
    Generate a list of points (x, y) that close to the circle with origin
    (0, 0) and radius=|radius|.
    """
    ret = []
    r = radius
    offset = r / 5
    for _ in xrange(0, num_points):
        x = random.uniform(-r, r)
        y = math.sqrt(r**2 - x**2) * random.choice([-1, 1])
        # Given random offset to (x, y)
        ret.append((x + random.uniform(-offset, offset),
                    y + random.uniform(-offset, offset)))
    return ret


def __guess_radius(points):
    x_train = [_[0] for _ in points]
    y_train = [_[1] for _ in points]
    r = tf.Variable([0.3], dtype=tf.float32)
    x = tf.placeholder(tf.float32)
    y = tf.placeholder(tf.float32)
    idv_square = tf.abs(tf.subtract(tf.sqrt(tf.pow(x, 2) + tf.pow(y, 2)), r))
    square_sum = tf.reduce_mean(tf.reduce_sum(idv_square))
    init = tf.global_variables_initializer()
    optimizer = tf.train.GradientDescentOptimizer(0.01)
    train = optimizer.minimize(square_sum)
    sess = tf.Session()
    sess.run(init)
    for _ in xrange(0, 100):
        sess.run(train, {x: x_train, y: y_train})
    guessed_r, ssum = sess.run([r, square_sum], {x: x_train, y: y_train})
    print("guessed_r: {}".format(guessed_r))
    print("ssum: {}".format(ssum))
    return guessed_r


def main():
    radius = 2.7
    points = gen_approx_points(radius)

    guessed_r = __guess_radius(points)

    org_x = [_[0] for _ in points]
    org_y = [_[1] for _ in points]
    circle = plt.Circle((0, 0), radius, color="r", fill=False)
    guessed_circle = plt.Circle((0, 0), guessed_r, color="b", fill=False)
    # gcf() means Get Current Figure
    # gca() means Get Current Axis
    plt.gcf().gca().add_artist(circle)
    plt.gcf().gca().add_artist(guessed_circle)
    plt.scatter(org_x, org_y)
    plt.show()
    # output = "/mnt/ramdisk/guess_radius.pdf"
    # plt.savefig("/mnt/ramdisk/guess_radius.pdf")
    # logging.info("Save to %s", output)

if __name__ == "__main__":
    main()
