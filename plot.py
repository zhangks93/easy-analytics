import matplotlib.pyplot as plt 
import seaborn as sns
def Heatmap(self):
    sns.heatmap(self,cmap=plt.cm.coolwarm,alpha=0.85,xticklabels=list(self.columns),yticklabels=list(self.columns),linewidths=.1,square=True)
    
