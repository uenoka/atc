# Recursive_function.py
'''
再帰関数が苦手なので下の記事をもとに練習
https://drken1215.hatenablog.com/entry/2020/05/04/190252
0000
~
1111
を出力するだけの関数
'''
import time
def dfs(A):
    if len(A)==N:
        print(A)
        return
    for i in range(M):
        A.append(i)
        dfs(A)
        A.pop()
N, M = map(int,input().split())
dfs([])