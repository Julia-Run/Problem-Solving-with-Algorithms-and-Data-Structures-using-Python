# 异序词检测
# 1.sort法
def anagrem1(s1, s2):
    if len(s1) != len(s2):
        test = False
    else:
        list1, list2 = list(s1), list(s2)
        list1.sort()
        list2.sort()
        i, test = 0, True
        while i < len(list1) and test:
            if list1[i] != list2[i]:
                test = False
            else:
                i = i + 1
    print(test)
    return test


# 清点法
def anagrem2(s1, s2):
    if len(s1) != len(s2):
        test = False
    else:
        list2 = list(s2)
        i = 0
        test = True
        while i < len(s1) and test:
            j = 0
            found = False
            while j < len(list2) and not found:
                if s1[i] == list2[j]:
                    found = True
                else:
                    j = j + 1
            if found:
                list2[j] = None
                i = i + 1
            else:
                test = False
    print(test)
    return test


# 记数法
def anagrem3(s1, s2):
    if len(s1) != len(s2):
        test = False
    else:
        c1 = [0] * 26
        c2 = [0] * 26
        i = 0
        while i < len(s1):
            j1 = ord(s1[i]) - ord('a')
            c1[j1] = c1[j1] + 1
            j2 = ord(s2[i]) - ord('a')
            c2[j2] = c2[j2] + 1
            i = i + 1
        test = True
        while i < 26 and test:
            if c1[i] != c2[i]:
                test = False
            else:
                i = i + 1
    print(test)
    return test


a = 'timet'
b = 'imett'
anagrem3(a, b)
