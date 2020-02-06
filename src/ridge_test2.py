import ridge
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from numpy import linspace
import linearreg

if __name__ == "__main__":
    x = np.arange(12)
    y = 1 + 2 * x
    y[2] = 20
    y[4] = 0
    xmin, xmax, ymin, ymax = 0, 12, -1, 25
    flg, axes = plt.subplots(nrows=2, ncols=5)
    for i in range(5):
        xx = x[:2 * (i + 1)]
        yy = y[:2 * (i + 1)]

        model = linearreg.LinerRegression()
        model.fit(xx, yy)
        xs = [xmin, xmax]
        ys = [model.w_[0] + model.w_[1] * xmin, model.w_[0] + model.w_[1] * xmax]
        axes[0, i].set_xlim([xmin, xmax])
        axes[0, i].set_ylim([ymin, ymax])
        axes[0, i].scatter(xx, yy, color="k")
        axes[0, i].plot(xs, ys, color="k")
        
        model = ridge.RidgeRegression(10.)
        model.fit(xx, yy)
        xs = [xmin, xmax]
        ys = [model.w_[0] + model.w_[1] * xmin, model.w_[0] + model.w_[1] * xmax]
        axes[1, i].set_xlim([xmin, xmax])
        axes[1, i].set_ylim([ymin, ymax])
        axes[1, i].scatter(xx, yy, color="k")
        axes[1, i].plot(xs, ys, color="k")

    plt.show()
