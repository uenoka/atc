# abc051_b.py
'''
O(N^3) では通らないから、いかにして O(N^2) にしますか?という問題。
ABS の類題 (https://atcoder.jp/contests/abc087/tasks/abc087_b) のようにそれぞれの数の関係性を見つけてループを減らす。
'''
K, S = map(int, input().split())
ans = 0
for i in range(K+1):
    for j in range(K+1):
        k = S-i-j
        if k <= K and i <= K and j <= K and k >= 0:
            ans += 1

print(ans)
