# sort-array-by-parity-ii.py
'''
この解法面白い。
偶数番目と奇数番目を別々にみていって、それぞれ合わないものを見つけたら交換をすることでO(N)で解くことができる。
'''


class Solution:
    def sortArrayByParityII(self, A):
        j = 1
        for i in range(0, len(A), 2):
            if A[i] % 2 == 1:
                while A[j] % 2 == 1:
                    j += 2
                A[i], A[j] = A[j], A[i]
        return A


sol = Solution()
s = [1, 3, 2, 5, 6, 4]
print(sol.sortArrayByParityII(s))
