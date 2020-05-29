# ALDS1_4_C.py
N = int(input())
dict = {}
for i in range(N):
    query, s = input().split()
    if query == "insert":
        dict[s] = True
    else:
        print('yes' if s in dict else 'no')
