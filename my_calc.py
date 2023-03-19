def sum_2(a, b):
    return a + b


def sum_args(*args):
    s = 0
    for i in args:
        s += i
    return s


def multi(a, b):
    return a * b


def division(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print('На ноль не делят')
