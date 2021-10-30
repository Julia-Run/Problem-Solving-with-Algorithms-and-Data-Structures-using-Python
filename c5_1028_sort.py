# 冒泡排序效率最低，金莲少用。选择排序相对冒泡排序，交换次数更少，快一点。
# 插入排序不适用交换，只进行移动操作（时间是交换的1/3），性能比较好，
# ·     所以再希尔排序中，备份功能尽量使用插入排序
# 1.冒泡排序
def bubble(alist):
    times = len(alist) - 1
    for unranked_len in range(times, 0, -1):  # 此处0不被包括早内
        for i in range(unranked_len):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
    return alist


test_list1 = [12, 5, 7, 3, 5, 711, 3, 45]
print(bubble(test_list1))


# 1.冒泡排序 -- 短冒泡
def bubble1(alist):
    times = len(alist) - 1
    exchange = True
    while times > 0 and exchange:
        exchage = False
        for i in range(times):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                exchage = True
        times -= 1
    return alist


test_list2 = [12, 5, 7, 3, 5, 711, 3, 45]
print(bubble1(test_list2))


# 2.选择排序
def choose(alist):
    times = len(alist) - 1
    for unranked_len in range(times, 0, -1):
        maxpos = 0
        for i in range(unranked_len):
            if alist[i + 1] > alist[maxpos]:
                maxpos = i + 1
        alist[unranked_len], alist[maxpos] = alist[maxpos], alist[unranked_len]
    return alist


test_list3 = [12, 5, 7, 3, 5, 711, 3, 45]
print(choose(test_list3))


# 3..插入排序
def insert(alist):
    for current in range(1, len(alist)):
        temp = current
        putin = False
        while temp > 0 and not putin:
            if alist[temp] < alist[temp - 1]:  # 采用了交换，本质上是一种冒泡排序的变体，通过冒泡插入
                alist[temp], alist[temp - 1] = alist[temp - 1], alist[temp]
            else:
                putin = True
            temp -= 1
    return alist


# 3. 插入排序，frombook
def insert1(alist):
    for current_pos in range(1, len(alist)):
        current_value = alist[current_pos]  # 存储当前计算值
        pos = current_pos
        while pos > 0 and current_value < alist[pos - 1]:
            alist[pos] = alist[pos - 1]  # 将前一位置上上更大的值移动到当前位置，前一位置空出
            pos -= 1  # pos指向空位
        alist[pos] = current_value
    return alist


test_list4 = [12, 5, 7, 3, 5, 711, 3, 45]
print(insert(test_list4))


# 4. 希尔排序
# n/2，n/4,
# a.步长为n//2， 每个子列表排序,得到新的列表
# b。 步长为n/4, 每个子列表排序,得到新的列表
# 直到步长为1
# def shellonce(alist, k):
#     gap = len(alist) // 2 ** k
#     for i in range(gap):
#         index = i
#         while index + gap < len(alist):
#             if alist[index] > alist[index + gap]: # 冒泡排序效率最低，尽量少用,可修该为插入法
#                 alist[index + gap], alist[index] = alist[index], alist[index + gap]
#             index = index + gap
#     return alist
#
#
# def shell(alist):
#     k = 1
#     while len(alist) // 2 ** k > 0:
#         alist = shellonce(alist, k)
#         k += 1
#     return alist

def shell(alist):
    gap = len(alist) // 2
    while gap > 0:
        for i in range(gap, len(alist)):  # 这个写的应该是不对的吧。。。。。。
            pos = i
            current_value = alist[pos]
            while pos >= gap and current_value < alist[pos - gap]:
                alist[pos] = alist[pos - gap]
                pos = pos - gap
            alist[pos] = current_value
        gap = gap // 2
    return alist


test_list5 = [12, 5, 7, 11, 5, 711, 3, 4, 5, 6, 6, 7, 7, 8, 8, 33, 55, 77, 89, 45]
print(shell(test_list5))


def shell2(alist):
    gap = len(alist) // 2
    while gap > 0:
        for i in range(gap):
            for j in range(i + gap, len(alist), gap):
                pos = j  # first need comparetion
                current_value = alist[pos]
                while pos >= gap and current_value < alist[pos - gap]:
                    alist[pos] = alist[pos - gap]
                    pos = pos - gap
                alist[pos] = current_value
        gap = gap // 2
    return alist


test_list5 = [12, 5, 7, 11, 5, 711, 3, 4, 5, 6, 6, 7, 7, 8, 8, 33, 55, 77, 89, 45]
print(shell2(test_list5))


# 归并排序
def merge(alist):
    # 拆分成两个list，一直拆到最小一个元素的情况，比较大小
    # 再将两个list融合再一起
    lens = len(alist)
    if lens > 1:
        mid = lens // 2
        left = alist[:mid]
        right = alist[mid:]
        merge(left)
        merge(right)

        i, j, k, = 0, 0, 0
        # 先比较左边的最下面的两个左右分支
        # 左右只有一个元素，只比较一次，向上返回一级，要再比较左右，各有两个元素。。。。。。
        # 整体左边排序完成后，开始分离并排序右边
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                alist[k] = left[i]
                i = i + 1
            else:
                alist[k] = right[j]
                j = j + 1
            k = k + 1
        while i < len(left):
            alist[k] = left[i]
            i = i + 1
            k = k + 1
        while j < len(right):
            alist[k] = right[j]
            j = j + 1
            k = k + 1
    return alist


test_list5 = [12, 5, 7, 11, 5, 711, 3, 4, 5, 6, 6, 7, 7, 8, 8, 33, 55, 77, 89, 45]
print(merge(test_list5))


# 快速排序
def splitpoint(alist, start, end):
    # 锁定分割位的index
    key = alist[start]
    left, right = start + 1, end
    found = False
    while not found:
        while left <= right and alist[left] <= key:
            left += 1
        while right >= left and alist[right] >= key:
            right = right - 1
        if left < right:
            alist[left], alist[right] = alist[right], alist[left]
        else:
            found = True
    if found:
        alist[0], alist[right] = alist[right], alist[0]
    return right


def quick(alist):
    maincode(alist, 0, len(alist) - 1)


def maincode(alist, start, end):
    # 分割,得到分割位置的index
    # 左分割，直到左边排序完成，如何确定左排序完成？
    # 右分割直到右边排序完成
    while start < end:
        p = splitpoint(alist, start, end)
        maincode(alist, start, p - 1)
        maincode(alist, p + 1, end)
    return alist


test_list5 = [12, 5, 7, 11, 5, 711, 3, 4, 5, 6, 6, 7, 7, 8, 8, 33, 55, 77, 89, 45]
print(quick(test_list5), 'test')
