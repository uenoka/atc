# arc105_a_bfs.py


def dsf(a, idx):
    if idx == len(A):
        # print(a)
        if sums/2 == sum(a):
            print('Yes')
            exit()
        else:
            return

    a.append(A[idx])
    dsf(a, idx+1)
    a.pop()
    a.append(0)
    dsf(a, idx+1)
    a.pop()


A = list(map(int, input().split()))
sums = sum(A)
dsf([], 0)
print('No')
