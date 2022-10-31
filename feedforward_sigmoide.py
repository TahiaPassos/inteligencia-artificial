# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 20:17:57 2022

@author: lab56
"""

from linear_algebra import dot
import math

def sigmoid(t): 
    return 1 / (1 + math.exp(-t))

def neuron_output(weights, inputs):
    return sigmoid(dot(weights, inputs))

def feed_forward(neural_network, input_vector):
    
    outputs = []
    
    for layer in neural_network:
        
        input_with_bias = input_vector + [1]
        output = [neuron_output(neuron, input_with_bias)
                  for neuron in layer]
        outputs.append(output)
        
        input_vector = output
    
    return outputs

xor_network = [
                [[20, 20, -30],
                [20, 20, -10]],
                
                [[-60, 60, -30]]]

for x in [0, 1]:
    for y in [0, 1]:
        print(x, y, feed_forward(xor_network, [x,y])[-1])
        