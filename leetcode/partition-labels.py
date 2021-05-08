# partition-labels.py
'''
正直問題文が分からなかった…解説読みながら何言ってるのかをまず理解するのが先…
'''
from typing import List
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = {c: i for i, c in enumerate(S)}
        print(last)
        j = anchor = 0
        ans = []
        for i, c in enumerate(S):
            j = max(j, last[c])
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1
        return ans

testcases = [
    "ababcbacadefegdehijhklij",
    'abcdefghijklmnopqrstuvwxyz'
]
for S in testcases:
    sol = Solution().partitionLabels(S)
    print(sol)