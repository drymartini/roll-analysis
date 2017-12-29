# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 10:00:04 2017

@author: marti
"""

import os
import numpy as np
import pandas as pd

from pandas import Series, DataFrame

import matplotlib.pyplot as plt
from pylab import rcParams
import seaborn as sns

os.chdir("C:\\work\\School\\research\\research-2017-2018\\python-practice\\date-table")

# Read in table
attDF = pd.read_csv("7210-attendance-2017.csv", sep=',')
attDF.head()


attDF['Timestamp'] = pd.to_datetime(attDF['Timestamp'])

# comment in master.


