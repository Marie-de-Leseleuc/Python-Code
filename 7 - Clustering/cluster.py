import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from sklearn import datasets

from sklearn import metrics

np.random.seed(5)

centers = [[1, 1], [-1, -1], [1, -1]]
iris = datasets.load_iris()
X = iris.data
y = iris.target
cluster_numba = 3
showdata ="yes"
#http://scikit-learn.org/stable/modules/clustering.html



def cluster_data(estimators):
	fignum = 1
	for name, est in estimators.items():
	    fig = plt.figure(fignum, figsize=(4, 3))
	    plt.clf()
	    ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)

	    plt.cla()
	    est.fit(X)
	    labels = est.labels_
	    # variance = np.var(labels)
	    # mean = np.mean(labels)
	    # weight = mean/variance


	    try:
	    	score = metrics.silhouette_score(X, labels, metric='jaccard')
	    except:
	    	print("no score for this number of cluster...")
	    print("precision score: ",score)

	    ax.scatter(X[:, 3], X[:, 0], X[:, 2], c=labels.astype(np.float))

	    ax.w_xaxis.set_ticklabels([])
	    ax.w_yaxis.set_ticklabels([])
	    ax.w_zaxis.set_ticklabels([])
	    ax.set_xlabel('Petal width')
	    ax.set_ylabel('Sepal length')
	    ax.set_zlabel('Petal length')
	    fignum = fignum + 1



## Uncoment one of the methods :)

#Kmean
from sklearn.cluster import KMeans
estimators = {'k_means_iris_1': KMeans(n_clusters=cluster_numba)}
cluster_data(estimators)


# Mean shift (density kernel)
# from sklearn.cluster import MeanShift, estimate_bandwidth
# bandwidth = estimate_bandwidth(X, quantile=0.5, n_samples=100)
# estimators = {'MeanShift_iris_1': MeanShift(bandwidth=bandwidth, bin_seeding=True)}
# cluster_data(estimators)

# #Hierarchical
# from sklearn.cluster import AgglomerativeClustering
# # methods : 'ward', 'average', 'complete'
# # Which linkage criterion to use. The linkage criterion determines which distance to use between sets of observation. 
# #The algorithm will merge the pairs of cluster that minimize this criterion.

# 	# ward minimizes the variance of the clusters being merged.
# 	# average uses the average of the distances of each observation of the n sets.
# 	# complete or maximum linkage uses the maximum distances between all observations of the n sets.
# estimators = {'Hierarchical_iris_1': AgglomerativeClustering(linkage='ward',n_clusters=3)}
# cluster_data(estimators)





# Plot the ground truth
# fignum = 1
# fig = plt.figure(fignum, figsize=(4, 3))
# plt.clf()
# ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)

# plt.cla()

# for name, label in [('Setosa', 0),
#                     ('Versicolour', 1),
#                     ('Virginica', 2)]:
#     ax.text3D(X[y == label, 3].mean(),
#               X[y == label, 0].mean() + 1.5,
#               X[y == label, 2].mean(), name,
#               horizontalalignment='center',
#               bbox=dict(alpha=.5, edgecolor='w', facecolor='w'))
# # Reorder the labels to have colors matching the cluster results
# y = np.choose(y, [1, 2, 0]).astype(np.float)
# ax.scatter(X[:, 3], X[:, 0], X[:, 2], c=y)

# ax.w_xaxis.set_ticklabels([])
# ax.w_yaxis.set_ticklabels([])
# ax.w_zaxis.set_ticklabels([])
# ax.set_xlabel('Petal width')
# ax.set_ylabel('Sepal length')
# ax.set_zlabel('Petal length')

if showdata=="yes":
	plt.show()


