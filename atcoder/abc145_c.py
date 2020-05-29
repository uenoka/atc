# abc145_c.py
'''
解いたことあるのに解けなくなっていた…
と思ったら政界にはなるけど正しい開放じゃない感じだった。
本来は順列で全パターンの距離とる必要があるが、前の回答は
for i in range(N):
  for j in range(N):
    if i != j:
      ans += ((xy[i][0]-xy[j][0])**2 + ((xy[i][1]-xy[j][1])**2))**0.5
print(ans/N)
ってやってる
'''
import math
def calc(u,v):
    return math.sqrt((u[0]-v[0])**2 + (u[1]-v[1])**2)
import itertools
N = int(input())
XY = [list(map(int,input().split())) for i in range(N)]

l = [i+1 for i in range(N)]
dist = 0
for v in itertools.permutations(XY,N):
    for i in range(1,N):
        dist += calc(v[i],v[i-1])

print(dist/math.factorial(N))
