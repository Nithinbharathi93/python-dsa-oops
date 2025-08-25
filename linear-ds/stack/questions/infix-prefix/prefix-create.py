inp = input().replace(" ", "")
print(inp)
inp = inp[::-1]
print(inp)
temp = ""
for i in inp:
    if i=="(":
        i=")"
    elif i==")":
        i="("
    temp += i
print(inp:=temp)
stack = []
ans = ""
pd = {
    "^": 3,
    "*": 2, "/":2,
    "+": 1, "-":1,
    "(": 0
}
for i in inp:
    if i not in "+-*/()^":
        ans += i
    else:
        if not stack:
            stack.append(i) 
        elif i==")":
            while stack[-1]!="(":
                ans += stack.pop()
            stack.pop()
        else:
            while (stack) and (pd[stack[-1]] >= pd[i]) and (i!="(") and ( not (stack[-1]==i=="^")):
                ans += stack.pop()
            else:
                stack.append(i)
while stack:
    ans += stack.pop()
print(ans)
ans = ans[::-1]
print("Prefix expression:", ans)