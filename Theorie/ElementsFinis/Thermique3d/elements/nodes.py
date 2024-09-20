class Node:
    def __init__(self,num,x,y,z):
        self._id = num
        self._x = x
        self._y = y
        self._z = z
    def x(self):
        return self._x
    def y(self):
        return self._y
    def z(self):
        return self._z
    def id(self):
        return self._id

class Nodes(dict):
    def addNode(self,num,node):
        self[num] = node
