# # 1.列表法
# def binary_tree(root):
#     tree = [root, [], []]
#     # print(tree, len(tree), len(tree[1]))
#     # t = tree.pop(1)
#     # print(t, len(t), tree)
#     return tree
#
#
# def insert_left_child(root, left_child):
#     t = root.pop(1)
#     if len(t) > 1:  # 左子树至少有三个元素，这里可以是0，1，2
#         root.insert(1, [left_child, t, []])
#     else:
#         root.insert(1, [left_child, [], []])
#     return root
#
#
# def insert_right_child(root, right_child):
#     t = root.pop(2)
#     if len(t) > 1:  # 左子树至少有三个元素，这里可以是0，1，2
#         root.insert(2, [right_child, [], t])
#     else:
#         root.insert(2, [right_child, [], []])
#     return root
#
#
# def get_root_val(root):
#     return root[0]
#
#
# def set_root_val(root, new):
#     root[0] = new
#
#
# def get_left_child(root):
#     return root[1]
#
#
# def get_right_child(root):
#     print(root[2])
#     return root[2]
#
#
# binary_tree('animal')
#
# r = binary_tree(3)
# insert_right_child(r, 90)
# insert_right_child(r, 'next')
# set_root_val(r, 'head')
# get_right_child(r)
# print(r)


# 节点法：
class Tree2():
    def __init__(self, root):
        self.data = root
        self.left = None
        self.right = None

    def insert_left(self, newleft):
        if self.left is None:
            self.left = Tree2(newleft)
        else:
            t = Tree2(newleft)
            t.left = self.left
            self.left = t

    def insert_right(self, newright):
        if self.right is None:
            self.right = Tree2(newright)
        else:
            t = Tree2(newright)
            t.right = self.right
            self.right = t

    def get_root(self):
        return self.data

    def set_root(self, newroot):
        self.data = newroot

    def get_right(self):
        return self.right
        # return self.right.data  只能返回当前最新的data


r = Tree2(3)
r.insert_right(90)
r.insert_right('next')
r.set_root('head')

print(r.get_right())
print(r.get_root())

# print()
# print()
print(r)
