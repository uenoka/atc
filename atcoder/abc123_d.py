# abc123_d.py
'''
愚直解法だと全要素を突き合わせてその後にソートをするため O(ABClogABC) となり、A=B=C=1000 の時 10^10 程度の計算回数になるため間に合わない。
そこで、計算量改善をする。
今回は priorityQueue の練習ということで priorityQueue での解法。
まずABCをそれぞれソートする
priorityQueue に A[0]+B[0]+C[0],(0,0,0) を追加する(足した情報とインデックスの情報)
また、別途インデックスの情報を管理する
k回以下の操作を行う
priorityQueue に入っている最大の値とそのインデックスを取得（heappop）
取得した最大の値をprint
取得したA,B,Cのインデックスをそれぞれインクリメントしたものが priorityQueue に入ってないことを確認（use を利用）
入っていなければ取り込む（heappush）
ただし、Pythonのheapqは最小しか取れない?っぽいので最大の値をマイナスしてあげておいて、printの時に再度マイナスにする
'''
import heapq

x, y, z, k = map(int, input().split())
A = sorted(list(map(int, input().split())), reverse=True)
B = sorted(list(map(int, input().split())), reverse=True)
C = sorted(list(map(int, input().split())), reverse=True)
use = set((0, 0, 0))
q = []
heapq.heappush(q, (-A[0]-B[0]-C[0], 0, 0, 0))
for _ in range(k):
    taste, ai, bi, ci = heapq.heappop(q)
    if ai+1 < x and not (ai+1, bi, ci) in use:
        heapq.heappush(q, (-A[ai+1]-B[bi]-C[ci], ai+1, bi, ci))
        use.add((ai+1, bi, ci))
    if bi+1 < y and not (ai, bi+1, ci) in use:
        heapq.heappush(q, (-A[ai]-B[bi+1]-C[ci], ai, bi+1, ci))
        use.add((ai, bi+1, ci))
    if ci+1 < x and not (ai, bi, ci+1) in use:
        heapq.heappush(q, (-A[ai]-B[bi]-C[ci+1], ai, bi, ci+1))
        use.add((ai, bi, ci+1))
    print(-taste)
