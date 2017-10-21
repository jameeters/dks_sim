import numpy as np
from enum import Enum
from Door import Door
from ServiceStation import ServiceStation
from Register import Register


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
    ServiceStation(Names.sandwich, 200, 100, 0.33, nxt=register),
    ServiceStation(Names.wrap, 100, 50, 0.34, nxt=register),
    ServiceStation(Names.gandg, 0, 0, 0.33, nxt=register),
]

door = Door(LAM_ENTRY, T_END)
for customer in door.walkin():
    # Choose from the list of service stations with probabilities given by the stations in the list
    dest = stations[np.random.choice(list(range(len(stations))), p=[s.p for s in stations])]
    dest.line.push(customer)
    customer.choice = dest.name

while t <= T_END:
    try:
        t = min([i for i in [register.serve(t), *[ss.serve(t) for ss in stations]] if i > 0])
    except ValueError:
        t += 1

    print([register.free, *[ss.free for ss in stations]])
    print(t)
