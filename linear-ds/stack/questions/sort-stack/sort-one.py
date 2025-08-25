class Stack:
    def __init__(self):
        self.stack = []
    def push(self, data):
        self.stack.append(data)
    def is_exist(self):
        return True if self.stack else False 
    def pop(self):
        if not self.is_exist(self):
            return None
        return self.stack.pop()
    def top(self):
        if not self.is_exist():
            return None
        return self.stack[-1]

def sort_stack_one(stack, inter): 
    if stack.is_exist():
        inter.push(stack.pop())
    while inter.is_exist():
        s_element = stack.pop()
        i_element = inter.pop()
        if i_element > s_element:
            inter.push(s_element)
            stack.push(i_element)
        else:
            pass

myStack = Stack()
inter = Stack()
l = [100, 6, 10, 11]
for i in l:
    myStack.push(i)
myStack.display()
ans = sort_stack_one(myStack, inter)
ans.display()
