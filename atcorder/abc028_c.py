# abc028_c.py
a = list(map(int,input().split()))
anslist= []
for i in a:
    for j in a:
        for k in a:
            if i!=j and i!=k and j!=k:
                anslist.append(i+j+k)
anslist = list(set(anslist))
anslist.sort(reverse=True)
print(anslist[2])