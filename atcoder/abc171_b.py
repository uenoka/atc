# abc171_b.py
N, K = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
print(sum(A[:K]))