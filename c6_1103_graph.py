# 图数据结构的实现方案一
# Vertex: id, connetction{vertex:weight,......}
# graph: vertices{id:vertex, ......}

class Vertex(object):
    def __init__(self, id):
        self.id = id
        self.to = {}

    def addconnections(self, ver, weight=0):
        self.to[ver] = weight

    def getconnections(self):
        return self.to.keys()

    def getweight(self, nrb):
        return self.to[nrb]

    def __str__(self):
        return str(self.id) + ' connected to ' + str(x.id for x in list(self.to.keys()))

    __repr__ = __str__


a = Vertex('test')
for i in range(6):
    a.addconnections(Vertex(i), 10)

print(type(a.getconnections()))
print(a.getconnections())
print(a)
