from pythonds.basic import Stack
import string


# # 10进制向任意进制转化
# def ten2base(num, base):
#     value = '0123456789ABCDEF'
#     inverse = Stack()
#     while num / base > 0:  # while num > 0
#         inverse.push(num % base)
#         num = num // base
#     res = ''
#     while not inverse.isEmpty():
#         res = res + value[inverse.pop()]
#     print(res)
#     return res
#
#
# num1 = 100
# ten2base(123456, 16)

# # 中序表达式转换成后续表达A+B*C-D --> ABC*+D-
# # 字母放在输出的结果中，操作符放在Stack中
# # 操作符：1.遇到左括号直接推进， 2.*/，去除前面的惩处推进， 3.+_先提出前面的加减乘除，再推进  4.右括号，提出操作符，扔掉对应的一个左括号
# # 初始边界条件：上一行第2、3步，涉及提出--若最先出现，则没有可以提出的符号A+B*C-D
# # 末尾边界条件： 按顺序提出剩余的所有操作符
# def convertor(exp):
#     order = {'(': 1, '+': 2, '-': 2, '*': 3, '/': 3}
#     s = exp.split()
#     res = []
#     operator = Stack()
#     i = 0
#     while i < len(s):
#         if s[i].upper() in string.ascii_uppercase:
#             res.append(s[i])  # 放字母
#         elif s[i] in list(order.keys()):
#             if s[i] == '(':
#                 operator.push(s[i])  # 1.
#             else:
#                 while not operator.isEmpty() and order[operator.peek()] >= order[s[i]]:  # 2，3+初始边界条件
#                     res.append(operator.pop())
#                 operator.push(s[i])
#         elif s[i] == ')':  # 4.
#             while operator.peek() != '(':
#                 res.append(operator.pop())
#             operator.pop()
#         else:
#             raise "Wrong Input!"
#         i = i + 1
#     while not operator.isEmpty():
#         res.append(operator.pop())
#     final = ' '.join(res)
#     print(exp, ' --> ', final)
#     return final
#
#
# convertor('( A + B ) * C - ( D - E ) * ( F + G )')  # test
# convertor('( A + B ) * C')  # test
# convertor('A + B + C + D')  # test
# convertor('A * B + C * D')  # test
# convertor('A + B * C - D')  # test


# 计算后续表达式+计算器
# 把转换器中的字母换成数字，最后返回值换成list
# 将后续表达式list依次推入stack，遇到操作符，去除两个数计算，计算结果再次推入stack，stack中最后结果即为计算结果
# 要定义基本操作符的运算

def convertor(exp):  # 修改转换器
    order = {'(': 1, '+': 2, '-': 2, '*': 3, '/': 3}
    s = exp.split()
    res = []
    operator = Stack()
    i = 0
    while i < len(s):
        if s[i] in list(order.keys()):
            if s[i] == '(':
                operator.push(s[i])  # 1.
            else:
                while not operator.isEmpty() and order[operator.peek()] >= order[s[i]]:  # 2，3+初始边界条件
                    res.append(operator.pop())
                operator.push(s[i])
        elif s[i] == ')':  # 4.
            while operator.peek() != '(':
                res.append(operator.pop())
            operator.pop()
        else:
            res.append(int(s[i]))
        i = i + 1
    while not operator.isEmpty():
        res.append(operator.pop())
    # final = ' '.join(res)
    print(exp, ' --> ', res)
    return res


# 定义基本运算
def calculator_basic(a, b, oper):
    if oper == '+':
        c = a + b
    elif oper == '-':
        c = a - b
    elif oper == '*':
        c = a * b
    else:
        c = a / b
    return c


# 计算后续表达式
def calculator1(alist):  # list from 转换器
    res = Stack()
    for i in alist:
        if type(i) is int:
            res.push(i)
        else:
            a2 = res.pop()
            a1 = res.pop()
            res.push(calculator_basic(a1, a2, i))
    final = res.pop()
    return final


# 计算
def calculator(s):
    x = convertor(s)
    y = calculator1(x)
    print('result -->', y)
    return y


calculator('( 11 + 12 ) * 1  - ( 2 - 3 ) * ( 4 + 6 ) ')
