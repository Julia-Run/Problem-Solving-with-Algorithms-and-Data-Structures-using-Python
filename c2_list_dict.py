from timeit import Timer
from matplotlib import pyplot as plt
import random

# # generate a list ###############################################
# def test1():
#     a = list(range(1000))
#
#
# def test2():
#     a = [i for i in range(1000)]
#
#
# def test3():
#     a = []
#     for i in range(1000):
#         a.append(i)
#
#
# def test4():
#     a = []
#     for i in range(1000):
#         a = a + [i]
#
#
# for i in range(1, 5):
#     t = Timer('test%d()' % i, 'from __main__ import test%d' % i)
#     print(t.timeit(number=1000), 'ms')


# # experiment of pop and popi
# tp, tpi = [], []
# for i in range(10000, 200001, 10000):
#     x = list(range(i))
#     t = Timer("x.pop()", 'from __main__ import x').timeit(number=1000)
#     tp.append(t)
#     x = list(range(i))
#     t = Timer("x.pop(0)", 'from __main__ import x').timeit(number=1000)
#     tpi.append(t)
# alist = list(range(10000, 200001, 10000))
# plt.plot(alist, tp, alist, tpi)
# plt.show()


# #experiments

tl, td = [], []
for i in range(10000, 200001, 10000):
    t = Timer('random.randrange(%d) in x' % i, 'from __main__ import random,x')
    x = list(range(i))
    tl.append(t.timeit(number=1000))
    x = {j: None for j in range(i)}
    td.append(t.timeit(number=1000))
alist = list(range(10000, 200001, 10000))
plt.plot(alist, tl, alist, td)
plt.show()
