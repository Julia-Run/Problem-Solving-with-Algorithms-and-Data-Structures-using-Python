# # 递归是一种嵌套res=(1+(2+(3+(4+(5。
# # 5是最简单基础的一次计算，该结果返回给sumlist（[4,5]）,在else分支中被返回，再带入上一级。。。
# def sumlist(s):
#     if len(s) == 1:
#         return s[0]
#     else:
#         return s[0] + sumlist(s[1:])
#     # 在else分支中，每
#
#
# print(sumlist([1, 2, 3, 4, 5]))
# #
# #
# # 递归完成10进制向任意进制的转换
# def ten2any(num, base):
#     digitals = '0123456789ABCDEF'
#     if num < base:
#         return digitals[num]
#     else:
#         return ten2any(num // base, base) + digitals[num % base]
#
#
# print(ten2any(100000, 16))

# 分型树
from turtle import *

# myTurtle = Turtle()
# myWin = myTurtle.getscreen()
# # from book:从外向里画
# def drawSpiral(myTurtle, lineLen):
#     if lineLen > 0:
#         myTurtle.forward(lineLen)
#         myTurtle.right(90)
#         drawSpiral(myTurtle, lineLen - 5)
# drawSpiral(myTurtle, 100)
# myWin.exitonclick()

# # 从里向外画
# myTurtle = Turtle()
# myWin = myTurtle.getscreen()
#
#
# def myspiral(myTurtle, lineLen, delta, n):
#     if n > 0:
#         myTurtle.forward(lineLen)
#         myTurtle.right(90)
#         myspiral(myTurtle, lineLen + delta, delta, n - 1)
#
#
# myspiral(myTurtle, 10, 10, 20)
# myWin.exitonclick()


# 分型树
# 1.枝丫越来越短， 2.一分二，二分四，总共分多少次 3.
import random
myTurtle = Turtle()
myWin = myTurtle.getscreen()
myTurtle.left(90)
myTurtle.backward(100)
myTurtle.color('green')


def tree(myTurtle, len, delta):
    if len - delta >= 0:
        myTurtle.forward(len)
        myTurtle.right(30)
        tree(myTurtle, len - delta, delta)
        myTurtle.left(15)
        tree(myTurtle, len - delta, delta)
        myTurtle.left(15)
        tree(myTurtle, len - delta, delta)
        myTurtle.left(15)
        tree(myTurtle, len - delta, delta)
        myTurtle.left(15)
        tree(myTurtle, len - delta, delta)
        myTurtle.right(30)
        myTurtle.backward(len)


tree(myTurtle, 120, 20)
myWin.exitonclick()
