import matplotlib.pyplot as plt  
from matplotlib import style 
from sklearn.cluster import KMeans 
from sklearn.datasets.samples_generator import make_blobs 
  
style.use("fivethirtyeight") 
  
# make_blobs() is used to generate sample points 
# around c centers (randomly chosen) 
X, y = make_blobs(n_samples = 500, centers = 4,  cluster_std = 1, n_features = 2) 
                  
plt.scatter(X[:, 0], X[:, 1], s = 30, color ='b') 
  
# label the axes 
plt.xlabel('X') 
plt.ylabel('Y') 
  
plt.show() 
plt.clf() # clear the figure 

cost =[] 
for i in range(1, 11): 
    KM = KMeans(n_clusters = i, max_iter = 500) 
    KM.fit(X) 
      
    # calculates squared error 
    # for the clustered points 
    cost.append(KM.inertia_)      
  
# plot the cost against K values 
plt.plot(range(1,11), cost, color ='g', linewidth ='3') 
plt.xlabel("Value of K") 
plt.ylabel("Sqaured Error (Cost)") 
plt.show() # clear the plot 
  
# the point of the elbow is the  
# most optimal value for choosing k 