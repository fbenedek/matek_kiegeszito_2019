#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 22:18:29 2019

@author: fbenedek
"""

import matplotlib.pyplot as plt
import numpy as np
#random értékek az elején
z = np.random.random((256,256))
z = z>0.5

from scipy.signal import convolve

def iterate_game_of_life(board):
    neighbors_kernel = np.ones(shape=(3, 3), dtype='int') #kernel mátrix
    neighbors_kernel[1, 1] = 0
    neighbors_count = convolve(board, neighbors_kernel, mode='same') #konvoúció, szomszédok számának meghatározása - same fontos!
    return(np.logical_or(np.logical_and(board, neighbors_count==2), neighbors_count==3)) #Szabályok alkalmazása


#Innentől ez a megjelenítés, 400-szor fut le a cucc.
for i in range(400):
    
    if i == 0:
        p = plt.imshow(z.astype(float))
        fig = plt.gcf()
        plt.clim()   # clamp the color limits
        plt.title("Boring slide show")
    else:
        z = iterate_game_of_life(z)
        p.set_data(z.astype(float))

    print("step", i)
    plt.pause(0.01)
