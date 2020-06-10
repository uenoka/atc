'''
input : 数字
return : a^p,b^q,...,c^r を {a:p,b:q,...,c:r} の dict で表したもの
'''

top = 10**12
ans = 1
cnt = 0
while ans < top:
    ans *= 2
    cnt += 1
print(cnt, ans)
print(2**40)
