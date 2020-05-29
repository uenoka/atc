# ALDS1_3_A.py
from collections import deque as stack
S = input().split()
q = stack([])
# print(S)
for i in S:
    # print("i:", i)
    if i == "+":
        b = int(q.pop())
        a = int(q.pop())
        q.append(a+b)
        # print("+:", a, b)
    elif i == "-":
        b = int(q.pop())
        a = int(q.pop())
        q.append(a-b)
        # print("-:", a, b)
    elif i == "*":
        b = int(q.pop())
        a = int(q.pop())
        # print("*:", a, b)
        q.append(a*b)
    else:
        q.append(int(i))
print(q.pop())
