class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None 
    def __repr__(self):
        return str(self.data)

# Level order insertion
def insert(data):
    if not data:
        return None
    root = Node(data[0])
    i = 1
    queue = [root]
    q_index = 0
    while i<len(data):
        curr = queue[q_index]
        q_index += 1

        if i<len(data):
            curr.left = Node(data[i])
            queue.append(curr.left)
            i += 1
        if i<len(data):
            curr.right = Node(data[i])
            queue.append(curr.right)
            i += 1
    return root


def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)

def level_order(node):
    queue = [node]
    while queue:
        curr = queue.pop(0)
        print(curr.data, end=" ")
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)


def count_level(node):
    queue = []
    queue.append([node])
    count = 0
    while queue[count]:
        if queue[count]:
            curr = queue[count].pop(0)
        if not queue[count] or not all(i for i in queue[count]):
            count += 1
            queue.append([])
            if curr:
                queue[-1].extend([curr.left, curr.right])
            else:
                if queue[count]:
                    queue[count].pop(0)
        print(queue)
    print(count-1)

# 10 20 30 40 50 60 70
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)
node6 = Node(60)
node7 = Node(70)

# Edges

nodes = [1, 2, 3, 4, 5, 6, 7, 8]

root = insert(nodes)

inorder(root)
print()

count_level(root)