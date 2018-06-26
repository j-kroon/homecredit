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

target_distr = app_train['TARGET'].value_counts()
print
print(target_distr)
app_train['TARGET'].astype(int).plot.hist();

# Function to calculate missing vlaues by column 
def missing_values_table(df):
    # total missing values
    mis_val = df.isnull().sum()
    
    #percent of missing values
    mis_val_percent = 100 * mis_val / len(df)
    
    # make a table with results
    mis_val_table = pd.concat([mis_val, mis_val_percent], axis=1)
    
    # rename the columns
    mis_val_table_ren_columns = mis_val_table.rename(
            columns = {0: 'Missing Values', 1: '% of Total Values'})
    
    # Sort the table by percentage of missing descending
    mis_val_table_ren_columns = mis_val_table_ren_columns[
            mis_val_table_ren_columns.iloc[:,1] !=0].sort_values(
            '% of Total Values', ascending=False).round(1)
    
    # print some summary information
    print ("Your selected dataframe has " + str(df.shape[1]) +" columns.\n"
           
           "There are " + str(mis_val_table_ren_columns.shape[0]) +
           " columns that have missing values.")
    
    # Return the dataframe with missing information
    return mis_val_table_ren_columns

# Missing values stats
missing_values = missing_values_table(app_train)

mis_val_hd = missing_values.head(20)
print(mis_val_hd)