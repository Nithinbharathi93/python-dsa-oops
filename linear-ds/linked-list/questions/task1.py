# Merge 2 sorted linked lists and return as a single linked list
# linkedList1 = 10, 50, 70, 90, 100
# linkedList2 = 20, 30, 40, 60, 80

# solution:
# initialize 3 pointers -> s, p, q

# In list1, first element is s, and q in the other list.
# always print S
# always compare P and Q, which ever is smallest, that will become S 
# whenever you assign S to a node, move that respective P or Q to the next node


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print(None)

def merge_linked_list(l1, l2):
    p = l1.head
    q = l2.head
    s = LinkedList()
    while p and q:
        if p.data < q.data:
            s.insert(p.data)
            p = p.next
        else:
            s.insert(q.data)
            q = q.next
    while p:
        s.insert(p.data)
        p = p.next
    while q:
        s.insert(q.data)
        q = q.next
    return s

inp = int(input())
if inp: 
    l1 = list(map(int, input().split()))
else: l1 = []
inp = int(input())
if inp: 
    l2 = list(map(int, input().split()))
else: l2 = []
LL1 = LinkedList()
LL2 = LinkedList()

for i in l1:
  LL1.insert(i)
  
for i in l2:
  LL2.insert(i)

ans = merge_linked_list(LL1, LL2)
ans.display() 