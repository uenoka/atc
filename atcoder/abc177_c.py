# abc177_c.py
def solve():
    N = int(input())
    A = list(map(int, input().split()))
    square = []
    for i in A:
        square.append(i**2)
    return (sum(A)**2 - sum(square))//2 % (10**9+7)


print(solve())
