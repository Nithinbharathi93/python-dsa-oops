# [(value, priority)]
def enque(queue, value, prio):
    queue.append((value, prio))
def dequeue(queue):
    high = max(queue, key=lambda x:x[1])
    queue.remove(high)
    print(queue)
queue = []
count = int(input())
for i in range(count):
    inp = map(int, input().split())
    enque(queue, *inp)
print(queue)
dequeue(queue)