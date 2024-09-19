#!/usr/bin/env python3
'''train the model'''

import tensorflow as tf
import numpy as np

# Import the previously defined functions
calculate_accuracy = __import__(
    '3-calculate_accuracy').calculate_accuracy
calculate_loss = __import__(
    '4-calculate_loss').calculate_loss
create_placeholders = __import__(
    '0-create_placeholders').create_placeholders
create_train_op = __import__(
    '5-create_train_op').create_train_op
forward_prop = __import__('2-forward_prop').forward_prop


def train(X_train, Y_train, X_valid, Y_valid, layer_sizes,
          activations, alpha, iterations, save_path="/tmp/model.ckpt"):
    """
    Builds, trains, and saves a neural network classifier
    Args:
    X_train: numpy.ndarray - training input data
    Y_train: numpy.ndarray - training labels
    X_valid: numpy.ndarray - validation input data
    Y_valid: numpy.ndarray - validation labels
    layer_sizes: list - number of nodes in each layer of the network
    activations: list - 
    activation functions for each layer of the network
    alpha: float - learning rate
    iterations: int - number of iterations to train over
    save_path: str - path to save the model
    Returns:
    str - path where the model was saved
    """
    # Create placeholders
    nx = X_train.shape[1]
    classes = Y_train.shape[1]
    x, y = create_placeholders(nx, classes)

    # Forward propagation
    y_pred = forward_prop(x, layer_sizes, activations)

    # Calculate loss
    loss = calculate_loss(y, y_pred)

    # Create training operation
    train_op = create_train_op(loss, alpha)

    # Calculate accuracy
    accuracy = calculate_accuracy(y, y_pred)

    # Create a saver object
    saver = tf.train.Saver()

    with tf.Session() as sess:
        # Initialize all variables
        sess.run(tf.global_variables_initializer())

        for i in range(iterations + 1):
            # Perform training step
            _, train_loss, train_accuracy = sess.run(
                [train_op, loss, accuracy],
                feed_dict={x: X_train, y: Y_train})

            if i % 100 == 0 or i == iterations:
                # Calculate validation loss and accuracy
                valid_loss, valid_accuracy = sess.run(
                    [loss, accuracy],
                    feed_dict={x: X_valid, y: Y_valid})

                # Print the results
                print(f"After {i} iterations:")
                print(f"\tTraining Cost: {train_loss}")
                print(f"\tTraining Accuracy: {train_accuracy}")
                print(f"\tValidation Cost: {valid_loss}")
                print(f"\tValidation Accuracy: {valid_accuracy}")
        # Save the model
        saver.save(sess, save_path)
    return save_path
