import pandas as pd 
import numpy as np
import prettytable as pt
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

    return data,ave,std
def Prettytable_DF(df=pd.DataFrame()):
    table = pt.PrettyTable([''] + list(df.columns))
    for row in df.itertuples():
        table.add_row(row)
    return str(table)
def Prettytable_ND(ndarray=np.array([])):
    table = pt.PrettyTable()
    for row in ndarray:
        table.add_row(row)
    return str(table)
    for i in range(row_number):
        table.add_row(dataframe.iloc[i,:].values)
    print(table)
print(Prettytable_DF(input_data))
