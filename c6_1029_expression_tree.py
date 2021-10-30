# 1.遇到左括号，意味着言开始填入运算符左边的数字，所以：创建左节点顶下沉至左节点。
# 2.遇到数字，填入当前节点，并返回其父节点，
# 3.遇到运算符，填入当前节点，同时意味着要记录右边的运算数字，所以：创建右节点，并下沉至右节点
# 4.遇到右括号，意味着本次括号内的计算结束回到父节点。这款里为什么要回到父节点呢？
#       如果没有父节点可以跳，则意味着工作已经完成。、、、但是公式列表读完不就直到已经完成工作了吗
#       意味着括号里的内容计算结束，退出该括号，一个子树为一个括号
# 问题： 要是完全括号才可以
from pythonds.basic import Stack
from pythonds.trees import BinaryTree


def exp2tree(exp):
    el = exp.split()
    et = BinaryTree('')
    helper = Stack()
    helper.push(et)  # 否则会报错，最后一个括号无处可回,换成什么都可以
    operator = "+-*/"
    for i in el:
        if i == "(":
            et.insertLeft('')
            helper.push(et)  # 插入左半支的tree，仍在上一个节点：k级（的root位）
            et = et.getLeftChild()  # 到左半支的子树（的root位置）： k+1级
        elif i in operator:
            et.setRootVal(i)
            et.insertRight('')
            helper.push(et)
            et = et.getRightChild()
        elif i == ")":
            et = helper.pop()  # 回到上一个节点
        else:
            et.setRootVal(int(i))
            et = helper.pop()
    return et


import operator as op


def evaluate(parseTree):
    fn = {"+": op.add, '-': op.sub, "*": op.mul, "/": op.truediv}
    left = parseTree.getLeftChild()
    right = parseTree.getRightChild()
    if left and right:  # 一定是个运算符
        func = fn[parseTree.getRootVal()]
        return func(evaluate(left), evaluate(right))
    else:  # 否则一定是数字
        return parseTree.getRootVal()


test = exp2tree("( ( ( 100 + 5 ) * 3 ) + 123 )")
print(evaluate(test))


# 前序遍历
def pre(abook):
    # if abook.getLeftChild() is not None:
    if abook:
        pre(abook.getLeftChild())
        pre(abook.getRightChild())
        return abook.getRootVal()
