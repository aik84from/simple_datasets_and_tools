import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA


class SimpleClustering:
    def run(self, data, n_clusters):
        kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(data)
        data_t = PCA(n_components=2).fit_transform(data)
        plt.scatter(data_t[:, 0], data_t[:, 1], c=kmeans.labels_)
        plt.show()
        return kmeans.labels_

