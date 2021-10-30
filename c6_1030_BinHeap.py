# from pythonds.trees import BinaryTree
from pythonds.trees import BinHeap
from pythonds.basic import Stack
# 二叉搜索树，实现映射抽象数据类型。（之前用散列实现过）
# Map()  / put(key,value)  /del amap[key]  / get(key)  /len()  /in
# 二叉搜索树：对任意一个节点，比节点值小的值放在左子值，大的放在右子树，也叫做二叉搜索性
# 必须处理并创建一颗空的二叉树，因此在实现的过程中必须使用两个类，涉及两个类的耦合问题
# put函数，新来的一定被放在最后，无论大小



## 二叉堆的实现。 二叉堆：对任意树，父节点的值总是小于子节点的值，root的值为最小值.叶子从左往右排
# 用列表来实现。第一个元素为0，初始化
class Mybinheap(object):
    def __init__(self):
        self.list = [0]
        self.currentsize = 0

    def add(self, new):  #
        self.list.append(new)
        self.currentsize += 1
        self.percUp(self.currentsize)
        print(self.list)

    def percUp(self, i):
        # 在添加元素中被调用
        while i // 2 > 0:
            # 不需要考虑左半枝的元素（a），已经比父节点（c）大，（a《c），当新增在右半枝的b《c时候，才会b和c交换，此时a》c》b，因此只需要考虑半枝
            if self.list[i] < self.list[i // 2]:  # obey
                self.list[i], self.list[i // 2] = self.list[i // 2], self.list[i]  # 元素向上换到对应的位置
            i = i // 2

    def percDown(self, i):
        # 在DEL中调用
        # 如果顶端的元素大于子元素，换到更小的子元素位置上，速度更快，且较大的子元素再往下，可能比顶端元素更大
        while i * 2 <= self.currentsize:
            smallerchild_loc = self.locatemin(i)
            if self.list[i] > self.list[smallerchild_loc]:
                self.list[i], self.list[smallerchild_loc] = self.list[smallerchild_loc], self.list[i]
            i = smallerchild_loc

    def locatemin(self, i):
        if 2 * i + 1 > self.currentsize:
            return 2 * i
        else:
            if self.list[2 * i] < self.list[2 * i + 1]:
                return 2 * i
            else:
                return 2 * i + 1

    def deletemin(self):
        self.list[1] = self.list[self.currentsize]
        self.currentsize = self.currentsize - 1
        self.list.pop()
        self.percDown(1)
        print('\n')
        print(self.list)

    def creatfromlist(self, alist):
        i = len(alist) // 2
        self.currentsize = len(alist)
        self.list = [0] + alist[:]
        while i > 0:
            self.percDown(i)
            i = i - 1
        print(self.list)
    # def creatfromlist(self, alist):
    #     k = len(alist) // 2
    #     self.list = [0] + alist[:]
    #     self.currentsize = len(alist)
    #     for i in range(k, 0, -1):
    #         self.percDown(i)
    #     print(self.list)


test = Mybinheap()
test.add(10)
test.add(1)
test.add(3)
test.add(5)
test.add(-20)
test.add(-1)
test.deletemin()
a = Mybinheap()
a.creatfromlist([20, 15, 10, 5, 3, 2.2, 2])
a.deletemin()
a.add(-1)

# # # 遍历tree 前、中‘后序列********************************************************
# a0 = BinaryTree('1')
# a0.insertLeft('1.1')
# a0.insertRight('1.2')
#
# a1l = a0.getLeftChild()
# a1l.insertLeft('1.1.1')
# a1l.insertRight('1.1.2')
#
# a1r = a0.getRightChild()
# a1r.insertLeft('1.2.1')
# a1r.insertRight('1.2.2')
#
#
# def pre(tree):
#     if tree:
#         print(tree.getRootVal(), end='-->')
#         pre(tree.getLeftChild())
#         pre(tree.getRightChild())
#
#
# print('pre')
# pre(a0)
#
#
# def post(tree):
#     if tree:
#         post(tree.getLeftChild())
#         post(tree.getRightChild())
#         print(tree.getRootVal(), end='-->')
#
#
# print('\npost')
# post(a0)
#
#
# def mid(tree):
#     if tree:
#         mid(tree.getLeftChild())
#         print(tree.getRootVal(), end='-->')
#         mid(tree.getRightChild())
#
#
# print('\nmid')
# mid(a0)
