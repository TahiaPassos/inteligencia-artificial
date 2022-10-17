# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 20:15:02 2022
@author: lab56
"""

from __future__ import division
from linear_algebra import dot

def degrau(x): 
    return 1 if x >= 0 else 0

def saida_perceptron(pesos, entradas):
    y = dot(pesos, entradas)
    return degrau(y)

def ajustes(sinapses, entradas, saida):
    
    taxa_aprendizagem = 0.12
    
    saida_parcial = saida_perceptron(sinapses, entradas)
    
    for j in range(3):
        sinapses[j] = sinapses[j] + taxa_aprendizagem * (saida[0] - saida_parcial) * entradas[j]
    
    saida = saida_parcial
    return sinapses, saida

def teste_generalizacao(sinapses, entradas, saida):
    saida_parcial = saida_perceptron(sinapses, entradas)
    saida = saida_parcial
    return sinapses, saida

neuronio = [0.22, -0.33, 0.44]
padrao_0_0 = [-1, 0.87, 0.76]
padrao_0_1 = [-1, 0.77, 0.6]
padrao_0_2 = [-1, 0.85, 0.71]
padrao_0_3 = [-1, 0.84, 0.69]
padrao_0_4 = [-1, 0.94, 0.89]
padrao_0_5 = [-1, 0.875, 0.76]
padrao_0_6 = [-1, 0.96, 0.92]
padrao_0_7 = [-1, 0.83, 0.68]
padrao_0_8 = [-1, 0.845, 0.69]
padrao_0_9 = [-1, 0.925, 0.85]


padrao_1_0 = [-1, 0.8, 0.65]
padrao_1_1 = [-1, 0.91, 0.83]
padrao_1_2 = [-1, 0.89, 0.8]
padrao_1_3 = [-1, 0.835, 0.71]
padrao_1_4 = [-1, 0.92, 0.88]
padrao_1_5 = [-1, 0.845, 0.72]
padrao_1_6 = [-1, 0.955, 0.92]
padrao_1_7 = [-1, 0.825, 0.69]
padrao_1_8 = [-1, 0.99, 0.99]
padrao_1_9 = [-1, 0.92, 0.85]



saida0 = [0]
saida1 = [1]

n = 0

for  _ in range(30):
    neuronio, saida_0 = ajustes(neuronio, padrao_0_0, saida0)
    print (neuronio, "saida0 =", saida_0)    
    neuronio, saida_0 = ajustes(neuronio, padrao_0_1, saida0)
    print (neuronio, "saida0 =", saida_0)  
    neuronio, saida_0 = ajustes(neuronio, padrao_0_2, saida0)
    print (neuronio, "saida0  =", saida_0)  
    neuronio, saida_0 = ajustes(neuronio, padrao_0_3, saida0)
    print (neuronio, "saida0  =", saida_0)  
    neuronio, saida_0 = ajustes(neuronio, padrao_0_4, saida0)
    print (neuronio, "saida0  =", saida_0)  
    neuronio, saida_0 = ajustes(neuronio, padrao_0_5, saida0)
    print (neuronio, "saida0  =", saida_0)    
    neuronio, saida_0 = ajustes(neuronio, padrao_0_6, saida0)
    print (neuronio, "saida0  =", saida_0)    
    neuronio, saida_0 = ajustes(neuronio, padrao_0_7, saida0)
    print (neuronio, "saida0  =", saida_0)    
    neuronio, saida_0 = ajustes(neuronio, padrao_0_8, saida0)
    print (neuronio, "saida0  =", saida_0) 
    neuronio, saida_0 = ajustes(neuronio, padrao_0_9, saida0)
    print (neuronio, "saida0  =", saida_0)        
    
    
    neuronio, saida_1 = ajustes(neuronio, padrao_1_0, saida1)
    print (neuronio, "saida1 =", saida_1)  
    neuronio, saida_1 = ajustes(neuronio, padrao_1_1, saida1)
    print (neuronio, "saida1 =", saida_1)  
    neuronio, saida_1 = ajustes(neuronio, padrao_1_2, saida1)
    print (neuronio, "saida1 =", saida_1) 
    neuronio, saida_1 = ajustes(neuronio, padrao_1_3, saida1)
    print (neuronio, "saida1 =", saida_1) 
    neuronio, saida_1 = ajustes(neuronio, padrao_1_4, saida1)
    print (neuronio, "saida1 =", saida_1) 
    neuronio, saida_1 = ajustes(neuronio, padrao_1_5, saida1)
    print (neuronio, "saida1 =", saida_1) 
    neuronio, saida_1 = ajustes(neuronio, padrao_1_6, saida1)
    print (neuronio, "saida1 =", saida_1)
    neuronio, saida_1 = ajustes(neuronio, padrao_1_7, saida1)
    print (neuronio, "saida1 =", saida_1)   
    neuronio, saida_1 = ajustes(neuronio, padrao_1_8, saida1)
    print (neuronio, "saida1 =", saida_1) 
    neuronio, saida_1 = ajustes(neuronio, padrao_1_9, saida1)
    print (neuronio, "saida1 =", saida_1) 
    
    
        
    n = n + 1;
    print("número de ciclos = ", n)

#teste de generalização
padrao_teste_0 = [-1, 0.2, 0.4]
padrao_teste_1 = [-1, 0.7, 0.8]
padrao_teste_2 = [-1, 0.6, 0.3]
padrao_teste_3 = [-1, 0.1, 0.9]
padrao_teste_4 = [-1, 0.2, 0.6]
padrao_teste_5 = [-1, 0.8, 0.1]

print("teste de generalização")
neuronio, saida_0 = teste_generalizacao(neuronio, padrao_teste_0, saida0)
print (neuronio, "saida0 =", saida_0)  
neuronio, saida_1 = teste_generalizacao(neuronio, padrao_teste_1, saida1)
print (neuronio, "saida1 =", saida_0)  
neuronio, saida_0 = teste_generalizacao(neuronio, padrao_teste_2, saida0)
print (neuronio, "saida0 =", saida_0)  
neuronio, saida_1 = teste_generalizacao(neuronio, padrao_teste_3, saida1)
print (neuronio, "saida1 =", saida_0)  
neuronio, saida_0 = teste_generalizacao(neuronio, padrao_teste_4, saida0)
print (neuronio, "saida0 =", saida_0)  
neuronio, saida_0 = teste_generalizacao(neuronio, padrao_teste_5, saida1)
print (neuronio, "saida1 =", saida_0)  