
# coding: utf-8

# In[27]:


from sklearn.neighbors import NearestNeighbors
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import neighbors, datasets

n_neighbors=3

X=np.array([[4,3.5],[6,10],[-3,5],[9,7.7],[14,6]])

y = np.array([0, 2, 0, 2, 1])

kn = NearestNeighbors(n_neighbors = 3,algorithm='auto', leaf_size=30)
kn.fit(data)

distances, indices= kn.kneighbors(data,return_distance=True)

print("Indices: \r\n", indices)

print("Distances: \r\n", distances)


h = 0.02 

color_1 = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
color_2= ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

for weights in ['uniform', 'distance']:
    
    knn = neighbors.KNeighborsClassifier(n_neighbors=3, weights=weights)
    knn.fit(X, y)

   
    min_x, max_x = X[:, 0].min() - 1, X[:, 0].max() + 1
    min_y, max_y = X[:, 1].min() - 1, X[:, 1].max() + 1
    
    
    x_test, y_test = np.meshgrid(np.arange(min_x, max_x, h),np.arange(min_y, max_y, h))
    
    pred = knn.predict(np.c_[x_test.ravel(), y_test.ravel()])

    pred = pred.reshape(x_test.shape)
    
    plt.figure()
    
    plt.pcolormesh(x_test, y_test, pred, cmap=color_1)
    
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=color_2, edgecolor='k', s=20)
    plt.xlim(x_test.min(), x_test.max())
    plt.ylim(y_test.min(), y_test.max())
    
    plt.title("Knn classification (k = %i, weights = '%s')" % (n_neighbors, weights))

plt.show()

