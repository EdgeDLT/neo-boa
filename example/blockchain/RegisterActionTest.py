from boa.interop.Neo.Action import RegisterAction
from boa.interop.Neo.Runtime import Notify


OnThing = RegisterAction('blah', 'bloop', 'bleep')


def Main():

    ename = 'thing'
    arg1 = 2
    arg2 = 4

    OnThing(ename, arg1, arg2)

    return arg1
