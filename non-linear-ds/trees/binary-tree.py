class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None 

# 10 20 30 40 50 60
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)
node6 = Node(60)

# Edges
 
# Root
root = node1
# Intermediate
root.left = node2
root.right = node3
# leaf
node2.left = node4
node2.right = node5
# right
node3.left = node6