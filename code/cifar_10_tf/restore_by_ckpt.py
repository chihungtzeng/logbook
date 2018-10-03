# -*- coding: utf-8 -*-
"""
Convolutional Network for classifying CIFAR-10 Images.
Current result: {'accuracy': 0.4537, 'loss': 1.5074927, 'global_step': 200}
"""
import tensorflow as tf


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


def main():
    """
    Prog entry.
    """
    #model = tf.estimator.Estimator(model_fn=cifar_cnn_model, model_dir="./model_export")
    #saver = tf.train.Saver()
    saver = tf.train.import_meta_graph("./model_export/model.ckpt-80.meta")

    # Use the saver object normally after that.
    with tf.Session() as sess:
        # Initialize v1 since the saver will not.
        saver.restore(sess, "model_export/model.ckpt-80")
        # print("all values %s" % sess.run(tf.global_variables()))
        for v in tf.trainable_variables():
            print(v.name)
            print(v.shape)
            if v.name == "logits/bias:0":
                print(v.eval())
        print(sess.run(tf.get_default_graph().get_tensor_by_name("logits/bias:0")))

if __name__ == "__main__":
    main()
