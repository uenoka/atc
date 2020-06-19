# abc117_b.py
def sums(a, l):
    return sum(a)-2*l


N = int(input())
A = list(map(int, input().split()))
m = max(A)
if m < sum(A)-m:
    print('Yes')
else:
    print('No')
