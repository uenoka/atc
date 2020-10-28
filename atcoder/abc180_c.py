# abc180_c.py
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    #divisors.sort()
    return divisors

N = int(input())
ans=make_divisors(N)
ans.sort()
for i in ans:
    print(i)