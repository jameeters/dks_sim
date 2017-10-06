import numpy as np


class Door:
    def __init__(self, lam, time):
        self.lam = lam
        self.vals = np.random.poisson(lam=self.lam, size=time)

    def walkin(self):
        for n in self.vals:
            yield n


