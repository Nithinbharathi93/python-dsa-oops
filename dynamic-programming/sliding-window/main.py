# def sub_array_sum(arr, target_sum, window_size):

#     iter_size = len(arr) - window_size
#     d = {}

#     for i in range(iter_size+1):

#         curr = arr[i:i+window_size]

#         d[sum(curr)] = curr
    
#     return d[target_sum] if target_sum in d else "Not available"

def slide_sum(arr, slide):
    ans = 0
    for i in range(slide):
        ans += arr[i]
    return ans

def sub_array(ln, arr, tar, wsz):
    sm = slide_sum(arr, wsz)
    for i in range(ln):
        if sm == tar:
            return arr[i:i+wsz]
        sm += (arr[i+wsz] - arr[i])
    return "Not available"

# size = int(input())
# arr = list(map(int, input().split()))
# target_sum  = int(input())
# window_size = int(input())

size = 5
arr = [10, 2, 6, 7, 4, 3, 1]
target_sum = 8
window_size = 2

print(sub_array(size, arr, target_sum, window_size))
