import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    x = np.linspace(-5, 5, 300)
    sin_x = np.sin(x)
    cos_x = np.cos(x)
    
    flg, aexs = plt.subplots(2, 1)
    aexs[0].set_ylim([-1.5,1.5])
    aexs[1].set_ylim([-1.5,1.5])
    aexs[0].plot(x,sin_x,color="r")    
    aexs[1].plot(x,cos_x,color="k")
    
    plt.show()