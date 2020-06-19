# tokiomarine2020_c.py
'''
imos 法を使って解くらしい
類題
https://atcoder.jp/contests/abc014/tasks/abc014_3
'''
import math
def calc(a):
    ret = []
    cumsum=0
    isOver = True
    for i in a:
        # print("i,N",i,N)
        cumsum += i
        ret.append(min(N,cumsum))
        if cumsum <= N:
            isOver = False
    return  ret[:5],isOver
N, K = map(int,input().split())
A = list(map(int,input().split()))
