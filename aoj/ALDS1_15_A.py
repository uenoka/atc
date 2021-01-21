# ALDS1_15_A.py

def solve(n):
    cnt = n//25
    n %= 25
    cnt += n//10
    n %= 10
    cnt += n//5
    n %= 5
    cnt += n
    return cnt


N = int(input())
print(solve(N))
