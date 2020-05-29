# agc002_a.py
A, B = map(int,input().split())
if A<=0 and B>=0:
    print('Zero')
elif A>0 and B>0:
    print("Positive")
elif A<0 and B<0:
    if (A-B)%2==0:
        print("Negative")
    else:
        print("Positive")
