import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns


# Load dataset
customer_data=pd.read_csv("Mall_Customers.csv")


print("null value under each column")
print(customer_data.isnull().sum())

x =customer_data.iloc[:,[3,4]].values
print(x)

wcss = [] #to find no.of clusters

for i in range(1,11):
    kmeans = KMeans(n_clusters=i,init='k-means++',random_state=42)
    kmeans.fit(x)
    
    wcss.append(kmeans.inertia_)
    
#Elbow Graph
sns.set()
sns.set()
plt.plot(range(1,11),wcss)
plt.title("The Elbow Point Graph")
plt.xlabel("Number of Clusters")
plt.ylabel("wcss")
plt.show()

clusters = 5

kmeans = KMeans(n_clusters=5,init='k-means++',random_state=0)
y = kmeans.fit_predict(x)

print(y)

clusters = 0,1,2,3,4

plt.figure(figsize=(8,8))
plt.scatter(x[y==0,0],x[y==0,1],s=50,c='blue',label='Cluster 1')
plt.scatter(x[y==1,0],x[y==1,1],s=50,c='green',label='Cluster 2')
plt.scatter(x[y==2,0],x[y==2,1],s=50,c='pink',label='Cluster 3')
plt.scatter(x[y==3,0],x[y==3,1],s=50,c='black',label='Cluster 4')
plt.scatter(x[y==4,0],x[y==4,1],s=50,c='gray',label='Cluster 5')

#Centroids
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=100,c='red')
plt.title('Customer Group')
plt.xlabel('Annual Income')
plt.show()