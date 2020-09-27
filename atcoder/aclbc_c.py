class path_compressed_quick_union:
    def __init__(self, n):
        self.n = n
        self.data = [i for i in range(n)]
        self.size = [1 for i in range(n)]

    def root(self, p):
        while p != self.data[p]:
            self.data[p] = self.data[self.data[p]]
            p = self.data[p]
        return p

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        proot = self.root(p)
        qroot = self.root(q)
        if self.size[proot] < self.size[qroot]:
            self.data[qroot] = proot
            self.size[qroot] += self.size[proot]
        else:
            self.data[proot] = qroot
            self.size[proot] += self.size[qroot]



N, M = map(int,input().split())
uf = path_compressed_quick_union(N)
for i in range(M):
    a,b=map(int,input().split())
    uf.union(a-1,b-1)
ans = []
for i in range(N):
    ans.append(uf.root(i))
print(len(set(ans))-1)