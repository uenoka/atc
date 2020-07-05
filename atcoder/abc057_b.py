# abc057_b.py
def calc(p1, p2):
    return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])


N, M = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(N)]
cd = [list(map(int, input().split())) for i in range(M)]
for i in range(N):
    dist = 10**9
    ans = 0
    for j in range(M):
        now_dist = calc(ab[i], cd[j])
        if dist > now_dist:
            dist = now_dist
            ans = j+1
    print(ans)
