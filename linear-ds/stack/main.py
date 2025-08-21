
stack = [] #-> Creating an empty array
max_size = 5

# Defining push function
def push(item):
    if len(stack)==max_size:
        print("Stack Overflow")
    else:
        stack.append(item)

# Defining pop function
def pop():
    if not stack:
        print("Stack Underflow")
    else:
        print(stack.pop())

def peak():
    if not stack:
        print("Stack empty")
    else:
        print(stack[-1])

push(100)
push(200)
push(300)
push(400)
push(400)
push(400)
print(stack)
pop()
pop()
pop()
pop()
pop()
pop()
peak()