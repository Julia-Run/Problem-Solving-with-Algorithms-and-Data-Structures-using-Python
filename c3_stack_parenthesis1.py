from pythonds.basic import Stack


def match(left, right):
    a, b = '([{', ')]}'
    return a.index(left) == b.index(right)


def parcheck(s):
    left = Stack()
    result = True
    i = 0
    while i < len(s) and result:
        if s[i] in "([{":
            left.push(s[i])
        else:
            if left.isEmpty():
                result = False  # 1.右括号多了
            else:
                top = left.pop()
                if not match(top, s[i]):
                    result = False  # 2. 对应的括号不match
        i = i + 1
    if not left.isEmpty():
        result = False  # 3. 左括号多了. 总共三种出错的情况
    print(result)
    return result


test = '({[(())()]}]'
parcheck(test)
