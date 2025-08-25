class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, data):
        self.queue.append(data)
    def dequeue(self):
        if self.queue:
            print(self.queue.pop())
    def get_front(self):
        if self.queue:
            print(self.queue[0])
    def get_rear(self):
        if self.queue:
            print(self.queue[-1])
    def display(self):
        for i in self.queue:
            print(i, end=" ")
        print()
q = Queue()
l = [4, 3, 2, 5]
for i in l:
    q.enqueue(i)
q.display()