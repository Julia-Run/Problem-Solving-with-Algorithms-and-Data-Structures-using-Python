from pythonds.basic import Stack


def match3(a, b):
    lefts, rights = '([{', ')]}'
    return lefts.index(a) == rights.index(b)


def parenthesis(s):
    if len(s) % 2 != 0:
        match = False
    else:
        left = Stack()
        i = 0
        match = True
        while i < len(s) and match:
            if s[i] in '({[':
                left.push(s[i])
            else:
                if left.isEmpty():
                    match = False
                else:
                    if not match3(left.pop(), s[i]):
                        match = False
            i = i + 1
        if not left.isEmpty():
            match = False
    print(match)
    return match


test = '(({{}}))'
parenthesis(test)
