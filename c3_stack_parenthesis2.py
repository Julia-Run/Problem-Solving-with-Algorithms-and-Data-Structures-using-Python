from pythonds.basic import Stack


def onematch(a, b):
    left, right = '([{', ')]}'
    return left.index(a) == right.index(b)


def parcheck(s):
    lefts = Stack()
    i = 0
    match = True
    while i < len(s) and match:
        if s[i] in '([{':
            lefts.push(s[i])
        else:
            if lefts.size() == 0:
                match = False
            else:
                top = lefts.pop()
                if not onematch(top, s[i]):
                    match = False
        i = i + 1

    if lefts.size() != 0:  # if not lefts.isEmpty():
        match = False

    print(match)
    return match


test = '({[(())()]})'
parcheck(test)
