import numpy as np


class Dice:

    def __init__(self):
        np.random.seed(0)
        self.sum_ = 0

    def throw(self):
        self.sum_ += np.random.randint(1, 7)
    
    def get_sum(self):
        return self.sum_

    
if __name__ == "__main__":
    d1 = Dice()
    for _ in range(10):
        d1.throw()
    print(d1.get_sum())
    
    d2 = Dice()
    for _ in range(10):
        d2.throw()
    print(d2.get_sum())
    
    d1 = Dice()
    d2 = Dice()
    for _ in range(10):
        d1.throw()
        d2.throw()
    print(d1.get_sum())
    print(d2.get_sum())
