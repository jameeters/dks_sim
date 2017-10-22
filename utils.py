
def rvec(l):
    s = l.__repr__()
    s = s[1:-1]
    return 'c({})'.format(s)


