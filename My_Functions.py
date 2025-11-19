#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  8 19:31:40 2023
"""
import numpy as np
def vankrevelan(data_array):
    # Estimating species atomic contribution in formulas
    lenspecies = len(data_array)
    data_array = [data_array[i].strip() for i in range(lenspecies)]
    elements = ['C', 'H', 'N', 'O', 'P', 'S']
    element_lists = {elem: [0] * lenspecies for elem in elements}
    for j in range(lenspecies):
        cdata = data_array[j]
        for i in range(len(cdata)):
            if cdata[i].isalpha():
                element = cdata[i]
                num_str = ''
                for k in range(i+1, len(cdata)):
                    if cdata[k].isdigit():
                        num_str += cdata[k]
                    else:
                        break
                if num_str:
                    num = int(num_str)
                else:
                    num = 1
                element_lists[element][j] = num
    return element_lists

###############################################################################
def Oparam(x,y,z1,z2):
    # Step 1: Compute the absolute differences between all pairs
    abs_diff = np.abs(np.subtract.outer(z1,z2))
    # Step 2: Compute the product of all pairs
    product = np.outer(x, y)
    # Step 3: Compute the weighted sum of the absolute differences
    result = np.einsum('ij,ij->', abs_diff, product)
    return result

# def Oparam(x, y, z1, z2):
#     # Ensure that inputs are NumPy arrays, and convert them to avoid unnecessary overhead
#     x = np.asarray(x)
#     y = np.asarray(y)
#     z1 = np.asarray(z1)
#     z2 = np.asarray(z2)
    
#     # Step 1 & 2: Compute the weighted absolute differences directly using broadcasting
#     abs_diff = np.abs(z1[:, None] - z2[None, :])
    
#     # Use broadcasting for multiplication and summation
#     result = np.sum(abs_diff * (x[:, None] * y[None, :]))

#     return result

def selfOparam(x,z):
    N = np.shape(x)[0]
    i, j = np.triu_indices(N, k=1)
    sum_result = np.sum(x[i] * x[j] * np.abs(z[i] - z[j]))    
    return sum_result
###############################################################################

def jaccard_rk(a,b):
    # estimating intersection, i.e. #(1,1)s
    intsc = np.where((a == 1) & (b == 1))
    n_intsc = np.shape(intsc)[1]
    # estimating #(1,0)s
    N10 = np.where((a == 1) & (b == 0))
    n_N10 = np.shape(N10)[1]
    # estimating #(0,1)s
    N01 = np.where((a == 0) & (b == 1))
    n_N01 = np.shape(N01)[1]
    
    return n_intsc/(n_intsc + N10 + N01)
