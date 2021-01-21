# PAST_1_E.py
'''
解けない。。。こういう添え字ゴリゴリ系はやっぱ苦手…
もうちょいわかりやすく書いたら出来るようになるだろうか…
'''


def printans():
    for i in range(1, N+1):
        for j in range(1, N+1):
            print("Y" if ff[i][j] else "N", end="")
        print()


N, Q = map(int, input().split())
ff = [[False for i in range(N+1)] for i in range(N+1)]

for i in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        ff[q[1]][q[2]] = True
    elif q[0] == 2:
        for i in range(1, N+1):
            if ff[i][q[1]]:
                ff[q[1]][i] = ff[i][q[1]]
    else:
        # q[1] がフォローしているユーザーがフォローしているユーザーをすべてフォローする
        target_user = q[1]
        follows = ff[target_user].copy()
        for i in range(1, N+1):
            if follows[i]:
                for j, is_follow in enumerate(ff[i]):
                    if is_follow:
                        ff[target_user][j] = True
printans()
