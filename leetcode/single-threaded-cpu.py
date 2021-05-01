# single-threaded-cpu.py
'''
ゴリゴリのアルゴリズムというよりは、データ構造（heap_queue）の理解と、丁寧に実装できるかという感じの問題だった。

'''
from typing import List
import heapq as hq
class Solution:
    def getOrder(self, tasks):
        ans = []
        pq = []
        t = 0
        tasks.append([float('inf'), float('inf')])
        for (enq,prc),i in sorted(zip(tasks,range(len(tasks)))):
            while pq and t < enq:
                prc_time, idx, enq_time = hq.heappop(pq)
                ans.append(idx)
                t = max(t, enq_time) + prc_time
            hq.heappush(pq, (prc, i, enq))
        return ans

testcases = [
    [[1, 2], [2, 4], [3, 2], [4, 1]],
    # [[7, 10], [7, 12], [7, 5], [7, 4], [7, 2]]
]
for tasks in testcases:
    sol = Solution().getOrder(tasks)
    print(sol)
