n = int(input())    
a = list(map(int,input().split()))
q = int(input())
query = [list(map(int,input().split())) for i in range(q)]
for i in query:
    if i[0] == 1:
        a[i[1]-1] = i[2]
    if i[0] == 2:
        print(a[i[1]-1])