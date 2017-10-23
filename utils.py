from enum import Enum


class Names(Enum):
    sandwich = 'SANDWICH'
    wrap = 'WRAP'
    gandg = 'GRAB AND GO'
    register = 'REGISTER'


def rvec(l):
    s = l.__repr__()
    s = s[1:-1]
    return 'c({})'.format(s)


