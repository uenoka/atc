'''
ソートしてD枚ずつ見て、合計が D*P 以上なら周遊チケットを使う、それ以降はもう終わりという感じで見る
'''
N,D,P = map(int,input().split())
F = list(map(int,input().split()))
F.sort(reverse=True)
ans = 0
for n in range(0,N,D):
    if sum(F[n:n+D]) > P:
        ans += P
    else:
        ans += sum(F[n:])
        break
print(ans)