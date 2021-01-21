# paiza_s015.py
'''
確実にTLEするとわかっててもこれ以上わからん…
どうすんだろこれ。
s, t の差が100位内になっているのがキモだと思うけど、結局全部構築しないとどういう文字なのかわからん気がする…
https://drken1215.hatenablog.com/entry/2019/05/13/114600
ここら辺をもうちょっとちゃんと読む
'''
import sys
sys.setrecursionlimit(500000)


def dfs(n):
    if n == 1:
        return "ABC"
    pre = dfs(n-1)
    return "A" + pre + "B" + pre + "C"


k, s, t = map(int, input().split())
ans = dfs(k)
print(ans[s-1:t])
