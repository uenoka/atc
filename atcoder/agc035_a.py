# agc035_a.py
'''
両隣の数のXORが自身と等しい状態にできる場合Yes、そうでない場合No
例：
N = 3
Ai = 1, 2, 3
1, 2, 3 -> 1, 2, 3 にすることで
2 XOR 3  = 1, 2 XOR 1 = 3, 3 XOR 1 = 1 となるので Yes
XOR の性質は
a XOR a = 0
a XOR 0 = a
a XOR b >= a + b
などがある。
'''
import collections
N = int(input())

L = list(map(int,input().split()))
C = collections.Counter(L)
flg = False
if len(C)>3:
    print('No')
    exit()

if len(C)==3:
    ans = 0
    cnt = []
    for i,v in C.items():
        ans ^= i
        cnt.append(v)
    if ans == 0 and max(cnt) == min(cnt):
        print('Yes')
        exit()
    else:
        print('No')
if len(C) == 2:
    if C[0] == 0:
        print('No')
        exit()
    x = 0
    y = 0
    for i,v in C.items():
        if i == 0 :
            x = v
        else:
            y = v
    if 2 * x == y:
        print('Yes')
        exit()
    else:
        print('No')
        exit()
if len(C) == 1:
    if C[0]>0:
        print('Yes')
        exit()
    else:
        print('No')
