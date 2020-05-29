# abc133_b.py
N, M = map(int,input().split())
X = list(map(int,input().split()))
X.sort()
Xsub = [X[i+1]-X[i] for i in range(M-1)]
Xsub.sort(reverse=True)
print(sum(Xsub[N-1:]))
