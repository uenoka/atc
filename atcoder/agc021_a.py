# agc021_a.py
'''
やりたいことは
各桁を1減らして、その下の桁をすべて999…にする
それらを比較して一番大きいものを答えにする（何も操作しないものも含む）
だが、Listとstrとかでやると大変…
どこかに落とし穴があるらしい…どこだろう
'''
import math

def digitSum(n):
    s = str(n)
    array = list(map(int, s))
    return sum(array)

def calc(n):
    ans = []
    for i in range(len(str(n))):
        target = n-10**i
        target = math.floor(target/(10**i))
        for _ in range(i):
            target*=10
            target+=9
        ans.append(digitSum(target))
#        print(target)
    return ans

N = int(input())
ans = max(calc(N))
print(ans)
