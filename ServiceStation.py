import numpy as np

from queue import Queue


class Line:
    def __init__(self, name):
        self.name = name
        self.line = []

    def push(self, person):
        self.line.append(person)

    def pop(self):
        popped = self.line[0]
        self.line = self.line[1:]
        return popped

    def head(self):
        return self.line[0]

    def empty(self):
        return len(self.line) == 0

    def __len__(self):
        return len(self.line)


class ServiceStation:
    def __init__(self, name, mu, sigma, p, nxt=None):
        self.name = name
        self.mu = mu
        self.sigma = sigma
        self.p = p
        self.line = Line(self.name)
        self.nxt = nxt
        self.serving = None
        self.free = 0

    def serve(self, t):
        # check that the last customer has been served
        if (not self.line.empty()) and self.free <= t:
            # free will be the finishing time of serving: if it is past, move serving to the next line.
            if self.serving is not None:
                self.nxt.line.push(self.serving)

            if self.line.head().tin_door <= t:
                # take the next customer from the head of the line
                cust = self.line.pop()
                # Set their serve start time
                cust.t_serv_start = t

                # calculate the time to serve this customer
                # I don't care to be accurate beyond the nearest second
                self.free = t + abs(round(np.random.normal(loc=self.mu, scale=self.sigma)))
                cust.t_serv_end = self.free
                self.serving = cust

        # If the line is empty, this station can skip until the end of days
        if self.line.empty():
            next_cust_time = float('inf')
        # If the line is not empty, it may be able to skip to the next customer
        else:
            next_cust_time = self.line.head().tin_door
        # Because we can skip to whichever of these is further away, as far as this station is concerned
        # Either the next time it can serve a customer or the next time it has one
        return max(self.free, next_cust_time)
