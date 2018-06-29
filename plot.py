import matplotlib.pyplot as plt 
import seaborn as sns
#plot heatmap
def Heatmap(self):
    fig = plt.figure()
    ax = plt.subplot(111)
    sns.heatmap(self,ax=ax,cmap=plt.cm.coolwarm,alpha=0.85,xticklabels=list(self.columns),yticklabels=list(self.columns),linewidths=.1,square=True)
    plt.show()
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
