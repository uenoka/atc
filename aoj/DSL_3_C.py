# DSL_3_C.py
def count_two_idx(A, q):
    ans = 0
    left = 0
    csum = 0
    for right in range(N):
        csum += A[right]
        while csum > q:
            csum -= A[left]
            left += 1
        ans += right - left + 1
    return ans


N, M = [int(x) for x in input().split()]
A = list(map(int, input().split()))
X = list(map(int, input().split()))

for q in X:
    print(count_two_idx(A, q))
