# partitioning-into-minimum-number-of-deci-binary-numbers.py
'''
想定解法かどうかわからないけど普通に最大の数値入れればいいよねという感じ…？
これがMediumなのがわからない…Easyの軽いクイズ枠じゃないのか…？
'''
class Solution:
    def minPartitions(self, n: str) -> int:
        n = list(n)
        return max(n)

testcases = [
    "123454326",
    "32",
    "82734"
]
for n in testcases:
    sol =Solution().minPartitions(n)
    print(sol)
