#arc017_1.py
def is_prime(n):
    if n == 2 or n%2 == 0:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True
N = int(input())
if is_prime(N):
    print("YES")
else:
    print("NO")
