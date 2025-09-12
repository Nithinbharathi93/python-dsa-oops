arr = [5, 5, 3, 4, 1, 7, 4]
tar = 4

# Pegion sorting

min_value = min(arr)
max_value = max(arr)
N = max_value - min_value
hole = {i:[] for i in range(N+1)}
for i in arr:
    hole[i-min_value].append(i)
val_list = []
for i in hole.values():
    val_list.extend(i)
print(val_list)

# 2 pointer target sum search

left, right = 0, len(val_list)
while (right >= 0):
    curr = val_list[left] + val_list[right]
    if curr == tar:
        print(val_list[left], val_list[right])
        exit(0)
    if curr < tar:
        left += 1
    else:
        right -= 1
print("Not found")


'''

# Alternative approach

from collections import defaultdict

arr = [5, 5, 3, 4, 1, 7, 4]

temp_dict = defaultdict(bool)
for i in arr:
    temp_dict[i] = True

min_value = min(arr)
max_value = max(arr)
N = max_value - min_value
hole = {i:[] for i in range(N+1) if temp_dict[i+min_value]}
for i in arr:
    hole[i-min_value].append(i)
val_list = []
for i in hole.values():
    val_list.extend(i)
print(hole)
# print(val_list)


'''