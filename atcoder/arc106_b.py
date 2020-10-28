# arc106_b.py
'''
連結成分内で和が同じであればOKって感じかな。
'''
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
glaph = [[] for i in range(N+1)]
for i in range(M):
    c, d = map(int, input().split())
    glaph[c].append(d)
    glaph[d].append(c)
# print(glaph)
ans = True
seen = [False]*(N+1)
for i in range(1, N+1):
    stack = []
    connected_node = []
    if not seen[i]:
        seen[i] = True
        stack.append(i)
        connected_node.append(i)
    while stack:
        idx = stack.pop()
        for node in glaph[idx]:
            if not seen[node]:
                connected_node.append(node)
                stack.append(node)
                seen[node] = True
    A_sum = 0
    B_sum = 0
    # print(connected_node)
    for idx in connected_node:
        A_sum += A[idx-1]
        B_sum += B[idx-1]
    if not A_sum == B_sum:
        ans = False
        break
if ans:
    print('Yes')
else:
    print('No')
