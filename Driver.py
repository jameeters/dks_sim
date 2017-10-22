import numpy as np
from enum import Enum
from Door import Door
from ServiceStation import ServiceStation
from Register import Register
from utils import rvec


class Names(Enum):
    sandwich = 'SANDWICH'
    wrap = 'WRAP'
    gandg = 'GRAB AND GO'
    register = 'REGISTER'


# CONFIG VARS
H_END = 1  # The number of hours for which the simulation should be run
LAM_ENTRY = 0.04614800359813854

# NON-CONFIG CONSTANTS
T_0 = 0  # a datetime for the start of the simulation
T_END = H_END * 3600  # the number of seconds for which the

# IMPORTANT MUTABLE VALUES
t = 0  # the number of seconds since T_0 currently being simulated

done = []
register = Register(Names.register, 16, 14, done)
stations = [
    ServiceStation(Names.sandwich, 298, 68, 0.3558080808, nxt=register),
    ServiceStation(Names.wrap, 74, 18, 0.2962121212, nxt=register),
    ServiceStation(Names.gandg, 10, 3, 0.347979798, nxt=register),
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

print('-'*30)
print('total')
total_times = []
for p in done:
    total_times.append(p.total_time() / 60)
print(np.mean(total_times)/60)
print(np.median(total_times)/60)
print(min(total_times), max(total_times))
print('-'*30)

print(Names.sandwich.value)
times = []
for p in [d for d in done if d.choice == Names.sandwich]:
    times.append(p.serv_time() / 60)
print(np.mean(times))
print(np.median(times))
print(min(times), max(times))
print('-'*30)

print(Names.wrap.value)
times = []
for p in [d for d in done if d.choice == Names.wrap]:
    times.append(p.serv_time() / 60)
print(np.mean(times))
print(np.median(times))
print(min(times), max(times))
print('-'*30)

print(Names.gandg.value)
times = []
for p in [d for d in done if d.choice == Names.gandg]:
    times.append(p.serv_time() / 60)
print(np.mean(times))
print(np.median(times))
print(min(times), max(times))
print('-'*30)


