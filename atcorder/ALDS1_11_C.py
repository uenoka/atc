# ALDS1_11_C.py
import queue


def printNode():
    for i, node in enumerate(glaph):
        print(i, node)


N = int(input())
glaph = [[] for i in range(N+1)]
for i in range(1, N+1):
    glaph[i] = list(map(int, input().split()))[2:]
# printNode()

step = [-1]*(N+1)
step[1] = 0

q = queue.Queue()
q.put(1)
while not q.empty():
    now = q.get()
    next_node = glaph[now]
#    print("now is ", now, ", next is", next_node)
    for i in next_node:
        if step[i] != -1:
            continue
        q.put(i)
        step[i] = step[now] + 1

for i, v in enumerate(step):
    if i != 0:
        print(i, v)
