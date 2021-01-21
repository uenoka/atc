# n-repeated-element-in-size-2n-array.py
'''
下から取っていって2回目に当たったらその値を返す→O(N)
set で要素を減らす→全部足すからO(N)かかる…?
'''


class Solution:
    def repeatedNTimes(self, A) -> int:
        unique = set(A)
        return (sum(A)-sum(unique))//(len(A)//2-1)


sol = Solution()
A = [2, 1, 2, 5, 3, 2]
print(sol.repeatedNTimes(A))
