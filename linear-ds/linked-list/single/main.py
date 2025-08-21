class Node:
    
     def __init__(self, data):
        self.data = data
        self.next = None 

class LinkedList:
    
    def __init__(self):
        self.head = None 
    
    #insert at last
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
            print(temp.data, "->", end=" ")
            temp = temp.next
        print("None")
    
    # delete element based on value
    def delete(self, fnd):
        temp = self.head
        if not self.head:
            print("Element not found in Linked List")
            return
        if temp.data == fnd:
            self.head = self.head.next
        else:
            prev = self.head
            curr = prev.next
            while curr:
                if curr.data == fnd:
                    prev.next = curr.next
                    print("Deleted", fnd)
                    return
                prev = curr
                curr = curr.next
            print("Element not found in Linked List")
        
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    
    def insert_at_position(self, data, pos):
        new_node = Node(data)
        count = 2
        temp = self.head
        while count<pos:
            count += 1
            temp = temp.next
        print("Namma data",temp.data)
        new_node.next = temp.next
        temp.next = new_node
    
    def delete_first(self):
        self.head = self.head.next
    
    def delete_last(self):
        prev = temp = self.head
        if not self.head:
            return
        while temp.next:
            prev = temp
            temp = temp.next
        if prev.next:
            print("Deleted", prev.next.data)
            prev.next = None
        else:
            self.head = None
    
    def delete_at_pos(self, pos):
        prev = temp = self.head
        while pos-1>0:
            pos -= 1
            prev = temp
            temp = temp.next
        prev.next = temp.next
        print("Deleted", temp.data)

myLinkedList = LinkedList()
myLinkedList.insert(100)
myLinkedList.insert(200)
myLinkedList.insert(300)
myLinkedList.insert(400)
myLinkedList.insert(500)
myLinkedList.display()

print(f"\nInserting {1} in beginning")
myLinkedList.insert_at_beginning(1)
myLinkedList.display()
print(f"\nInserting 2 at pos 3")
myLinkedList.insert_at_position(2, 2)
myLinkedList.display()
print(f"\nInserting 3 in the end")
myLinkedList.insert(3)
myLinkedList.display()
print("\nDeleting part")
myLinkedList.delete_first()
myLinkedList.display()
myLinkedList.delete_last()
myLinkedList.display()
myLinkedList.delete(300)
myLinkedList.display()
myLinkedList.delete_at_pos(3)
myLinkedList.display()

# l = [1, 2, 3, 4, 5, 6, 7]

# for i in l:
#     myLinkedList.insert_at_beginning(i)
# myLinkedList.display()

myLinkedList.insert_at_position(100, 4)
myLinkedList.display()

myLinkedList.insert(23)
