#abc106_b.py
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    #divisors.sort()
    return divisors

def has_eight_div(N):
#    print(len(make_divisors(N)) )
    if 8 == len(make_divisors(N)) and N%2==1:
        return 1
    return 0

N = int(input())
ans = 0
for i in range(N+1):
    ans += has_eight_div(i)
print(ans)
