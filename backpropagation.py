# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from __future__ import division
from collections import Counter
from functools import partial
from linear_algebra import dot
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math
import math, random

def sigmoid(t): 
    return ((2 / (1 + math.exp(-t)))-1)

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

alpha = 0.08
def backpropagate(network, input_vector, target):
    hidden_outputs, outputs = feed_forward(network, input_vector)
    output_deltas = [0.5 * (1 + output) * (1 - output) * (output - target[i]) * alpha
                     for i, output in enumerate(outputs)]
    
    for i, output_neuron in enumerate(network[-1]):
        for j, hidden_output in enumerate(hidden_outputs + [1]):
            output_neuron[j] -= output_deltas[i] * hidden_output
            
    hidden_deltas = [0.5 * alpha * (1 + hidden_output) * (1 - hidden_output) *
                     dot(output_deltas, [n[i] for n in network[-1]])
                     for i, hidden_output in enumerate(hidden_outputs)]
    
    for i, hidden_neuron in enumerate(network[0]):
        for j, input in enumerate(input_vector + [1]):
            hidden_neuron[j] -= hidden_deltas[i] * input
            
def seno(x):
        seno = [(math.sin(math.pi/180*x)*math.sin(2*math.pi/180*x))]
        return [seno]
def predict(inputs):
    return feed_forward(network, inputs)[-1]

input = []
targets = []
for x in range(360):
    seno_a = seno(x)
    
#TREINAMENTO REDE NEURAL

random.seed(0)
input_size = 1
num_hidden = 6
output_size = 1


hidden_layer = [[random.random() for __ in range(input_size + 1)]
                 for __ in range(num_hidden)]
    
output_layer = [[random.random() for __ in range(num_hidden + 1)]
                 for __ in range(output_size)]

network = [hidden_layer, output_layer]

for __ in range(300):
    for x in range(360):
        inputs = seno(x)
        targets = seno(x)
        for input_vector, target_vector in zip(inputs, targets):
            backpropagate(network, input_vector, target_vector)
            
#formatação do gráfico
fig, ax = plt.subplots()
ax.set(xlabel='ângulo (º)', ylabel='função sen(x)*sen(2x)',
title='Aproximação Funcional')
ax.grid()
t = np.arange(0, 360, 1)

#teste da rede através de predict( )
saida = []
for x in range(360):
    inputs = seno(x)
    targets = seno(x)
    for input_vector, target_vector in zip(inputs, targets):
        sinal_saida = predict(input_vector)
        saida.extend(sinal_saida)

entrada = []
for x in range(360):
    entrada += seno(x)
ax.plot(t, entrada)
ax.plot(t, saida)
plt.show()

print ("camada entrada", hidden_layer)
print ("camada saída", output_layer)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    