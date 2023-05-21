from sklearn.cluster import OPTICS
import numpy as np

# Verinin oluşturulması
X = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [7, 8], [8, 9], [9, 10]])

# OPTICS modelinin oluşturulması
clustering = OPTICS(min_samples=2).fit(X)

# Kümelerin çıktısını almak
print(clustering.labels_)
