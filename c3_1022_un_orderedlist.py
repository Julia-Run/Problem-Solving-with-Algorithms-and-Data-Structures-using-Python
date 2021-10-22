# class Node(object):
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#     def getdata(self):
#         return self.data
#
#     def getnext(self):
#         return self.next
#
#     def setdata(self, new):
#         self.data = new
#
#     def setnext(self, anode):
#         self.next = anode
#
#
# class Unorderedlist(object):
#     def __init__(self):
#         self.head = None
#
#     def search(self, item_s):
#         current = self.head
#         found = False
#         while not found and current is not None:
#             if current.getdata() == item_s:
#                 found = True
#             else:
#                 current = current.getnext()
#         return found
#
#     def add(self, item_a):
#         temp = Node(item_a)
#         temp.setnext(self.head)
#         self.head = temp
#
#     def remove(self, item_r):
#         current = self.head
#         previous = None
#         found = False
#         while current is not None and not found:
#             if current.getdata() == item_r:
#                 found = True
#             else:
#                 previous = current
#                 current = current.getnext()
#         if previous is None:
#             self.head = current.getnext()
#         else:
#             previous.setnext(current.getnext())  # previous指向链表中的Node，对其调用setnext（），就是更改了链表中该Node的指向
#
#     def length(self):
#         current = self.head
#         i = 0
#         while current is not None:
#             i = i + 1
#             current = current.getnext()
#         return i
#
#     def isEmpty(self):
#         return self.head == None
#
#     def __str__(self):
#         current = self.head
#         res = []
#         while current is not None:
#             res.append(current.getdata())
#             current = current.getnext()
#         return str(res)
#
#     __repr__ = __str__
#
#
# a = Unorderedlist()
# a.add(1)
# a.add(True)
# a.add('test1')
# print(a)
# a.remove(True)
# print(a)

# 有序列表
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def getdata(self):
        return self.data

    def getnext(self):
        return self.next

    def setdata(self, new):
        self.data = new

    def setnext(self, anode):
        self.next = anode


class Orderedlist(object):
    def __init__(self):
        self.head = None

    def search(self, item_s):
        current = self.head
        found = False
        while not found and current is not None and current.getdata() < item_s:
            if current.getdata() == item_s:
                found = True
            else:
                current = current.getnext()
        return found

    def add(self, item_a):
        current = self.head
        previous = None
        stop = False
        while not stop and current is not None:
            if current.getdata() > item_a:
                stop = True
            else:
                previous = current
                current = current.getnext()

        temp = Node(item_a)
        if previous == None:
            self.head = temp
            temp.setnext(current)
        else:
            previous.setnext(temp)
            temp.setnext(current)

    def __str__(self):
        current = self.head
        res = []
        while current is not None:
            res.append(current.getdata())
            current = current.getnext()
        return str(res)

    __repr__ = __str__


a = Orderedlist()
a.add(1)
a.add(8)
a.add(3)
a.add(-11)
a.add(9)
a.add(0)
print(a)

# # 双端队列回文数检测
# from pythonds.basic import Deque
#
#
# def reverse(s):
#     a = Deque()
#     # s_hat = s.replace(' ', '')   #
#     s_hat = ''.join(s.split())
#     # print(s_hat)
#     for i in s_hat:
#         a.addFront(i)
#         res = True
#     while a.size() > 1 and res:
#         f = a.removeFront()
#         r = a.removeRear()
#         if f != r:
#             res = False
#     print(res)
#     return res
#
#
# reverse('LOOL')
