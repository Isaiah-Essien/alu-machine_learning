#!/usr/bin/env python3
'''Evaluate'''

import tensorflow as tf
import numpy as np


def evaluate(X, Y, save_path):
    """
    Evaluates the output of a neural network
    Args:
    X: numpy.ndarray - input data to evaluate
    Y: numpy.ndarray - one-hot labels for X
    save_path: str - location to load the model from
    Returns:
    tuple - network’s prediction, accuracy, and loss
    """
    # Create placeholders
    nx = X.shape[1]
    classes = Y.shape[1]
    x = tf.placeholder(tf.float32, shape=(None, nx), name='x')
    y = tf.placeholder(tf.float32, shape=(None, classes), name='y')

    # Restore the model
    with tf.Session() as sess:
        # Load the meta graph and restore the weights
        saver = tf.train.import_meta_graph(save_path + '.meta')
        saver.restore(sess, save_path)

        # Get tensors from the graph's collection
        graph = tf.get_default_graph()
        y_pred = graph.get_tensor_by_name('y_pred:0')
        loss = graph.get_tensor_by_name('loss:0')
        accuracy = graph.get_tensor_by_name('accuracy:0')

        # Evaluate the model
        feed_dict = {x: X, y: Y}
        pred, loss_val, accuracy_val = sess.run(
            [y_pred, loss, accuracy], feed_dict=feed_dict)

    return pred, accuracy_val, loss_val
