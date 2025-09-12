def hashFunction(num, ln):
    return num%ln

def search_hash(num, hash_table, ln):
    pos  = num%ln
    for i in range(len(hash_table[pos])):
        if hash_table[pos][i] == num:
            return True
    return False


arr = [45, 3, 5, 9, 32, 54 ,90, 34]
length = 7

hash_table = {i:[] for i in range(length)}

i = 0

while i==len(arr):
    hash_table[hashFunction(arr[i], length)].append(i)

tar = 32
print(search_hash(tar, hash_table, length))