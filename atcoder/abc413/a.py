N, M = map(int,input().split())
A = list(map(int,input().split()))
if sum(A)<=M:
    print('Yes')
else:
    print('No')