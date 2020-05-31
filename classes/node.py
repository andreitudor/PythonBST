class Node():
  def __init__(self, data):
    self.data = data 
    self.left = None
    self.right = None
    self.parent = None

  def getLeft(self):
    return self.left

  def getRight(self):
    return self.right
  
  def setLeft(self, data):
    self.left = Node(data)

  def setRight(self, data):
    self.right = Node(data)

  def getParent(self):
    return self.parent
  
  def setParemt(self, data):
    self.parent = self

  def getData(self):
    return self.data