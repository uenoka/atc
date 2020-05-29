# ALDS1_4_B.pys
def binary_search(key,target):
    left = -1
    right = len(target)
    while (abs(right - left) > 1):
        mid = left + (right - left) // 2
        if mid == key:
            return mid
        elif key < mid:
            right = mid
        else:
            left = mid
    return -1

N = int(input())
S = list(map(int,input().split()))
q = int(input())
T = list(map(int,input().split()))
ans = 0
for i in T:
    if binary_search(i,S) > 0:
        ans += 1
print(ans)
