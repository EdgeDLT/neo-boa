from boa.interop.Neo.Runtime import Notify


def Main():

    a = 4

    b = a << 2

    c = a >> 2

    print("shifted a!")

    Notify(b)

    Notify(c)

    m = 16

    m >>= 3

    q = 670

    q >>= 8

    Notify(m)

    if q == m:
        print("all ok!")

    else:
        print("not ok")

    return b
