# ALDS1_1_C.py
def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


cnt = 0
N = int(input())
for i in range(N):
    p = int(input())
    if is_prime(p):
        cnt += 1
print(cnt)
