class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None 
    
class DoubleLinkedList:
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
            new_node.prev = temp
    
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print(None)
    
    def insert_at_begin(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
    def insert_at_pos(self, data, pos):
        new_node = Node(data)
        if not self.head:
            self.head = new_node

        temp = self.head

        while pos-1 > 1:
            pos -= 1
            temp = temp.next

        new_node.next = temp.next
        temp.next.prev = new_node

        new_node.prev = temp.next
        temp.next = new_node
    
    def split_half(self):
        count = 0
        temp = self.head
        while temp:
            temp = temp.next
            count += 1
        temp = self.head
        for i in range(count//2+1):
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("NULL")
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("NULL")
    

l = [1,2,3,4,5]
myDL = DoubleLinkedList()
for i in l:
    myDL.insert(i)
# myDL.display()
# myDL.insert_at_pos(10, 3)
# myDL.display()
myDL.split_half()