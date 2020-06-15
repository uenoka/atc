# abc170_a.py
a = list(map(int,input().split()))
for i,v in enumerate(a):
    if v == 0:
        print(i+1)
