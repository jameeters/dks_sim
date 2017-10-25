import numpy as np
from Door import Door
from ServiceStation import ServiceStation
from Register import Register
from utils import rvec, Names
from Analysis import *

# CONFIG VARS
H_END = 0.5  # The number of hours for which the simulation should be run
LAM_ENTRY = 0.04614800359813854
SIM_ITERATIONS = 1

# NON-CONFIG CONSTANTS
T_0 = 0  # a datetime for the start of the simulation
T_END = round(H_END * 3600)  # the number of seconds for which the

# IMPORTANT MUTABLE VALUES
t = 0  # the number of seconds since T_0 currently being simulated

alldone = []
# stations = [
#     ServiceStation(Names.sandwich, 298, 68, 0.3558080808, nxt=register),
#     ServiceStation(Names.wrap, 74, 18, 0.2962121212, nxt=register),
#     ServiceStation(Names.gandg, 10, 3, 0.347979798, nxt=register),
# ]


for i in range(SIM_ITERATIONS):
    t = 0
    done = []
    register = Register(Names.register, 16, 14, done)
    stations = [
        ServiceStation(Names.sandwich, 298, 68, 0.2, nxt=register),
        ServiceStation(Names.wrap, 74, 18, 0.4, nxt=register),
        ServiceStation(Names.gandg, 5, 1, 0.4, nxt=register),
    ]
    door = Door(LAM_ENTRY, T_END)
    for customer in door.walkin():
        # Choose from the list of service stations with probabilities given by the stations in the list
        dest = stations[np.random.choice(list(range(len(stations))), p=[s.p for s in stations])]
        dest.line.push(customer)
        customer.choice = dest.name

    while True:
        next_times = [s.serve(t) for s in stations]
        next_times.append(register.serve(t))
        if min(next_times) == float('inf'):
            break
        else:
            t = min(next_times)

    alldone = [*alldone, *done]
print('SIM DONE')
count_choices(alldone)
# print('-' * 30)
# print('total')
# times = []
# for p in done:
#     times.append(p.total_time() / 60)
# print(np.mean(times) / 60)
# print(np.median(times) / 60)
# print(min(times), max(times))
# print('-' * 30)
#
# print(Names.sandwich.value)
# times = []
# for p in [d for d in done if d.choice == Names.sandwich]:
#     times.append(p.serv_time() / 60)
# print(np.mean(times))
# print(np.median(times))
# print(min(times), max(times))
# print('-' * 30)
#
# print(Names.wrap.value)
# times = []
# for p in [d for d in done if d.choice == Names.wrap]:
#     times.append(p.serv_time() / 60)
# print(np.mean(times))
# print(np.median(times))
# print(min(times), max(times))
# print('-' * 30)
#
# print(Names.gandg.value)
# times = []
# for p in [d for d in done if d.choice == Names.gandg]:
#     times.append(p.serv_time() / 60)
# print(np.mean(times))
# print(np.median(times))
# print(min(times), max(times))
# print('-' * 30)
#
# print(rvec([i.total_time() for i in done]))
# print('*' * 70)
# print(rvec([i.food_line_time() for i in done if i.choice == Names.sandwich]))

# total_times(done)
# line_times(done)
line_lengths(done)
