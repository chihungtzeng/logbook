import tensorflow as tf


def main():
    t1 = tf.constant([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
    with tf.Session() as sess:
        print("t1:")
        print(sess.run(t1))
        print("3 split along axis=0:")
        i, j, k = tf.split(t1, num_or_size_splits=3, axis=0)
        print(j.eval())



if __name__ == "__main__":
    main()
