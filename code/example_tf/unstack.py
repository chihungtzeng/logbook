import tensorflow as tf
import numpy as np

def main():
    a = tf.constant([1, 2, 3, 4])
    b = tf.constant([5, 6, 7, 8])
    a_b = tf.stack([a, b], axis=0)
    c = tf.constant([
        [[1,2,3], [4,5,6]],
        [[7,8,9], [9,8,7]]])
    unstack_0 = tf.unstack(a_b, axis=0)
    unstack_1 = tf.unstack(a_b, axis=1)
    unstack_c_0 = tf.unstack(c, axis=0)
    unstack_c_1 = tf.unstack(c, axis=1)
    with tf.Session() as sess:
        print("stack:", sess.run(a_b))
        print("unstack, axis=0: ", sess.run(unstack_0))
        print("unstack, axis=1: ", sess.run(unstack_1))
        print("c:", sess.run(c))
        print("unstack_c_0:")
        print(sess.run(unstack_c_0))
        print("unstack_c_1:")
        print(sess.run(unstack_c_1))



if __name__ == "__main__":
    main()
