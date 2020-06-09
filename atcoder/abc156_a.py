# abc156_a.py
N, R = map(int,input().split())
if N>=10:
    print(R)
else:
    print(R + 100*(10-N))
