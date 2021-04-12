# count-items-matching-a-rule.py
'''
多次元配列触れますかという問題
'''
class Solution:
    def countMatches(self, items, ruleKey: str, ruleValue: str) -> int:
        idxTable = {'type':0,
                'color':1,
                'name':2
                }
        cnt = 0
        idx = idxTable[ruleKey]
        for item in items:
            if item[idx] == ruleValue:
                cnt+=1
        return cnt


testcases = [
    [
        [["phone", "blue", "pixel"], ["computer", "silver","lenovo"], ["phone", "gold", "iphone"]]
        ,"color"
        ,"silver"
    ],
    [
        [["phone", "blue", "pixel"], ["computer", "silver","lenovo"], ["phone", "gold", "iphone"]]
        ,"type"
        ,"phone"
    ]
]

for items, ruleKey, ruleValue in testcases:
    sol = Solution().countMatches(items, ruleKey, ruleValue)
    print(sol)
