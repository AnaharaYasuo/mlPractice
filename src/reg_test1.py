import linearreg
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

if __name__ == "__main__":
    n = 100
    scale = 10
    np.random.seed(0)
    X = np.random.random((n, 2)) * scale
    w0 = 1
    w1 = 2
    w2 = 3
    y = w0 + w1 * X[:, 0] + w2 * X[:, 1] + np.random.randn(n)

    model = linearreg.LinerRegression()
    model.fit(X, y)
    print("係数:", model.w_)
    print("(1,1)への予測値:", model.predict(np.array([1, 1])))
    
    xmesh, ymesh = np.meshgrid(np.linspace(0, scale, 20), np.linspace(0, scale, 20))
    zmesh = (model.w_[0] + model.w_[1] * xmesh.ravel() + model.w_[2] * ymesh.ravel()).reshape(xmesh.shape)
    flg = plt.figure()
    ax = flg.add_subplot(111, projection="3d")
    ax.scatter(X[:, 0], X[:, 1], y, color="k")
    ax.plot_wireframe(xmesh, ymesh, zmesh, color="r")
    plt.show()
