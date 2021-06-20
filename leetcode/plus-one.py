# plus-one.py
'''
想定解法かわかんないけど、Pythonだと一回Listを数字に直してから足してListに戻すのが楽
'''
from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = int(str("".join([str(i) for i in digits])))
        digits+=1
        return list(str(digits))
testcases = [
    [1,2,3],
    [4,3,2,1],
    [1],
    [0],
    [9]
]
for digits in testcases:
    sol = Solution().plusOne(digits)
    print(sol)