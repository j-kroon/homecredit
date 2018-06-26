# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 08:24:58 2018

@author: josep
"""
# numpy and pandas for data manipulation
import numpy as np
import pandas as pd 

# sklearn preprocessing for dealing with categorical variables
from sklearn.preprocessing import LabelEncoder

# File system manangement
import os

# Suppress warnings 
import warnings
warnings.filterwarnings('ignore')

# matplotlib and seaborn for plotting
import matplotlib.pyplot as plt
import seaborn as sns

root_dir = '../homecredit/data/'

print (os.listdir(root_dir))

# load initial data set
app_train = pd.read_csv(root_dir + 'application_train.csv')
print()
print('Training data shape: ', app_train.shape)                 
print()
print(app_train.head())