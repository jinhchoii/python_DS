
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None 

    """
    Use recursion to write a search function here to search the target on the current node, left side of the tree, and right side of the tree. 
    If the target is found, will print "Found it", otherwise print "Not found"
    """
    def search(self, target):
        pass
    
    """
    Use recursion write a function to count the height of the tree
    You will need to count both side, and the return the number of the heighter side
    """
    def height(self, h =0):
        pass
    
class Tree:
        def __init__(self, root, name =''):
            self.root = root
            self.name = name
        
        def search(self, target):
            return self.root.search(target)

        def height(self):
            return self.root.height()



print("====== add node =======")

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
#Write your own test case