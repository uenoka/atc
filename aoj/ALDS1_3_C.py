# ALDS1_3_C.py
'''
本来はlinkedList を自前実装する必要がありそうだが、Python だとDequeで実装できる。
'''
from collections import deque
N = int(input())
linkedList = deque([])
for i in range(N):
    command = input().split()
    if command[0] == "insert":
        linkedList.appendleft(command[1])
    elif command[0] == "delete":
        if command[1] in linkedList:
                linkedList.remove(command[1])
    elif command[0] == "deleteFirst":
        linkedList.popleft()
    elif command[0] == "deleteLast":
        linkedList.pop()
print(" ".join(list(linkedList)))