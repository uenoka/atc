#abc042_b
N, M = map(int,input().split())
S = [input() for i in range(N)]
S.sort()
print("".join(S))