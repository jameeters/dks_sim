from Door import Door
from ServiceStation import ServiceStation
from DQ import DQ
from Line import Line
from Entryway import Option, Entryway

# CONFIG VARS
H_END = 1  # The number of hours for which the simulation should be run
LAM_ENTRY = 0.04614800359813854


# NON-CONFIG CONSTANTS
T_0 = 0  # a datetime for the start of the simulation
T_END = H_END * 3600  # the number of seconds for which the
NAMES = ['sandwich', 'wrap', 'grab', 'register']

# IMPORTANT MUTABLE VALUES
t = 0  # the number of seconds since T_0 currently being simulated



SERVICE_STATIONS = [
    ServiceStation('sandwich', mu=200, sigma=100),
    ServiceStation('wrap', mu=100, sigma=50),
    ServiceStation('register', mu=16, sigma=14)
]
# todo: delete this
QUEUES = {ss.name: (DQ(ss.name, ss)) for ss in SERVICE_STATIONS}

LINES = { name: Line(name) for name in NAMES }

OPTIONS_CONFIG = [
    {
        'name': 'sandwich',
        'p': 0.333,
        'line': LINES['sandwich']
    },
    {
        'name': 'wrap',
        'p': 0.333,
        'line': LINES['wrap']
    },
    {
        'name': 'grab',
        'p': 0.333,
        'line': LINES['register']
    }
]
OPTIONS = [ Option(opt['name'], opt['p'], opt['line']) for opt in OPTIONS_CONFIG ]

entryway = Entryway(OPTIONS)

door = Door(LAM_ENTRY, T_END)
while t <= T_END:
    entries = door.walkin()
    for i in list(range(0, entries)):
        person = Per




