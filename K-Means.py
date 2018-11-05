
# coding: utf-8

# In[4]:


from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt 

data=np.array([[4,3.5],[6,10],[-3,5],[9,7.7],[14,6]])
km_C = KMeans(n_clusters=3, random_state=0)
km_C.fit(data)
labels=km_C.predict(data)
print("\nlabels:",labels)
print("\nCluster Centers(Centroids):\n ",km_C.cluster_centers_)  

clusters = {}
n = 0
for i in labels:
    if i in clusters:
        clusters[i].append(data[n])
    else:
        clusters[i] = [data[n]]
    n +=1
for item in clusters:
    print("\nCluster", item)
    for i in clusters[item]:
        print (i)

plt.scatter(data[:,0],data[:,1], c=km_C.labels_, cmap='rainbow') 

plt.show()

