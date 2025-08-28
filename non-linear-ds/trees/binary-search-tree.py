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
    
    def search_bst(self, data):
        if not self.root:
            return False
        temp = self.root
        while temp:
            if data == temp.data:
                return True
            if data < temp.data:
                temp = temp.left 
            else:
                temp = temp.right 
        return False

    def delete(self, data):
        sub_prev = Node(None)
        if self.search_bst(data):
            temp = self.root
            while temp:
                prev = temp
                if data == temp.data:
                    print(f"Found {data} with parent {prev.data}")
                    
                    if temp.left:
                        sub_temp = temp.left
                        sub_prev.data = temp.data
                        while sub_temp:
                            if sub_temp.right:
                                sub_prev = sub_temp
                                sub_temp = sub_temp.right 
                            else:
                                break
                        temp.data = sub_temp.data
                        if sub_prev.data != temp.left.data:
                            print("inga")
                            temp.left = None
                        else:
                            print("anga")
                            sub_prev.right = None

                    elif temp.right:
                        sub_temp = temp.right
                        sub_prev.data = temp.data
                        while sub_temp:
                            if sub_temp.left:
                                sub_prev = sub_temp
                                sub_temp = sub_temp.left
                            else:
                                break
                        temp.data = sub_temp.data
                        if sub_prev.data != temp.right.data:
                            print("inga")
                            temp.right = None
                        else:
                            print("anga")
                            sub_prev.left = None
                    return
                elif data < temp.data:
                    temp = temp.left 
                else:
                    temp = temp.right
    
def display_inorder(root):
    if root:
        display_inorder(root.left)
        print(root.data, end=" ")
        display_inorder(root.right)

def display_level_order(node):
    queue = [node]
    while queue:
        curr = queue.pop(0)
        print(curr.data, end=" ")
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)

# def vera_maari_vera_maari(node):
#     queue = []
#     queue.append([node])
#     count = 0
#     while queue[count]:
#         if queue[count]:
#             curr = queue[count].pop(0)
#         if not queue[count] or not all(i for i in queue[count]):
#             count += 1
#             queue.append([])
#             if curr:
#                 queue[-1].extend([curr.left, curr.right])
#                 print(curr.left.data, curr.right.data)
#             else:
#                 if queue[count]:
#                     queue[count].pop(0)
#         print(queue)
#     print(count-1)


nodes = [100, 4, 200, 2, 6, 150, 300, 1, 3, 7]
nodes = [1, 2, 12, 45, 6, 77]
tree = BST()
for i in nodes:
    tree.insert(i)
display_inorder(tree.root)
print()
display_level_order(tree.root)
print()
print("Found" if tree.search_bst(45) else "Not Found")
tree.delete(45)
display_inorder(tree.root)
print()
display_level_order(tree.root)
print()
vera_maari_vera_maari(tree.root)