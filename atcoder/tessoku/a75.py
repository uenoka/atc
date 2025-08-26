
'''
# 問題

次郎君は $N$ 問からなる期末試験を受けることになりました。各設問には $1$ から $N$ までの番号が付けられており、設問 $i$ は連続する $T\_i$ 分間を使って考えると正解にたどり着けます。

しかし、各設問には **締切** が定められており、設問 $i$ は試験開始時刻から $D\_i$ 分後を過ぎると回答できなくなります。次郎君が最適な行動をしたとき、最大で何問正解することができるかを求めてください。

# 考察

なんか締切が一番近いソートの問題っぽそうな見た目をしているw
愚直に締め切りが一番近いものを取って、時間を消費、次にできる問題を探す、という流れがいいのかなぁ?
だめだったーーー
DPらしいが解説がわからん。
DPテーブルで横を時間、縦をそれぞれの問題(締め切り時間でソートさせておく)として見ていく。
イメージは、問題1〜k までを使用して時間tで何問解けるかというところに落とし込んでいくイメージ
'''
N = int(input())
problems = []
for i in range(N):
    time, deadline = map(int, input().split())
    problems.append({'time': time, 'deadline': deadline})

# 締切順にソート
problems.sort(key=lambda p: p['deadline'])

# 最大時間
max_time = max(p['deadline'] for p in problems)

# dp[i][t] = 問題0〜i-1を考慮して時刻tまでに解ける最大問題数
dp = [[0] * (max_time + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    problem = problems[i - 1]
    required_time = problem['time']
    deadline = problem['deadline']
    
    for current_time in range(max_time + 1):
        # この問題を解かない場合
        dp[i][current_time] = dp[i - 1][current_time]
        
        # この問題を解く場合
        if current_time >= required_time and current_time <= deadline:
            dp[i][current_time] = max(
                dp[i][current_time],
                dp[i - 1][current_time - required_time] + 1
            )

print(max(dp[N]))