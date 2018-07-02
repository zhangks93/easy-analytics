import pandas as pd 
import numpy as np
import prettytable as pt
import matplotlib.pyplot as plt 
import seaborn as sns
from sklearn.decomposition import FastICA,PCA
import statsmodels.api as sm
def input_data():
    try:
        data= pd.read_excel('./input/test1.xlsx')
    except:
        data = pd.read_csv('./input/test.csv')
    return data
def Preprocess(data):
    time=np.unique(data.ix[:,0].values)
    location=np.unique(data.ix[:,1].values)
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
    data.to_excel(writer,'data',float_format='%.01f')
    dropNa=dropNa.to_excel(writer,'dropna',float_format='%.01f')
    imputna=imputna.to_excel(writer,'imputna',float_format='%.01f')
    ave.to_excel(writer,'ave',float_format='%.01f')
    std.to_excel(writer,'std',float_format='%.01f')
    writer.save()
    return ave
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
def Description(self):
    self=pd.DataFrame(self.ix[:,3:].values,index=[list(data.ix[:,0].values),list(data.ix[:,1].values)])
    plt.figure()
    self.plot()
    plt.savefig('./output/description/line.png',dpi=1000,bbox_inches='tight')
    plt.figure()
    self.plot.bar()
    plt.savefig('./output/description/bar.png',dpi=1000,bbox_inches='tight')
    plt.figure()
    self.plot.barh()
    plt.savefig('./output/description/barh.png',dpi=1000,bbox_inches='tight')
    plt.figure()
    self.plot.box()
    plt.savefig('./output/description/box.png',dpi=1000,bbox_inches='tight')

def IndependentComponentAnalysis(self,n):
    ica = FastICA(n_components=n)
    de=ica.fit_transform(self.values)
    return ica.mixing_,de
def LinerRegression(self,a,b,c):
    x=self.ix[:,a:b]
    X=sm.add_constant(x)
    Y=self.ix[:,c]
    print(x.columns.values,Y.name)
    model = sm.OLS(Y, X)
    results = model.fit()
    print(results.summary())
    if ((b-a)==1):
        plt.scatter(x, Y, alpha=0.3) 
        X_prime=np.linspace(x.min(), x.max(),100)[:,np.newaxis]
        X_prime=sm.add_constant(X_prime)
        y_hat=results .predict(X_prime)
        plt.plot(X_prime[:,1], y_hat, 'r', alpha=0.9) 
        plt.xlabel(x.columns.values[0])
        plt.ylabel(Y.name)
        plt.show()
data=input_data()
data=Preprocess(data)
for i in range(8,9):
     LinerRegression(data.ix[:,2:],0,1,i)
