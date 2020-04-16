# babc094_b.py
N, M, X = map(int,input().split())
A = list(map(int,input().split()))
cnt_pre=0
cnt_post=0
for i in A:
    if i<X:
        cnt_pre+=1
    else:
        cnt_post+=1
print(min(cnt_post,cnt_pre))