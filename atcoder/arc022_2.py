# arc022_2.py
'''
尺取り法とデータ構造の合わせ技。
結構難しいからもう一回時間たったら解きなおしたい良問。
'''
s = set()
N = int(input())
A = list(map(int,input().split()))
right = 0
ans = 0
for left in range(N):
    while  right < N and A[right] not in s:
        s.add(A[right])
        right += 1
    ans = max(ans,right - left)
    if right == left:
        right += 1
    else:
        s.discard(A[left])
print(ans)
