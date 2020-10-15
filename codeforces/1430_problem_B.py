# 1430_problem_B.py
t = int(input())
for i in range(t):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    print(sum(A[-K-1:]))
