# abc081_b.py
n = int(input())
a = list(map(int,input().split()))
cnt = 0
end = False
while not end:
    for i in range(n):
        if a[i]%2 == 0:
            a[i] = a[i]//2
        else:
            end = True
            break
    if not end :
        cnt+=1
print(cnt)