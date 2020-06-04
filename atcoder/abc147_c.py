# abc147_c.py
'''
嘘つきと正直者の問題
各人Aiが嘘つきか正直者かを0,1で管理して、2^15 の探索を行う基本的なBit全探索。
証言のYijも嘘つき=0, 正直者=1 で表せるから、評価を論理和とか論理積とかでやってもいいかも。
'''
import itertools


def match(pattern):
    return True


N = int(input())
XY = []
for _ in range(N):
    A = int(input())
    for i in range(A):
        XY.append(list(map(int, input().split())))

status = [(0, 1) for _ in range(N)]
state = list(itertools.product(*status))
ans = 0
for i in state:
    if match(i):
        ans += 1
print(ans)
print(XY, state)
