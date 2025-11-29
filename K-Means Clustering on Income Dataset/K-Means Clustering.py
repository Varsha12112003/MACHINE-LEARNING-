
# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
# %matplotlib inline

df=pd.read_csv("/content/income.csv")
df

km=KMeans(n_clusters=3)
y_pred=km.fit_predict(df[["Age","Income($)"]])
y_pred

df["cluster"]=y_pred
df.head()

df0=df[df.cluster==0]
df1=df[df.cluster==1]
df2=df[df.cluster==2]
plt.scatter(df0["Age"],df0["Income($)"],color="green")
plt.scatter(df1["Age"],df1["Income($)"],color="red")
plt.scatter(df2["Age"],df2["Income($)"],color="black")

from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler()
scaler.fit_transform(df[["Income($)"]])
df["Income($)"]=scaler.transform(df[["Income($)"]])
df

km=KMeans(n_clusters=3)
y_pred=km.fit_predict(df[["Age","Income($)"]])
y_pred

df['cluster']=y_pred
df.head()

df0=df[df.cluster==0]
df1=df[df.cluster==1]
df2=df[df.cluster==2]
plt.scatter(df0.Age,df0['Income($)'],color='red')
plt.scatter(df1.Age,df1['Income($)'],color='green')
plt.scatter(df2.Age,df2['Income($)'],color='blue')

from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler()
scaler.fit_transform(df[['Income($)']])
df['Income($)']=scaler.fit_transform(df[['Income($)']])
df.head()

scaler.fit_transform(df[['Age']])
df['Age']=scaler.fit_transform(df[['Age']])
df.head()

"""km=KMeans(n_clusters=3)
y_pred=km.fit_predict(df[['Age','Income($)']])
y_pred
"""
# Apply K-Means
km = KMeans(n_clusters=3, random_state=42)
df['cluster'] = km.fit_predict(df[['Age', 'Income($)']])

df

df0=df[df.cluster==0]
df1=df[df.cluster==1]
df2=df[df.cluster==2]
plt.scatter(df0['Age'],df0['Income($)'],color='red')
plt.scatter(df1['Age'],df1['Income($)'],color='green')
plt.scatter(df2['Age'],df2['Income($)'],color='blue')
plt.scatter(df0['Age'], df0['Income($)'], color='red',label='Cluster 0')