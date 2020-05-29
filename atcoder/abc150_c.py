# abc150_c.py
'''
全パターン作ってソートで順番みる
tuple の比較とか、itertools の使い方とか、ちゃんといろいろ勉強したほうがよさそう。
'''
import itertools
N = int(input())
P = tuple(list(map(int,input().split())))
Q = tuple(list(map(int,input().split())))

l = [i+1 for i in range(N)]
target =  itertools.permutations(l)
cnt=0
pcnt = 0
qcnt = 0
for i in target:
    cnt += 1
    if i == P:
        pcnt=cnt
    if i == Q:
        qcnt=cnt

print(abs(pcnt-qcnt))
