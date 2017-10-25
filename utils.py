from enum import Enum
import numpy as np

SIM_ITERATIONS = 1000


class Names(Enum):
    sandwich = 'SANDWICH'
    wrap = 'WRAP'
    gandg = 'GRAB AND GO'
    register = 'REGISTER'


def rvec(l):
    s = l.__repr__()
    s = s[1:-1]
    return 'c({})'.format(s)


def print_total_time_stats(data):
    times = []
    for p in data:
        times.append(p.total_time() / 60)
    print(np.mean(times))
    print(np.std(times))
    print(min(times), max(times))
