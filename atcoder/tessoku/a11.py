import bisect
N,X = map(int, input().split())
A = list(map(int, input().split()))
print(bisect.bisect_right(A, X))