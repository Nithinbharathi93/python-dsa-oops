# heap = []
# def heapin(i):
#     heap.append(i)
#     i = len(heap)-1
#     while i>0 and heap[(i-1)//2]>heap:
#         heap[i], heap[(i-1)//2] = heap[(i-1)//2], heap[i]
#         i - (i-1)//2

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None 

def is_heap(node):
    queue = [node]
    while any(queue):
        curr = queue.pop(0)
        
        if curr and curr.left:
            if not curr.left.data < curr.data:
                return False
            else:
                queue.append(curr.left)
        if curr and curr.right:
            if not curr.right.data < curr.data:
                return False
            else:
                queue.append(curr.right)
    return True

def heapify(root):
    if not root:
        return None
    queue = [root]
    while queue:
        curr = queue.pop(0)
        largest = curr 
        
        if curr.left and curr.left.data > largest.data:
            largest = curr.left
        elif curr.right and curr.right.data > largest.data:
            largest = curr.right

        if largest != curr:
            largest.data, curr.data = curr.data, largest.data
        
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
    if not is_heap(root):
        heapify(root)
    return root

def display(root):
    queue = [root]
    while queue:
        curr = queue.pop(0)
        print(curr.data, end=" ")
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)        

root = Node(17)
root.left = Node(1)
root.right = Node(3)
root.left.left = Node(25)
print(is_heap(root))
sorted_heap = heapify(root)
display(sorted_heap)