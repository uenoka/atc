D = int (input())
N = int (input())
attend = [0] * (D + 1)
for i in range(N):
    L,R = map(int, input().split())
    attend[L-1] += 1
    attend[R] -= 1
yesterday = 0
for i in range(D):
    attend[i] += yesterday
    yesterday = attend[i]
    print(attend[i])
