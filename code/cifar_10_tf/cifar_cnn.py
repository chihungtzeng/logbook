# -*- coding: utf-8 -*-
"""
Convolutional Network for classifying CIFAR-10 Images.
"""
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
    conv3_64 = tf.layers.conv2d(
        inputs=input_layer, filters=64, kernel_size=[3, 3], padding="same",
        activation=tf.nn.relu)
    pool1 = tf.layers.max_pooling2d(inputs=conv3_64,
                                    pool_size=[2, 2], strides=2)
    pool1_flat = tf.reshape(pool1, [-1, 16 * 16 * 64])
    logits = tf.layers.dense(inputs=pool1_flat, units=10)
    predictions = {"classes": tf.argmax(logits, axis=1),
                   "probabilities": tf.nn.softmax(logits, name="softmax_tensor")}

    if mode == tf.estimator.ModeKeys.PREDICT:
        return tf.estimator.EstimatorSpec(mode=mode, predictions=predictions)
    print("logits shape: {}".format(logits.shape))
    print("label shape: {}".format(labels.shape))
    loss = tf.losses.sparse_softmax_cross_entropy(
        labels=labels, logits=logits)
    if mode == tf.estimator.ModeKeys.TRAIN:
        optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.001)
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
    model = tf.estimator.Estimator(model_fn=cifar_cnn_model, model_dir="/mnt/ramdisk/cifar10")
    train_x, train_y = get_training_data("data_batch_1")
    def _train_input_fn(train_x, train_y, batch_size=1000):
        dataset = tf.data.Dataset.from_tensor_slices((train_x, train_y))
        return dataset.shuffle(1000).repeat(count=32).batch(batch_size)
    model.train(input_fn=lambda: _train_input_fn(train_x, train_y))

    test_x, test_y = get_training_data("test_batch")
    def _eval_input_fn(test_x, test_y):
        test_y = test_y.reshape(10000, 1)
        dataset = tf.data.Dataset.from_tensor_slices((test_x, test_y))
        return dataset
    eval_results = model.evaluate(input_fn=lambda: _eval_input_fn(test_x, test_y))

    print('\nEvaluation results:\n\t%s\n' % eval_results)

    # Export the model
    #image = tf.placeholder(tf.float32, [None, 32, 32])
    #input_fn = tf.estimator.export.build_raw_serving_input_receiver_fn({
    #    'image': image,
    #})
    #model.export_savedmodel("/mnt/ramdisk/cifar10_model", input_fn)
    #print("Saved to /mnt/ramdisk/cifar10_model")


if __name__ == "__main__":
    tf.logging.set_verbosity(tf.logging.INFO)
    tf.app.run(main)
