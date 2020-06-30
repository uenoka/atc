# abc032_c.py
N, K = map(int, input().split())
S = [int(input()) for i in range(N)]
if 0 in S:
    print(N)
    exit()

left = 0
mul = 1
ans = []
for right in range(N):
    mul *= S[right]
    while mul > K and left <= right:
        mul //= S[left]
        left += 1
    ans.append(right - left + 1)
    # print(left, right, mul, ans)
print(max(ans))
