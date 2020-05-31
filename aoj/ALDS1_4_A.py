# ALDS1_4_A.py
_ = int(input())
S = list(map(int,input().split()))
_ = int(input())
T = list(map(int,input().split()))
cnt = 0
for i in T:
    if i in S:
        cnt+=1
print(cnt)