# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 06:22:52 2019

@author: urkang
"""

import networkx as nx
import numpy as np
import random_modular_generator_variable_modules as rmg
import sequence_generator as sg

from tqdm import tqdm
np.random.seed(0)

# Enter the network size(N), average network degree (d), total modules in the network (m), and modularity (Q)
N=200
d=6
m=4
Q=0.5

# specify the degree distribution of the graph. In it's current format the code can generate
# four well known degree distribution found in biological networks - scalefree, geometric, poisson and regular distribution
degfunction = sg.regular_sequence

# specify the distribution of module size. The distribution can be scalefree, geometric, poisson and regular distribution (or any aribtrary sequence)
# in it's simplest form speicify module size tp be regular which implies that all modules are of equal size
modfunction = sg.regular_sequence

# --------------------------
net_list = []
net_name = "Q_"+str(Q)+"_"
net_num = 50
path_save = "C:/Users/urkang/Desktop/test_directory/Net_simple_modular/"

for i in tqdm(range(net_num)) :
    temp_graph = rmg.generate_modular_networks(N, degfunction, modfunction, Q, m, d)
    temp_matrix = nx.to_numpy_matrix(temp_graph)
    temp_len = len(temp_matrix)
    for j in range(temp_len) :
        for k in range(temp_len) :
            temp_matrix[j, k] *= np.random.uniform(low=-0.5, high=0.5) # 2D array indexing
    net_list.append(temp_matrix)
    
for i in range(net_num) :
    temp_name = net_name + str(i+1) + ".csv"
#    temp_path = path_save + "Q_" + str(Q) + "/"
    np.savetxt(path_save+temp_name, net_list[i], delimiter=",")