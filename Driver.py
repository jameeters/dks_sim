import numpy as np
from Door import Door
from ServiceStation import ServiceStation
from Register import Register
from utils import *
from Analysis import *

# CONFIG VARS
H_END = 0.5  # The number of hours for which the simulation should be run
LAM_ENTRY = 0.04614800359813854

# NON-CONFIG CONSTANTS
T_0 = 0  # a datetime for the start of the simulation
T_END = round(H_END * 3600)  # the number of seconds for which the

# IMPORTANT MUTABLE VALUES
t = 0  # the number of seconds since T_0 currently being simulated

alldone = []
per_iteration = []
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
        ServiceStation(Names.gandg, 5, 0.001, 0.4, nxt=register),
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
    per_iteration.append(done)

print('SIM DONE')
count_choices(alldone)

print('-' * 30)
print('total')
print_total_time_stats(alldone)
print('-' * 30)

print(Names.sandwich.value)
print_total_time_stats([d for d in alldone if d.choice == Names.sandwich])
print('-' * 30)

print(Names.wrap.value)

print_total_time_stats([d for d in alldone if d.choice == Names.wrap])
print('-' * 30)

print(Names.gandg.value)
print_total_time_stats([d for d in alldone if d.choice == Names.gandg])
print('-' * 30)

c = input('continue (y/n): ')
if not c.lower().strip() == 'y' or 'yes':
    exit(0)

total_times(alldone)
line_times(alldone)
line_lengths(per_iteration)

