# unique-number-of-occurrences.py
'''
さて他に改善点はあるかしら…?
'''


class Solution:
    def uniqueOccurrences(self, arr) -> bool:
        import collections
        C = collections.Counter(arr)
        cnt = C.values()
        unique_cnt = set(cnt)
        return len(cnt) == len(unique_cnt)


sol = Solution()
arr = [1, 2, 2, 4, 4, 4]
print(sol.uniqueOccurrences(arr))
