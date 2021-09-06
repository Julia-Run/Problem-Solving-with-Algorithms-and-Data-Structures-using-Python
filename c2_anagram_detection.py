## 异序词检测，三种方案
# 排序法
def anagram1(s1, s2):
    list1 = list(s1)
    list2 = list(s2)

    list1.sort()
    list2.sort()

    test = True
    i = 0
    while i < len(list1) and test:
        if list1[i] == list2[i]:
            i = i + 1
        else:
            test = False
    print(test)
    return test


# 清点法
def anagram2(s1, s2):
    if len(s1) != len(s2):
        test = False
    else:
        list2 = list(s2)
        i, test = 0, True

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
        # 我第一次写的
        # while i < len(s1) and test:
        #     test = False
        #     j, found = 0, False
        #     while j < len(list2) and not found:
        #         if s1[i] == list2[j]:
        #             found = True
        #             test = True
        #             i = i + 1
        #             list2[j] = None
        #         else:
        #             j = j + 1
    print(test)
    return test


# 计数器法
def anagram3(s1, s2):
    if len(s1) != len(s2):
        test = False
    else:
        c1 = [0] * 26
        c2 = [0] * 26

        for i in range(len(s1)):
            j1 = ord(s1[i]) - ord('a')
            j2 = ord(s2[i]) - ord('a')
            c1[j1] = c1[j1] + 1
            c2[j2] = c2[j2] + 1
        test = True
        j = 0
        while j < 26 and test:  # 可以用range，但range的order是什么目前不确定
            if c1[j] != c2[j]:
                test = False
            else:
                j = j + 1
    print(test)
    return test


# # test
a = 'thisisit'
b = 'thisitis'
anagram3(a, b)
