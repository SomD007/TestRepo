print("hello")
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv("/storage/emulated/0/Advertising.csv")
#df.head()
#print(df)

#print(df.shape)


#print(df.describe())
"""
sns.pairplot(df,x_vars=['TV','Radio','Newspaper'],y_vars='Sales',kind='scatter')

#df['TV'].plot.hist(bins=10)

plt.show()

"""
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train,Y_test=train_test_split(df[['TV']], df[['Sales']], test_size=0.3, random_state=0)
print(X_train)







a=[1,2,3,4,5,6]
arr=np.array(a)
print(arr)