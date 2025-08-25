inp = input().replace(" ", "")

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
        if i.isalnum():
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
print("Postix expression:", ans)
# print(stack) 
# inp = input().replace(" ", "")

# stack = []
# ans = ""
# pd = {
#     "^": 3,
#     "*": 2, "/":2,
#     "+": 1, "-":1,
#     "(": 0
# }
# for i in inp:
#     if i not in "+-*/()^":
#         if i.isalpha():
#             ans += i
#             print(i, ans, "Letter came")
#     else:
#         if not stack:
#             stack.append(i) 
#             print(i, stack, "pushed")
#         elif i==")":
#             while stack[-1]!="(":
#                 ans += stack.pop()
#             stack.pop()
#             print("( bracket closed", stack, ans)
#         else:
#             while (stack) and (pd[stack[-1]] >= pd[i]) and (i!="(") and ( not (stack[-1]==i=="^")):
#                 ans += stack.pop()
#                 print(i, ans, "popped")
#             else:
#                 stack.append(i)
#                 print(i, stack, "pushed")
# while stack:
#     ans += stack.pop()
# print("Postix expression:", ans)
# # print(stack)