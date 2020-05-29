# abc090_b.py
A, B = map(int,input().split())
cnt=0
for i in range(A,B+1):
    i_str = str(i)
    if i_str == i_str[::-1]:
        cnt+=1
print(cnt)