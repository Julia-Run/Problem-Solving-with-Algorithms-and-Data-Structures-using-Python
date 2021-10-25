from turtle import *


# t = Turtle()
# win = t.getscreen()
# win.exitonclick()

# # 汉诺塔问题(基本的递归问题：基本情况+循环体，理解最简单的解法）
# #  有n个需要移动：
# #       1.先将n-1个借助end移动到to上，2.将最底下的从start移动到end。3.将n-1个从to移动到end上（循环完成）
# def move(n, start, to, end):
#     if n < 2:
#         print(start, '-->', end)  # 基本情况。
#     else:  # 循环
#         move(n - 1, start, end, to)
#         print(start, '-->', end)
#         move(n - 1, to, start, end)
#
#
# a = move(3, 'start', 'to', 'end')
#
# 基本的递归问题：基本情况+循环体
# def multiply(alist):
#     if len(alist) < 2:
#         return alist[0]
#     else:  # 循环
#         return alist[0] * multiply(alist[1:])
#
#
# num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1000]
# b = multiply(num)
# res = 1
# for i in num:
#     res = res * i
# print(b, b == res)

# 分形树.(情况更加复杂一点，理解清楚到底怎么画是关键)
# 基本情况：向前画x，退x
# 循环体：向前画x，右转theta，{{向前画x-delta，退x-delta}}，左转2*theta，{{向前画x-delta，退x-delta}}，右转theta，退x。（出错）
# 先画右边：基本情况：向前画x，右转theta。 循环：向前画（x-delta）。 //结束时，turtle停在右枝的末尾，角度为θ，x<delta
# 再画左边回退x，左转2θ，画x，右转θ，回退x+delta (出错，画x会使得整体陷入无限循环，思路本身没有问题，要稍加修改)
#       画x，违背了递归三原则（基本情况，调用递归，改变状态）---改变其状态，使得整体陷入无限循环
# 再画左边：
#       回退x（画右边的最后一次结果，x<delta，左画的时候无法进行，在这一循环中完成回退），到上一个节点
#       进入上一个tree结构体并继续（x>delta），左转2θ，画（x-θ），右转θ，回退x。
# t = Turtle()
# t.left(90)
# win = t.getscreen()
#
#
# def tree(x, delta):
#     if x - delta > 0:
#         t.forward(x)
#         t.right(20)
#         tree(x - delta, delta)
#         t.left(40)
#         tree(x - delta, delta)
#         t.right(20)
#         t.backward(x)
#
#
# x = tree(100, 30)
# win.exitonclick()

# 谢尔平斯基三角形
# func1：三个顶点画，0-1-2-0.
# func2：找中点
# func3： 递归（全部顺时针画）（基础3个点，n级）
#   思路类似分形树，先完成一支（0--1--2（左上下））
#       1.0-1-2-0


def draw(p, colors, my_turtle):
    my_turtle.fillcolor(colors)
    my_turtle.up()
    my_turtle.goto(p[0])
    my_turtle.down()
    my_turtle.begin_fill()
    my_turtle.goto(p[1])
    my_turtle.goto(p[2])
    my_turtle.goto(p[0])
    my_turtle.end_fill()


def mid_point(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)


def array(p, degree, one_turtle):
    # my first writting. //认为是（基本情况+循环，仿照假发计算部分）从左下角最小的开始画，只填充一种颜色
    # 不要太刻板。基本情况就是简单的画一个三角形，和degree无关。
    # 循环体中，考虑画的顺序：左上右
    colormap = ['blue', 'red', 'green', 'white', 'yellow', 'violet', 'orange']
    if degree == 0:
        draw(p, colormap[0], one_turtle)
    else:
        array([p[0], mid_point(p[0], p[1]), mid_point(p[0], p[2])], degree - 1, one_turtle)
        array([p[1], mid_point(p[1], p[2]), mid_point(p[1], p[0])], degree - 1, one_turtle)
        array([p[2], mid_point(p[2], p[0]), mid_point(p[2], p[1])], degree - 1, one_turtle)

# def array(p, degree, one_turtle):
#     # modified based on book
#     # 基本情况（被重复的操作）：画图函数draw（）。循环体：画左右上（通过调用递归并改变状态实现）
#     colormap = ['blue', 'red', 'green', 'white', 'yellow', 'violet', 'orange']
#     draw(p, colormap[degree], one_turtle)
#     if degree > 0:
#         array([p[0], mid_point(p[0], p[1]), mid_point(p[0], p[2])], degree - 1, one_turtle)
#         array([p[1], mid_point(p[1], p[2]), mid_point(p[1], p[0])], degree - 1, one_turtle)
#         array([p[2], mid_point(p[2], p[0]), mid_point(p[2], p[1])], degree - 1, one_turtle)


t = Turtle()
win = t.getscreen()
p_test = [(-200, -150), (0, 150), (200, -150)]
array(p_test, 4, t)
win.exitonclick()
