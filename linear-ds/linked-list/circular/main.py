class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 
    
class CircularLinkedList:
    def __init__(self):
        self.head = None 
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
            self.tail = temp.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, "->", end =" ")
            temp = temp.next
        print("None")
    
    def display_looped(self):
        temp = self.head
        self.tail.next = temp.next.next.next
        while temp:
            print(temp.data, end= " -> ")
            temp = temp.next
        print(None)

    def create_loop(self, el):
        temp = self.head
        starting_point = None
        while temp.next:
            if temp.data == el:
                starting_point = temp
            temp = temp.next
        temp.next = starting_point
    
    # def cycle_detect(self):
    #     slow, fast = self.head, self.head
    #     while fast.next and fast.next.next:
    #         slow = slow.next
    #         fast = fast.next.next
    #         if (slow.data == fast.data) and slow:
    #             print("Loop found")
    #             return 
    #     print("No loop found") 
    
    def remove_cycle(self):
        slow, fast = self.head, self.head
        second_cycle = False

        while fast.next and fast.next.next:
            slow = slow.next

            if second_cycle: fast = fast.next
            else: fast = fast.next.next

            if (slow.next.data == fast.next.data) and slow:
                if second_cycle:
                    slow.next = None
                    print("Loop removed")
                    return
                else:
                    second_cycle = True
                    fast = self.head
                    print("Loop Found!!")
        

l = "A B C D E F G H I J K".split()
myLL = CircularLinkedList()
for i in l:
    myLL.insert(i)
myLL.display()
# myLL.create_loop("D")
myLL.remove_cycle()
myLL.display()