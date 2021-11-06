# 宽度优先--词梯问题--没有这个整体词包的file
# 创建桶+构图。color（白灰黑）。 pred。 distance（height of tree）. + 回溯
from pythonds.graphs import Graph, Vertex
from pythonds.basic import Queue


def buildGraph(filename):
    # 创建桶 + 构图
    pool = {}
    g = Graph()
    file = open(filename, 'r')
    for line in file:
        word = str(line)
        # word=lin[:-1]
        for i in range(len(word)):
            tag = word[:i] + '_' + word[i + 1:]
            if tag not in pool:
                pool[tag] = [word]
            else:
                pool[tag].append(word)
    for tags in pool:
        for word1 in tags:
            for word2 in tags:
                if word1 != word2:
                    g.addEdge(word1, word2)
    return g


def bfs(g, s):
    # color（白灰黑）。 pred。 distance（height of tree）
    pathpool = Queue()
    s.setColor('gray')
    s.setDistance(0)
    s.setPred(None)
    pathpool.enqueue(s)
    while pathpool.size() > 0:
        current = pathpool.dequeue()  # vertex
        for i in current.getConnections():
            if i.getColor() == 'white':
                i.setColor('gray')
                i.setDistance(current.getDistance() + 1)
                i.setPred(current)
                pathpool.enqueue(i)
        current.setColor('black')
    return current  # 最后一个vertex，也是最终结果


def goback(last):
    # 回溯
    temp = last
    while temp.getaPred():
        print(temp.getId())
        temp = temp.getaPred()
    print(temp.getId())


# 骑士周游问题（递归、wornsdorff（向可行位置最小的方向走））
# 创建图。
#   在每个点，都有8个可能的移动方案，选出所有可行移动方案（下一个节点），在两个节点之间添加edge
def buildG(size):
    g = Graph()
    for row in range(size):
        for col in range(size):
            posid = pos2id(row, col)  # name for a point
            nexts = moves(row, col, size)
            for p in nexts:
                nid = pos2id(p[0], p[1])
                g.addEdge(posid, nid)
    return g


def pos2id(r, c):
    return 'g_' + str(r + 1) + str(c + 1)


def moves(r, c, size):
    next_p = []
    delta = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (-2, 1), (-2, -1), (2, -1)]
    for i in delta:
        r = r + i[0]
        c = c + i[1]
        if size > r >= 0 and size > c >= 0:
            next_p.append((r, c))
    return next_p


g1 = buildG(5)


# 深度优先算法--递归
def move(n, s, path, limit):  # path is Stack# ,s is vertex
    s.setColor('gray')
    path.push(s)
    if n < limit:
        nbs = list(s.getConnections())
        # nbs = quick(s)  # wornsdorff算法快速找出路
        i = 0
        found = False
        while i < len(nbs) and not found:
            if nbs[i].getColor() == 'white':  # 如果一个点的nbs中没有white，会return false
                move(n + 1, nbs[i], path, limit)
            i += 1
        if not found:  # 在当前节点没找到，则准备回溯
            path.pop()
            s.setColor('white')
    else:
        found = True
    return found


# wornsdorff
def quick(current):
    res = []
    for i in current.getConnections():
        space = 0
        for j in i.getConnections():
            if j.getColor() == 'white':
                space = space + 1
        res.append([space, i])
    res.sort(key=lambda x: x[0])
    resf = [i[1] for i in res]
    return resf

# 通用深度有限算法
# 深度优先森林+前驱动+时间
