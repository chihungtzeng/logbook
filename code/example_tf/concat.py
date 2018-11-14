import tensorflow as tf


def main():
    t1 = tf.constant([[1, 2, 3], [4, 5, 6]])
    t2 = tf.constant([[7, 8, 9], [10, 11, 12]])
    x = tf.concat([t1, t2], axis=0)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    y = tf.concat([t1, t2], axis=1)  # [[1, 2, 3, 7, 8, 9], [4, 5, 6, 10, 11, 12]]
    with tf.Session() as sess:
        print("t1:")
        print(sess.run(t1))
        print("concat along axis=0:")
        print(sess.run(x))
        print("concat along axis=1:")
        print(sess.run(y))


if __name__ == "__main__":
    main()
