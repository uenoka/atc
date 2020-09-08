# eratosthenes.py
import time


def eratosthenes(n):
    prime_list = []
    nums = set()
    for i in range(2, n+1):
        if i not in nums:
            prime_list.append(i)
            for j in range(i*i, n+1, i):
                nums.add(j)
    return prime_list


def prime_eratosthenes(n):
    prime_list = []
    num_list = []
    for i in range(2, n+1):
        if i not in num_list:
            prime_list.append(i)
            for j in range(i*i, n+1, i):
                num_list.append(j)
    return prime_list


def exec(num):
    start = time.time()
    eratosthenes(num)
    # print(eratosthenes(num))
    end = time.time()
    print(end-start)

    start = time.time()
    prime_eratosthenes(num)
    # print(prime_eratosthenes(num))
    end = time.time()
    print(end-start)


num = 100000
exec(num)
