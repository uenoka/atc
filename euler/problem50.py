# problem50.py
'''
The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.
The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
Which prime, below one-million, can be written as the sum of the most consecutive primes?
1000000 までの素数のリストをエラトステネスの篩で作成して2重ループで探索。
この時足し合わせたものは必ず奇数じゃないといけないから、2を含む/含まないで場合分けして必ず奇数になるように探索をする
'''

import math


def is_prime(n):
    # print('in', n)
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 2
    while i**2 <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def get_sieve_of_eratosthenes(n):
    prime = [2]
    limit = int(n**0.5)
    data = [i + 1 for i in range(2, n, 2)]
    while True:
        p = data[0]
        if limit <= p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]


prime = get_sieve_of_eratosthenes(1000000)

primeCumSum = [0]
cumsum = 0
for i in prime:
    cumsum += i
    primeCumSum.append(cumsum)
# print(primeCumSum)
print('cumsum end')
m = 0
N = 78497
for i in range(N):
    for j in range(i, N):
        sums = primeCumSum[j] - primeCumSum[i]
        # print(primeCumSum[j], primeCumSum[i])
        if is_prime(sums) and m < sums:
            m = sums
            print(i, j, m)
print(m)
