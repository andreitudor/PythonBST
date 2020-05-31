from .node import Node

class BinarySearchTree:
  def __init__(self):
    self.root = None
    self.size = 0

  def getRoot(self):
      return self.root

  def add(self, data):
    print("adding", data)
    if self.root is None:
      self.root = Node(data)
      print("root ", self.root.getData())
      self.size += 1
      return
    else:
      self._add(data, self.root)

  def _add(self, data, nodeR):
    if data < nodeR.getData():
      if nodeR.getLeft() is not None:
        print("go left ", nodeR.getData(), " => ", nodeR.getLeft().getData())
        self._add(data, nodeR.getLeft())
      else:
        print("insert left")
        nodeR.setLeft(data)
        print("left data ", nodeR.getLeft().getData())
        self.size += 1
    elif data > nodeR.getData():
      if nodeR.getRight() is not None:
        print("go right", nodeR.getData(), " => ", nodeR.getRight().getData())
        self._add(data, nodeR.getRight())
      else:
        print("insert right")
        nodeR.setRight(data)
        print("right data ", nodeR.getRight().getData())
        self.size += 1
    return

  """ Inorder traversal of a binary tree"""
  def inorder(self):
    self._inorder(self.root)

  def _inorder(self, node):
    if (not node): 
        return
    self._inorder(node.getLeft())
    print(node.data,end = " ")
    self._inorder(node.getRight())

  def contains(self, data):
    if self.root is None:
      return False
    else:
      print("root not none ", data, self.root.getData())
      # print(self._contains(data, self.root))
      return self._contains(data, self.root)

  def _contains(self, data, node):
    print(node.getData())
    if node is None:
      return False
    if node.getData() == data:
      print("node.getData() == data ", node.getData(), data)
      return True
    elif data < node.getData():
      print("data < node.getData() ", node.getData(), data)
      return self._contains(data, node.getLeft())
    elif data > node.getData():
      print("data > node.getData() ", node.getData(), data)
      return self._contains(data, node.getRight())

    return False
