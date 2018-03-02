#from pandas_datareader.data import DataReader
import pandas_datareader.data as pd
#from datetime import date
import datetime
from matplotlib.pyplot import *
import matplotlib.pyplot as plt

start = datetime.datetime(1968,1,1)
end = datetime.datetime(2018,1,11)

gold = pd.DataReader('GOLDAMGBD228NLBM','fred',start,end)

#print(gold)

plt.plot(gold)
plt.show()