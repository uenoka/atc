# ALDS1_3_D.py
'''
なぜか\と/のindexを引くとうまく面積になる。理屈がわからん…
らせん本に回答があるから、あとで再度解いてみる。2つStack使う理屈がわからん…
'''
from collections import deque
S = input()
top = 0
stack = deque()

ans = 0
total = []
for i,c in enumerate(S):
    print("len:",len(stack))
    if c =='\\':
        stack.append((i,c))
    if c=='/' :
        if len(stack) != 0:
            pre ,_ = stack.pop()
            ans += (i-pre)
        if len(stack) == 0:
            print("flush")
            total.append(ans)
            ans = 0
print(ans)
print(total)
