import numpy as np


class Tracker:
    def __init__(self, name):
        self.name = name
        self.data = []

    def append(self, datum):
        self.data.append(datum)

    def stats(self):
        return {
            'mean': np.mean([d.elapsed for d in self.data]),
            'sd': np.std([d.elapsed for d in self.data]),
            'n': len(self.data)
        }
