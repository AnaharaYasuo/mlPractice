import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

if __name__ == "__main__":
    x=np.linspace(-5,5)
    y=norm.pdf(x)
    plt.plot(x,y,color="r")
    plt.show()
    
