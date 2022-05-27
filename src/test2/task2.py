import random

import numpy
import numpy as np
from PIL import Image
from numpy.random import uniform


# function is defined in SciPy?
def euclidean(point, data):
    return np.sqrt(np.sum((point - data) ** 2, axis=1))


class KMeans:
    def __init__(self, n_clusters=2, max_iter=100):
        self.n_clusters = n_clusters
        self.max_iter = max_iter

    def fit(self, X: numpy.array):
        self.centroids = [random.choice(X)]
        for _ in range(self.n_clusters - 1):
            dists = np.sum([euclidean(centroid, X) for centroid in self.centroids], axis=0)
            dists /= np.sum(dists)
            (new_centroid_idx,) = np.random.choice(range(len(X)), size=1, p=dists)
            self.centroids += [X[new_centroid_idx]]
        iteration = 0
        prev_centroids = None
        while np.not_equal(self.centroids, prev_centroids).any() and iteration < self.max_iter:
            sorted_points = [[] for _ in range(self.n_clusters)]
            for point in X:
                dists = euclidean(point, self.centroids)
                centroid_idx = np.argmin(dists)
                sorted_points[centroid_idx].append(point)
            prev_centroids = self.centroids
            self.centroids = [np.mean(cluster, axis=0) for cluster in sorted_points]
            for i, centroid in enumerate(self.centroids):
                if np.isnan(centroid).any():
                    self.centroids[i] = prev_centroids[i]
            iteration += 1

    def predict(self, X: numpy.array):
        centroids = []
        centroid_idxs = []
        for x in X:
            dists = euclidean(x, self.centroids)
            centroid_idx = np.argmin(dists)
            centroids.append(self.centroids[centroid_idx])
            centroid_idxs.append(centroid_idx)
        return np.array([i for i in centroid_idxs])


with Image.open("img.png") as img:
    width, height = img.size
    pixels = np.array([(i % width, i // width) + c for i, c in enumerate(list(img.getdata()))])
    model = KMeans(30, 100)
    model.fit(pixels)
    prediction = model.predict(pixels)
    image_pixels = img.load()
    for i in range(len(pixels)):
        image_pixels[pixels[i][0], pixels[i][1]] = tuple(int(x) for x in model.centroids[prediction[i]][2:])
    img.save("processed.png")
