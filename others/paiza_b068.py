# paiza_b068.py
H, W = map(int, input().split())
chocolate = [list(map(int, input().split())) for _ in range(H)]
ans = []
for row in chocolate:
    can_split = False
    for w in range(W):
        # print(row[:w], row[w:])
        if sum(row[:w]) == sum(row[w:]):
            can_split = True
            ans.append(["A"]*(w)+["B"]*(W-w))
            break

    if not can_split:
        print('No')
        exit()
print('Yes')
for i in ans:
    print("".join(i))
