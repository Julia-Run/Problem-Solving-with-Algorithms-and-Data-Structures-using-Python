# 二叉搜索树，实现映射抽象数据类型。（之前用散列实现过）
# Map()  / put(key,value)  /del amap[key]  / get(key)  /len()  /in
# 二叉搜索树：对任意一个节点，比节点值小的值放在左子值，大的放在右子树，也叫做二叉搜索性
# 必须处理并创建一颗空的二叉树，因此在实现的过程中必须使用两个类，涉及两个类的耦合问题
# put函数，新来的一定被放在最后，无论大小
class TreeNode(object):
    def __init__(self, key, val, lc=None, rc=None, par=None):
        self.key = key
        self.val = val
        self.lc = lc
        self.rc = rc
        self.par = par

    def has_lc(self):
        return self.lc

    def has_rc(self):
        return self.rc

    def has_child(self):
        return self.lc or self.rc

    def has_2child(self):
        return self.lc and self.rc

    def is_root(self):
        return self.par is None

    def is_lc(self):
        return self.par is not None and self.par.lc is self

    def is_rc(self):
        return self.par is not None and self.par.rc is self

    def is_leaf(self):
        return self.lc is None and self.rc is None

    def set_lc(self, lc):
        self.lc = lc

    def set_rc(self, rc):
        self.lc = rc

    def change_data(self, key, val, new_lc, new_rc):
        self.key = key
        self.val = val
        self.lc = new_lc
        self.rc = new_rc
        if self.has_lc():  ################################################## 为什么呀下面这四句
            self.lc.par = self
        if self.has_rc():
            self.rc.par = self


class SearchTree(object):
    def __init__(self):  # 初始化
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()  #################################################

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            aNode = TreeNode(key, val)
            self.root = aNode
        self.size = self.size + 1  ##########################################forgot

    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.has_lc():
                self._put(key, val, currentNode.lc)
            else:
                currentNode.lc = TreeNode(key, val, par=currentNode)  # #################################### par loose
        elif key > currentNode.key:
            if currentNode.has_rc():
                self._put(key, val, currentNode.rc)
            else:
                currentNode.rc = TreeNode(key, val, par=currentNode)  ################################struggle
        else:
            currentNode.change_data(key, val, currentNode.lc, currentNode.rc)

    def __setitem__(self, key, val):  ## ######################################## why return that?
        return self.put(key, val)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.val
            else:
                return None
        else:
            return None

    def _get(self, key, current):
        if current is None:  ############################### 出错 if current.key is None:。没有空白，空白即是None
            return None
        elif key < current.key:
            return self._get(key, current.lc)  ########  掉了return！！！！！！！！！！！！！！！！！！ 检查了至少两个半小时。。。。。。
            # 会在这一步得到return的正确值，但_get函数没有返回值！！是None，所以除了第一个，其他结果查出来都是None
        elif key > current.key:
            return self._get(key, current.rc)  ########   掉了return！！！！！！！！！！！！！！！！！！
        else:
            return current

    def __getitem__(self, key):
        return self.get(key)

    #
    # def __contains__(self, key):
    #     if self._get(key, self.root):
    #         return True
    #     else:
    #         return False
    ######定义一个delete函数
    def successor(self, nodenow):  # 右边最小值
        successor = nodenow.rc
        while successor.lc:
            successor = successor.lc
        return successor.key

    def precessor(self, nodenow):  # 左边最大值
        precessor = nodenow.lc
        while precessor.rc:
            precessor = precessor.rc
        return precessor.key

    def delete(self, key):
        # 11.01  今天未测试delete#################################################################################
        # 1.是叶子，直接删除。
        # 2.不是叶子，使用递归
        #   1.如果有右子节点，找到successor，替代当前点的key/val,在子树中再用下一个node替代successo，直到下一个Node is None--> 循环--》 直到左右节点都是None
        #   2.如果有左节点，找precessor,替代当前点的key/val,
        if self.root:
            pos = self._get(key, self.root)
            if pos:
                self.delnode(pos)
            else:
                print('key is not in this data!')
        else:
            return None

    def delnode(self, pos):
        if pos.isLeaf():
            pos = None
        else:
            if pos.has_rc():
                new_pos = self.successor(pos)
            else:
                new_pos = self.precessor(pos)
            pos.key = new_pos.key
            pos.val = new_pos.val
            return self.delnode(new_pos)


a = SearchTree()
a.put(1, 'A')
a.put(10, 'B')
a.put(-1, '[[[C]]]')
print(a.size)
print(a.get(10))
print(a.get(1))
print(a[-1])
