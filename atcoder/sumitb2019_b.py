# sumitb2019_b.py
import math 
N = int(input())
for i in range(50000):
    if math.floor(i*1.08) == N:
        print(i)
        exit()
print(":(")