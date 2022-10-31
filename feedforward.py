# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 19:56:21 2022

@author: lab56
"""

from __future__ import division
from collections import Counter
from functools import partial
from linear_algebra import dot
import math, random

def step_function(x): 
    return 1 if x >= 0 else 0

def neuron_output(weights, inputs):
    calculation = dot(weights, inputs)
    return step_function(calculation)

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
                [[1, 1, -1.5],
                [1, 1, -0.5]],
                
                [[-2, 1, -0.5]]]

for x in [0,1]:
    for y in [0,1]:
        print(x, "EXCLUSIVO", y, " = ", feed_forward(xor_network, [x,y])[-1])
        
        
        
        
    