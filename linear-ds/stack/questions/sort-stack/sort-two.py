# 100, 6, 10, 11
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if not self.stack:
            return False
        else:
            popped_element = self.stack.pop()
            return popped_element
    def display(self):
        print(*self.stack)
    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            return False
    def exists(self):
        if self.stack: return True
        return False

def sort_stack(stack):
    fin = Stack()
    temp = Stack()
    while stack.exists():
        if not temp.exists():
            temp.push(stack.pop())
        else:
            s_element = stack.top()
            f_element = temp.top()
            if s_element < f_element:
                temp.push(stack.pop())
            else:
                while (stack.top() > temp.top()):
                    if not temp.exists():
                        break
                    fin.push(temp.pop())
                temp.push(stack.pop())
                while fin.exists():
                    temp.push(fin.pop())
    while temp.exists():
        fin.push(temp.pop())
    return fin


myStack = Stack()
l = [100, 6, 10, 11]
for i in l:
    myStack.push(i)
myStack.display()
ans = sort_stack(myStack)
ans.display()


