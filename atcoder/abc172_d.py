# abc172_d.py
'''
input : 数字
return : a^p,b^q,...,c^r を {a:p,b:q,...,c:r} の dict で表したもの
'''

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return len(divisors)

N = int(input())
ans = 0
for i in range(1,N+1):
    ans += i*make_divisors(i)
print(ans)