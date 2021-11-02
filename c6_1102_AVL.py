# AVL tree： 限制了树高度，从而限制了计算的复杂度
# 如何实现
# 1.是一种特殊的二分搜索树，--满足二分搜索树的基本规则
# 2. 多加入平衡因子的参数，平衡态，平衡因子为0，-1，+1.放入新参数的时候，如果平不平衡，要左再平衡
# 3. 再平衡：左右旋，如果某子树右倾（小于2），需要左旋，要先检查其右子树的状态，如果右子节点需要右旋（大于0），必须先对右子树右旋，再对子树左旋。
class TreeNode(object):
    def __init__(self, key, val, b=0, lc=None, rc=None, par=None):  # 初始化lc,rc,par, (node or None)
        self.key = key
        self.val = val
        self.lc = lc
        self.rc = rc
        self.par = par
        self.b = b

    def isleaf(self):
        return self.lc is None and self.rc is None

    def isroot(self):
        return self.par is None

    def islc(self):
        return self.par is not None and self.par.lc == self

    def isrc(self):
        return self.par is not None and self.par.rc == self

    def haslc(self):
        return self.lc

    def hasrc(self):
        return self.rc

    def haschild(self):
        return self.lc or self.rc

    def has2child(self):
        return self.lc and self.rc

    def replace_data(self, k, v, lc, rc):
        self.key = k
        self.val = v
        self.lc = lc
        self.rc = rc
        if self.lc:
            self.lc.par = self
        if self.rc:
            self.rc.par = self


class BinaryTreeAVL(object):
    def __init__(self):  # 初始化
        self.root = None  # root是一个treenode
        self.size = 0

    # 1.是一种特殊的二分搜索树，--满足二分搜索树的基本规则
    # 2. 多加入平衡因子的参数，平衡态，平衡因子为0，-1，+1.放入新参数的时候，如果平不平衡，要左再平衡
    # 3. 再平衡：左右旋，如果某子树右倾（小于2），需要左旋，要先检查其右子树的状态，如果右子节点需要右旋（大于0），必须先对右子树右旋，再对子树左旋。
    def put(self, k, v):
        if not self.root:
            self.root = TreeNode(k, v)
        else:
            self._put(k, v, self.root)
        self.size += 1

    def _put(self, k, v, start_node):
        if k < start_node.key:
            if start_node.haslc():
                return self._put(k, v, start_node.lc)
            else:
                start_node.lc = TreeNode(k, v, par=start_node)
                self.updatebalance(start_node)
        elif k > start_node.key:
            if start_node.hasrc():
                return self._put(k, v, start_node.rc)
            else:
                start_node.rc = TreeNode(k, v, par=start_node)
                self.updatebalance(start_node)
        else:
            start_node.replace_data(k, v, start_node.lc, start_node.rc)

    def updatebalance(self, anode):  # 更新参数 、再更新
        if anode.b < -1 or anode.b > 1:  # 先对当前节点进行再平衡
            self.rebalence(anode.par)
        if anode.par is not None:
            if anode.islc():
                anode.par.b += 1
            else:
                anode.par.b -= 1
            if anode.par.b != 0:
                return self.updatebalance(anode.par)

    def rotate_right(self, old):
        new = old.lc
        if new.rc is not None:
            old.lc = new.rc
            new.rc.par = old
        if old.par is not None:
            if old.par.rc == old:
                old.par.rc = new
            else:
                old.par.lc = new
        else:
            self.root = new
        new.par = old.par
        new.rc = old
        old.par = new
        old.b = old.b + 1 - min(0, new.b)
        new.b = new.b + 1 + max(0, old.b)

    def rotate_left(self, old):
        # old右，old par
        # new left， new par
        # old。par   left、right
        new = old.rc
        if new.lc is not None:
            old.rc = new.lc
            new.lc.par = old
        if old.par is not None:
            if old.par.lc == old:
                old.par.lc = new
            else:
                old.par.rc = new
        else:
            self.root = new
        new.par = old.par
        new.lc = old
        old.par = new
        old.b = old.b + 1 - min(0, new.b)
        new.b = new.b + 1 + max(0, old.b)

    def rebalence(self, anode):
        if anode.b < 0:
            if anode.rc.b > 0:
                self.rotate_right(anode.rc)
                self.rotate_left(anode)
            else:
                self.rotate_left(anode)
        else:
            if anode.lc.b < 0:
                self.rotate_left(anode.lc)
                self.rotate_right(anode)
            else:
                self.rotate_right(anode)
