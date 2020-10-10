# aclbc_d.py
N, K = map(int,input().split())
A = [int(input()) for i in range(N)]
B =[A[0]]

for i in range(1,N):
    if abs(A[i]-B[-1])<=K:
        B.append(A[i])
# print(B)
print(len(B))
