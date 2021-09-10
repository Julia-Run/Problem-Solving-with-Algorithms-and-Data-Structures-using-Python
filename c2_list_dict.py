from timeit import Timer


def test1():
    a = list(range(1000))


def test2():
    a = [i for i in range(1000)]


def test3():
    a = []
    for i in range(1000):
        a.append(i)


def test4():
    a = []
    for i in range(1000):
        a = a + [i]


for i in range(1, 5):
    t = Timer('test%d()' % i, 'from __main__ import test%d' % i)
    print(t.timeit(number=1000), 'ms')

