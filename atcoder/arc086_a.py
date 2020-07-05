# arc086_a.py
import collections
N, K = map(int, input().split())
A = list(map(int, input().split()))
C = collections.Counter(A)
C = sorted(C.values())

lenght = len(C)
# print(lenght, K, C)
print(sum(C[:(lenght-K)]))
