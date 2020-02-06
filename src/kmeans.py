import numpy as np

if __name__ == "__main__":
    X = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 9]])
    label = np.array([0, 1, 2, 0, 1, 2, 0])
    cluster_center = np.array([[1, 1], [2, 2], [3, 3]])
    p = X[:, :, np.newaxis]
    print(p)
    q = cluster_center.T[np.newaxis, :, :]
    print(q)
    r = (p - q) ** 2
    print(r)
    s = r.sum(axis=1)
    print(s)
