import pandas as pd 
import numpy as np
import prettytable as pt
import matplotlib.pyplot as plt 
import seaborn as sns
def input_data():
    try:
        data= pd.read_excel('./input/test.xlsx')
    except:
        data = pd.read_csv('./input/test.csv')
    return data
def Preprocess(data):
    time=np.unique(data.ix[:,0].values)
    location=np.unique(data.ix[:,0].values)
    #Imputation of missing values
    dropNa=data.dropna()
    imputna=data.fillna(data.mean())
    #get average and standard derivation
    ave=pd.DataFrame(columns=data.columns)
    std=pd.DataFrame(columns=data.columns)
    for i in time:
        for j in location:
            ave=ave.append(data[((data.time==i) & (data.location==j))].mean(),ignore_index=True)
            std=std.append(data[((data.time==i) & (data.location==j))].std(),ignore_index=True)
    del ave['sample']
    del std['sample']
    writer = pd.ExcelWriter('./output/Preprocess.xlsx')
    data.to_excel(writer,'data')
    dropNa=dropNa.to_excel(writer,'dropna')
    imputna=imputna.to_excel(writer,'imputna')
    ave.to_excel(writer,'ave')
    std.to_excel(writer,'std')
    writer.save()
#Pretty table for dataframe and ndarray 
def Print(df):
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


data=input_data()
Preprocess(data)
