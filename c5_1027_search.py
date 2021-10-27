# 无序列表的顺序搜索
def search1(alist, item):
    found = False
    i = 0
    while i < len(alist) and not found:
        if item == alist[i]:
            found = True
            pos = i
        i += 1
    #   return found
    return pos


test_list1 = [1, 5, 7, 3, 5, 711, 3, 45]
print(search1(test_list1, 1))


# 有序列表的顺序搜索
def search2(alist, item):
    found = False
    i = 0
    stop = False
    while i < len(alist) and not found and not stop:
        if alist[i] == item:
            found = True
        elif alist[i] > item:
            stop = True
        else:
            i += 1
    # return found
    return i


test_list2 = [1, 5, 7, 11, 71, 223, 345]
print(search2(test_list2, 71))


# 3. 有序列表的二分搜索
def search3(alist, item):
    start = 0
    end = len(alist) - 1
    found = False
    mid = (start + end) // 2

    while end - start > 0 and not found:
        if item == alist[mid]:
            found = True
        else:
            if item < alist[mid]:
                end = mid - 1
            else:
                start = mid + 1
            mid = (start + end) // 2
    return mid


test_list3 = [1, 5, 7, 11, 71, 223, 345]
print(search3(test_list3, 1))


# 4. 二分搜索的递归版本
def search4(alist, item):
    if len(alist) == 0:
        return False
    else:
        mid = (0 + len(alist) - 1) // 2
        if item == alist[mid]:
            return True

        else:
            if item < alist[mid]:
                return search4(alist[0:mid], item)
            else:
                return search4(alist[mid + 1:], item)


test_list4 = [1, 5, 7, 11, 71, 223, 345]
print(search4(test_list4, 223))


# 散列表、 哈希表？ hashtable。以更便于查找的方式储存。 尺寸一般为素数
# 散列函数：将元素与其所属位置对应。：将元素映射存储位址空间，最简单常见的为取散列表尺寸的余数
# 载荷因子
# 完美散列函数：每个元素银蛇到不同的槽。--》对任意给定的元素集合，并不不通用，会冲突。于是产生目标：
#       1.创建一个散列函数：冲突最少，计算方便，元素均匀分布不聚集
#           1.折叠法：data:522-98-27  pos:(522+98+27)%size
#           2.平方取中：data:44  pos:44*2=1936, 93%size
#           3.基于元素为字符串：pos： ord（‘str’）（乘以字符位置比重）求和为x, pos=x%size
#       2.处理冲突:找新的位置安排hash值相同的元素--开放定址：
#           1.线性探测：顺序遍历列表，直到找到下一个空槽 -- 缺点：出现聚集
#           2.避免聚集--》再散列：
#               1.扩展线性探测：不顺序逐个遍历，跳过一些空槽。eg +3
#               2.平方探测：h+1,h+4,h+9,h+16......
#               3.链表法，在同样的位n置添加链表

# 抽象映射数据类型（举例：字典）
# Map()  /.put(key,value)  /.get(key)  /del map(key)  /len()  /key in map
# 字典可以用两个list生成：
class HashTable:
    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size  # 储存key（依据k的hashnumber）
        self.data = [None] * self.size  # 储存data（依据k的hashnumber）

    # def put(self, key, value):
    #     # 处理冲突，采用顺序查找法**************************************************************
    #     hashnumber = self.hashnum(key)
    #     if self.slots[hashnumber] is None:
    #         self.slots[hashnumber] = key
    #         self.data[hashnumber] = value
    #     else:
    #         if self.slots[hashnumber] == key:
    #             self.data[hashnumber] = value
    #         else:
    #             i = 1
    #             put = False
    #             while i < self.size and not put:
    #                 if hashnumber == self.size - 1:
    #                     hashnumber = 0
    #                 else:
    #                     hashnumber += 1
    #                 if self.slots[hashnumber] is None:
    #                     self.slots[hashnumber] = key
    #                     self.data[hashnumber] = value
    #                     put = True
    #                 i += 1
    #             if put is False:
    #                 print('No More Space, "%s : %s" can NOT be put in' % (key, value))

    def hashnum(self, key):
        return key % self.size

    def rehash(self, oldhash):
        return (oldhash + 1) % self.size

    def put(self, key, value):
        # 处理冲突，采用rehash**************************************************************
        hashnumber = self.hashnum(key)
        if self.slots[hashnumber] is None:
            self.slots[hashnumber] = key
            self.data[hashnumber] = value
        else:
            if self.slots[hashnumber] == key:
                self.data[hashnumber] = value
            else:
                newhash = self.rehash(hashnumber)
                while self.slots[newhash] is not None and self.slots[newhash] != key:
                    newhash = self.rehash(newhash)
                if self.slots[newhash] is None:
                    self.slots[newhash] = key
                    self.data[newhash] = value
                else:
                    self.data[hashnumber] = value

    def __setitem__(self, key, value):
        return self.put(key, value)


H = HashTable(11)
H[54] = "cat"
H[26] = "dog"
H[21] = 'duck'
H[11] = 'monkey'
H[93] = "lion"
H[20] = "chicken"
print(H.slots, H.data)
for i in range(H.size):
    if H.slots[i] is not None:
        print(H.slots[i], '-->', H.data[i])
