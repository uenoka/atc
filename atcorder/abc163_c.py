# abc163_c.py
N = int(input())
ans = [0]*N
M = list(map(int,input().split()))
for i in M:
    ans[i-1] += 1
for i in ans:
    print(i)