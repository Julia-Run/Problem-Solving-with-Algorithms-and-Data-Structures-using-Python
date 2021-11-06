# 图数据结构的实现方案一
# Vertex: id, connetction{vertex:weight,......}
# graph: vertices{id:vertex, ......}

class Vertex(object):
    def __init__(self, id):
        self.id = id
        self.to = {}

    def addconnections(self, ver, weight=0):  # ver是一个vertex
        self.to[ver] = weight

    def getconnections(self):
        return self.to.keys()

    def getweight(self, nrb):
        return self.to[nrb]

    def getid(self):
        return self.id

    def __str__(self):
        return str(self.id) + ' connected to ' + str([x.id for x in self.to])

    __repr__ = __str__


# a = Vertex('test')
# for i in range(6):
#     a.addconnections(Vertex(i), 10)
# print(type(a.getconnections()))
# print([i.getid() for i in a.getconnections()])
# print(a)


class Graph(object):
    def __init__(self):
        self.vertices = {}
        self.num = 0

    def add_vertex(self, k):  # 增加顶点
        self.vertices[k] = Vertex(k)
        self.num += 1

    def add_edge(self, k1, k2, cost=0):  # 增加边
        if k1 not in self.vertices:
            self.vertices[k1] = Vertex(k1)
        if k2 not in self.vertices:
            self.vertices[k2] = Vertex(k2)
        self.vertices[k1].addconnections(self.vertices[k2], cost)

    def getvetices(self):
        return self.vertices.keys()

    def getvertex(self, k):
        if k in self.vertices:
            return self.vertices[k]
        else:
            return None

    def __iter__(self):
        return iter(self.vertices.values())  # return到了节点本身上


a = Graph()
for i in range(6):
    a.add_vertex(i)
a.add_edge(0, 1, 5)
a.add_edge(0, 5, 2)
a.add_edge(1, 2, 4)
a.add_edge(2, 3, 9)
a.add_edge(3, 4, 7)
a.add_edge(3, 5, 3)
a.add_edge(4, 0, 1)
a.add_edge(5, 4, 8)
a.add_edge(5, 2, 1)
for i in a:
    print(i)
for i in a:
    print('Node', i.id, ':')
    for j in i.to:
        print('    ', i.id, '-->', j.id, ': ', i.to[j])
