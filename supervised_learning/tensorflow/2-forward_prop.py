#!/usr/bin/env python3
'''Foward propagation'''
create_layer = __import__('1-create_layer').create_layer


def forward_prop(x, layer_sizes=[], activations=[]):
    """
    Creates the forward propagation graph for the neural network
    Args:
    x: placeholder - input data
    layer_sizes: list of integers - 
    number of nodes in each layer of the network
    activations: list of functions - 
    activation functions for each layer of the network
    Returns:
    tensor - the prediction of the network
    """
    # Initialize the input to the first layer as x
    prev_output = x

    # Create each layer in the network using create_layer function
    for i in range(len(layer_sizes)):
        prev_output = create_layer(
            prev_output, layer_sizes[i], activations[i])

    # Return the output of the final layer
    # (the prediction of the network)
    return prev_output
