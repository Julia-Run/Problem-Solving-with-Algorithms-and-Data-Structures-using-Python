from pythonds.basic import Stack
import string


# # 10进制转换成任意进制
# def myint(num, base):
#     digitals = '0123456789ABCDEF'
#     result_inv = Stack()
#     while num > 0:
#         result_inv.push(num % base)
#         num = num // base
#     i = 0
#     result = ''
#     while not result_inv.isEmpty():
#         result = result + digitals[result_inv.pop()]
#         i = i + 1
#     print(result)
#     return result
#
#
# test = 12345
# myint(test, 2)


# 中序表达式转换成后续表达式
def convertor(exp):
    first = {'(': 1, '+': 2, '-': 2, '*': 3, '/': 3}
    inputs = exp.upper().split()
    output = []
    oper = Stack()

    i = 0
    while i < len(inputs):
        if inputs[i] in string.ascii_uppercase:
            output.append(inputs[i])
        elif inputs[i] in list(first.keys()):
            if inputs[i] == '(':
                oper.push(inputs[i])
            else:
                while oper.size() != 0 and first[oper.peek()] >= first[inputs[i]]:  # 注意此处应该是大于等于，而不是直接大于
                    output.append(oper.pop())
                oper.push(inputs[i])
        elif inputs[i] == ')':
            while oper.peek() != '(':
                output.append(oper.pop())
            oper.pop()
        else:
            print('input Wrong !')
        i = i + 1
    while not oper.isEmpty():
        output.append(oper.pop())
    result = ' '.join(output)
    print(' '.join(inputs), ' --> ', result)

    return result


# convertor('( A + B ) * C - ( D - E ) * ( F + G )')  # test

def convertor1(exp):
    first = {'(': 1, '+': 2, '-': 2, '*': 3, '/': 3}
    inputs = exp.upper().split()
    output = []
    oper = Stack()

    i = 0
    while i < len(inputs):

        if inputs[i] in list(first.keys()):
            if inputs[i] == '(':
                oper.push(inputs[i])
            else:
                while oper.size() != 0 and first[oper.peek()] >= first[inputs[i]]:  # 注意此处应该是大于等于，而不是直接大于
                    output.append(oper.pop())
                oper.push(inputs[i])
        elif inputs[i] == ')':
            while oper.peek() != '(':
                output.append(oper.pop())
            oper.pop()
        else:
            output.append(inputs[i])

        i = i + 1
    while not oper.isEmpty():
        output.append(oper.pop())
    result = ' '.join(output)
    print(' '.join(inputs), ' --> ', result)

    return result


def math4(a, b, op):
    if op == '+':
        r = a + b
    elif op == "-":
        r = a - b
    elif op == '*':
        r = a * b
    else:
        if b == 0:
            raise 'Divided by Zero'
        else:
            r = a / b
    return r


def post_caculator(exp):
    operand = Stack()
    operator = ['+', '-', '*', '/']
    exp_list = exp.split()
    for i in exp_list:
        if i not in operator:
            operand.push(int(i))
        else:
            op2 = operand.pop()
            op1 = operand.pop()
            operand.push(math4(op1, op2, i))
    result = operand.pop()
    print(result)
    return result


def caculator(s):
    post_caculator(convertor1(s))


caculator('( 11 + 12 ) * 1  - ( 2 - 3 ) * ( 4 + 6 ) ')
