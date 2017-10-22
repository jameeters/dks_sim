import numpy as np
from ServiceStation import Line


class Register:
    def __init__(self, name, mu, sigma, nxt):
        self.name = name
        self.mu = mu
        self.sigma = sigma
        self.line = Line(self.name)
        self.nxt = nxt
        self.serving = None
        self.free = 0

    def serve(self, t):
        # check that the last customer has been served
        if (not self.line.empty()) and self.free <= t:
            # free will be the finishing time of serving, if it is past, serving can leave.
            if self.serving is not None:
                self.nxt.append(self.serving)

            if self.line.head().tin_door <= t:
                # take the next customer from the head of the line
                cust = self.line.pop()
                # Set their serve start time
                cust.t_co_start = t

                # calculate the time to serve this customer
                # I don't care to be accurate beyond the nearest second
                self.free = t + round(np.random.normal(loc=self.mu, scale=self.sigma))
                cust.tout_door = self.free
                self.serving = cust

        if self.line.empty():
            next_cust_time = float('inf')
        else:
            next_cust_time = self.line.head().t_serv_end

        return max(self.free, next_cust_time)
