import numpy as np


class Dice:

    def __init__(self, random_seed=None):
        self.random_state_ = np.random.RandomState(random_seed)
        self.sum_ = 0

    def throw(self):
        self.sum_ += self.random_state_.randint(1, 7)
    
    def get_sum(self):
        return self.sum_

    
if __name__ == "__main__":
    d1 = Dice(123)
    for _ in range(10):
        d1.throw()
    print(d1.get_sum())
    
    d2 = Dice(123)
    for _ in range(10):
        d2.throw()
    print(d2.get_sum())
    
    d1 = Dice(123)
    d2 = Dice(123)
    for _ in range(10):
        d1.throw()
        d2.throw()
    print(d1.get_sum())
    print(d2.get_sum())
