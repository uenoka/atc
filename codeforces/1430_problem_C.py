# 1430_problem_C.py
import math
T = int(input())
for i in range(T):
    N = int(input())
    lis = [i for i in range(1, N+1)]
    if N % 2 == 1:
        print(N//2+1)
    else:
        print(N//2)
        for i in range(N-1):
            a = lis.pop()
            b = lis.pop()
            print(a, b)
            lis.append(math.ceil((a+b)/2))
