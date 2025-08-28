class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None 
    
    def __insert_recursive(self, curr, new_node):
        if new_node.data < curr.data:
            if not curr.left:
                curr.left = new_node 
            else:
                self.__insert_recursive(curr.left, new_node)
        else:
            if not curr.right:
                curr.right = new_node
            else:
                self.__insert_recursive(curr.right, new_node)
    
    def insert(self, data):
        new_node = Node(data)
        if not self.root:
            self.root = new_node
        else:
            self.__insert_recursive(self.root, new_node)
    
def display_inorder(root):
    if root:
        display_inorder(root.left)
        print(root.data, end=" ")
        display_inorder(root.right)

nodes = [100, 6, 65, 9, 150, 300, 50]
tree = BST()
for i in nodes:
    tree.insert(i)
display_inorder(tree.root)