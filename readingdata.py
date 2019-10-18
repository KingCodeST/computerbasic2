import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df =pd.read_csv("tempdata.csv")


temperature =df['temperature']

datetime =df['date_time']


plt.scatter(temperature,datetime, edgecolors ='r')
plt.xlabel('temperature(Deg.C)')
plt.ylabel('datetime([YYYYMMDDHHMMSS])')
plt.title(' Sea Surface Temperature timeseries for an undisclosed location in the ocean.')

