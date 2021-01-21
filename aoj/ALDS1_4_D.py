# ALDS1_4_D.py

def can_load(w, p, k):
    # print("stert:",p,k)
    limit = p
    for idx, i in enumerate(w):
        # print("k is",k,"i is",i,"limit is",limit)
        if limit-i < 0:
            # print("limit -1 < 0 ")
            k -= 1
            limit = p - i
        else:
            # print("limit -1 >= 0 ")
            limit -= i
        if k <= 0 and idx != len(w):
            # print("cant load:",p,k)
            return False
    # print("can load!!:",p,k)
    return True


def solve(n, k, w):
    left = 0
    # right = 100000*10000
    right = 100
    while right-left > 1:
        # print(right,left)
        mid = (right+left)//2
        if can_load(w, mid, k):
            right = mid
        else:
            left = mid
    return right


N, K = map(int, input().split())
W = [int(input()) for _ in range(N)]
# print(W)
ans = solve(N, K, W)
print(ans)
