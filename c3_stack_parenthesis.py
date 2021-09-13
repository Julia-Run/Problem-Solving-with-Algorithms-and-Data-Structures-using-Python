from pythonds.basic import Stack


# 从list发展出stack
# class Mystack():
#     def __init__(self):
#         self.items = []
#
#     def myisEmpty(self):
#         return self.items == []
#
#     def mysize(self):
#         return len(self.items)
#
#     def mypop(self):
#         return self.items.pop()
#
#     def mypush(self, value):
#         return self.items.append(value)
#
#     def mypeek(self):
#         return self.items[-1]
#
#
# s = Mystack()
# s.mypush(1)
# s.mypush(True)
# s.mypush('good')
# print(s.items)
# print(s.mypeek(), s.mypop(), s.items, s.myisEmpty(), s.mysize(), sep=' ~~ ')

# # 括号的匹配
# def parenthesis_check(par):
#     s = Stack()
#     match = True
#     i = 0
#     while i < len(par) and match:
#         if par[i] == '(':
#             s.push(par[i])
#         else:
#             if s.isEmpty():
#                 match = False
#             else:
#                 s.pop()
#         i = i + 1
#     if not s.isEmpty():
#         match = False
#     print(match)
#     return match
#
#
# test = '((())())'
# parenthesis_check(test)

# # 括号的匹配 -- advanced

def basic_check(left, right):
    a, b = '([{', ')]}'
    # return a.index(left) == b.index(right)
    done = False
    if a.index(left) == b.index(right):
        done = True
    return done


#

def parenthesis_check(par):
    s = Stack()
    a, b = '([{', ')]}'
    match = True
    i = 0
    while i < len(par) and match:
        if par[i] in a:
            s.push(par[i])
        else:
            if s.isEmpty():
                match = False
            elif not basic_check(s.peek(), par[i]):
                match = False
            else:
                s.pop()
            # else: #
            #     top=pop() #
            #     if not basic_check(top, par[i]):
            #     match = False
        i = i + 1
    if not s.isEmpty():
        match = False
    # if match and s.isEmpty():
    #     match = True
    # else:
    #     match = False

    print(match)
    return match


test = '({[(())()]})'
parenthesis_check(test)
