
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None 

    def search(self, target):
        if self.data == target:
            print("Yay! Found it!")
            return self

        if self.left and self.data > target:
            return self.left.search(target)
        
        if self.right and self.data < target:
            return self.right.search(target)
        
        print("Oops! The target is not found")
    
    def height(self, h =0):
        leftHeight = self.left.height(h+1) if self.left else h
        rightHeight = self.right.height(h+1) if self.right else h
        return max(leftHeight, rightHeight)
    
class Tree:
        def __init__(self, root, name =''):
            self.root = root
            self.name = name
        
        def search(self, target):
            return self.root.search(target)

        def height(self):
            return self.root.height()



print("======add node =======")

node = Node(10)
print(node.data)

node.left = Node(5)
print(node.left.data)

node.right = Node(15)
print(node.right.data)

node.left = Node(8)
node.right = Node(50)

node.left = Node(3)
node.right = Node(12)

print("======Test 2 - search item =======")
loveTree = Tree(node, 'Love Tree')
print(loveTree.root.left.data)

found1 = loveTree.root.search(50) #Oops! The target is not found
found2 = loveTree.root.search(3) #Yay! Found it!
found3 = loveTree.root.search(8) #Oops! The target is not found
found4 = loveTree.root.search(5) #Oops! The target is not found
found5 = loveTree.root.search(12) #Yay! Found it!


print("======Test 3 - height =======")
tree = Tree(Node(51), 'A Tall Tree')
tree.root.left = Node(26)
tree.root.right = Node(74)

tree.root.left.left = Node(18)
tree.root.left.right = Node(35)

tree.root.left.right.left = Node(30)
tree.root.left.right.right = Node(42)

tree.root.left.left.left = Node(5)
tree.root.left.left.right = Node(13)
tree.root.left.left.left.left = Node(2)

print(tree.root.height()) # Expect output 4



