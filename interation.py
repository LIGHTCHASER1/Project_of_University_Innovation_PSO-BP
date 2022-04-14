# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 18:22:05 2021

@author: LIGHT CHASER
"""
import try1
import numpy as np
import matplotlib.pyplot as plt
print(list(range(1,len(try1.ff)+1)))
print(try1.ff)
a = np.arange(1,len(try1.ff)+1,1)
plt.plot(a,try1.ff)
print(try1.k-1)
plt.show()