class Stack:
    def __init__(self, max_size=0):
        self.top = 0
        self.stack = []
        self.max_size = max_size
    def push(self, item):
        if len(self.stack)==self.max_size:
            print("Stack Overflow")
        else:
            self.stack.append(item)
    def pop(self):
        if not self.stack:
            print("Stack Underflow")
        else:
            print("Popped element:", self.stack.pop())
    def peak(self):
        if not self.stack:
            print("Stack is emty")
        else:
            print("Peak element:", self.stack[-1])
    def display(self):
        print(self.stack)

myStack = Stack(5)
while True:
    print(f'''\nList of operations\n{'Push':<10} {'Pop':<10} {'Peak':<10} {'Display':<10} {'Exit':<10}''')
    inp = input("Select an option: ")
    if inp.lower() in ["exit"]:
        print("Varta maame")
        break
    elif inp.lower() == "push":
        item = int(input("Enter Element: "))
        myStack.push(item)
    elif inp.lower() in ["pop", "display", "peak"]:
        eval(f"myStack.{inp.lower()}()")
    else:
        print("Correct ah command kudunga thambi..!")