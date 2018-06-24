import pandas as pd 
import numpy as np
def input_data():
    try:
        data= pd.read_excel('./test.xlsx')
    except:
        data = pd.read_csv('./test.csv')
    time=np.unique(data.ix[:,0].values)
    location=np.unique(data.ix[:,0].values)
    for i in time:
        for j in location:
            ave=data[((data.time==i) & (data.location==j))].mean()
            std=data[((data.time==i) & (data.location==j))].std()
    return data,time,ave,std
print(input_data())
