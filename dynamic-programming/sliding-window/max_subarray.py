def max_subaray(array_size, arr, win_size):
    sm = {0:[]}
    for i in range(( array_size - win_size ) + 1):
        curr = arr[i:i+win_size]
        sm = max([sm, {sum(curr):curr}], key=lambda x: list(x.keys())[0])
    return sm
    
size = 6
array = [40, 25, 61, 80, 99, 4]
window_size = 3
print(max_subaray(size, array, window_size))
