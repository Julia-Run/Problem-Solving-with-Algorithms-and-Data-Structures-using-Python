# 二叉搜索树，实现映射抽象数据类型。（之前用散列实现过）
# Map()  / put(key,value)  /del amap[key]  / get(key)  /len()  /in
# 二叉搜索树：对任意一个节点，比节点值小的值放在左子值，大的放在右子树，也叫做二叉搜索性
# 必须处理并创建一颗空的二叉树，因此在实现的过程中必须使用两个类，涉及两个类的耦合问题
# put函数，新来的一定被放在最后，无论大小
# me_debug failed
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

    def change_data(self, key, val, new_lc=None, new_rc=None):
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
        self.size += 1  ##########################################forgot

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
            currentNode.change_data(key, val)

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
            self._get(key, current.lc)
        elif key > current.key:
            self._get(key, current.rc)
        else:
            return current

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False


a = SearchTree()
a.put(1, 'A')
a.put(10, 'B')
a.put(-1, 'C')
print(a.size)
print(a.get(10))
print(a.get(1))
print(a.get(12))
