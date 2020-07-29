# aising2020_b.py
N = int(input())
A = list(map(int,input().split()))
cnt = 0
for i,v in enumerate(A):
    if (i+1)%2==1 and v%2==1:
        cnt += 1

print(cnt)
