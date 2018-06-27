import pandas as pd 
import numpy as np
import prettytable as pt
import matplotlib.pyplot as plt 
import seaborn as sns
def Heatmap(self):
    fig = plt.figure()
    ax = plt.subplot(111)
    sns.heatmap(self,ax=ax,cmap=plt.cm.coolwarm,alpha=0.85,xticklabels=list(self.columns),yticklabels=list(self.columns),linewidths=.1,square=True)
    plt.show()
def input_data():
    try:
        data= pd.read_excel('./test.xlsx')
    except:
        data = pd.read_csv('./test.csv')
    time=np.unique(data.ix[:,0].values)
    location=np.unique(data.ix[:,0].values)
    #Imputation of missing values
    DropNa=data.dropna()
    imputmissing=data.fillna(data.mean())
    #get average and standard derivation
    ave=pd.DataFrame(columns=data.columns)
    std=pd.DataFrame(columns=data.columns)
    for i in time:
        for j in location:
            ave=ave.append(data[((data.time==i) & (data.location==j))].mean(),ignore_index=True)
            std=std.append(data[((data.time==i) & (data.location==j))].std(),ignore_index=True)
    del ave['sample']
    del std['sample']
    return data,time,ave,std
#Pretty table for dataframe and ndarray 
def Prettytable_DF(df):
    try:
        table = pt.PrettyTable([''] + list(df.columns))
        for row in df.itertuples():
            table.add_row(row)
        return str(table)
    except:
        table = pt.PrettyTable()
        for row in df:
            table.add_row(row)
        return str(table)
#plot histogram
def Histogram(self):
    for i in range(0,len(self.columns)):
         x=self.iloc[:,i]
         x.plot(kind='bar',title="Histogram of %s"%self.columns[i])
         plt.show()

#plot line chart
def LineChart(self):
    a=0
    for i in range(0,len(self.columns)):
        x=self.iloc[:,i].unstack(level=-1)
        x.plot(kind='line',title="LineChart of %s"%self.columns[i])
        a=a+1
    plt.show()

Histogram(input_data()[2])
