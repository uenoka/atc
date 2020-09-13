# relative-sort-array.py
'''
arr1 : 重複ありの配列
arr2 : 重複なしの配列
arr2 にある要素は arr1 に存在する。
タスク : arr1 の要素を arr2 の要素の並び順にソートする。
愚直に考えると、arr2 の要素で for を回して、その中で arr1 にその要素がある限りswapし続けるという感じ
この解法だと O(N^2) になる。
'''


class Solution:
    def relativeSortArray(self, arr1, arr2):
        ans = []
        import collections
        C = collections.Counter(arr1)
        print()
        for i in arr2:
            ans += [i]*C.pop(i)
        ans += sorted(C.elements())
        return ans


sol = Solution()
# arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
# arr2 = [2, 1, 4, 3, 9, 6]
arr1 = [33, 22, 48, 4, 39, 36, 41, 47, 15, 45]
arr2 = [22, 33, 48, 4]
# arr1 = [28, 6, 22, 8, 44, 17]
# arr2 = [22, 28, 8, 6]
print(sol.relativeSortArray(arr1, arr2))
