import numpy as np
import matplotlib.pyplot as plt 


def cointoss(n, m):
    res = []
    for _ in range(m):
        res.append(np.random.randint(2, size=n).sum())
    return res


if __name__ == "__main__":
    np.random.seed(0)
    flg, axes = plt.subplots(1, 2)
    res = cointoss(100, 1000000)
    axes[0].hist(res, range=(30, 70), bins=50, color="k")
    res = cointoss(10000, 1000000)
    axes[1].hist(res, range=(4800, 5200), bins=50, color="k")
    # plt.plot(res)
    # plt.hist(res)
    plt.show()
    
