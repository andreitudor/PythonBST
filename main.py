from classes.tree import BinarySearchTree

tree = BinarySearchTree()

print("12")
tree.add(40)
tree.add(20)
tree.add(10)
tree.add(5)
tree.add(30)
tree.add(50)
tree.add(60)
tree.add(67)
tree.add(78)
tree.inorder()

print (tree.contains(78))