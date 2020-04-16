# codefestival_2016_qualB_b.py
N,A,B = map(int,input().split())
S = input()
cnt = 0
bcnt = 0
for i,c in enumerate(S):
    if c =="a":
        if cnt < A+B:
            print("Yes")
            cnt +=1
        else:
            print("No")
    elif c=="b":
        if cnt < A+B and bcnt<B:
            print("Yes")
            cnt +=1
            bcnt +=1
        else:
            print("No")
    elif c=="c":
        print("No")