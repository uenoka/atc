N, Q = map(int,input().split())
ff = {}
for _ in range(Q):
    t,a,b = map(int,input().split())
    if t == 1:
        if a in ff:
            ff[a].add(b)
        else:
            ff[a] = set([b])
    elif t == 2:
        if a in ff:
            ff[a].discard(b)
    elif t == 3:
        if a in ff and b in ff:
            if b in ff[a] and a in ff[b]:
                print('Yes')
            else:
                print('No')
        else:
            print('No')

  