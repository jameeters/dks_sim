import numpy as np
from Person import Person


class Door:
    def __init__(self, lam, time):
        self.lam = lam
        # The number of people entering per 10-second interval
        self.vals = np.random.poisson(lam=self.lam, size=time)
        # Create a person object for each entry, with a tin_door randomly chosen within the interval.
        self.entries = []
        for i, v in enumerate(self.vals):
            intv_start = i * 10
            for e in range(v):
                self.entries.append(Person(intv_start + np.random.randint(0, 10)))

    def walkin(self):
        for person in self.entries:
            yield person
