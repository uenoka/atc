'''
input : 数字
return : a^p,b^q,...,c^r を {a:p,b:q,...,c:r} の dict で表したもの
'''
N = int(input())
import collections
L = list(map(int,input().split()))
C = collections.Counter(L)

print((N==3 * C[0]))