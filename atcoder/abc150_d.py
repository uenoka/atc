# abc150_d.py
import math
N, M = map(int,input().split())
A = set(list(map(int,input().split())))

mul = 1
for i in A:
    mul*=i
    mul/=2
    if mul>M:
        print(0)
        exit()
print(math.ceil(M/(mul*2)))
