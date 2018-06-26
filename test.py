# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 08:24:58 2018

@author: josep
"""
import numpy as np
import pandas as pd
import seaborn as sn

greeting = "Hello, STL Dawgs!"
hashtag = '#kagglegaggle'

print(greeting)
print(hashtag)

x = np.arange(0,50)
x = pd.DataFrame({'x':x})

# just random uniform distributions in differnt range

y1 = np.random.uniform(10,15,10)
y2 = np.random.uniform(20,25,10)
y3 = np.random.uniform(0,5,10)
y4 = np.random.uniform(30,32,10)
y5 = np.random.uniform(13,17,10)

y = np.concatenate((y1,y2,y3,y4,y5))
y = y[:,None]

sn.regplot(x=x, y=y, fit_reg=False)
