# sort-array-by-parity.py
'''
左から順にアクセスして偶数ならeven 奇数なら odd という配列に入れて最後にくっつけることで
O(N) で実装。
'''
class Solution:
    def sortArrayByParity(self, A):
        even = []
        odd = []
        for i in A:
            if i%2==0:
                even.append(i)
            else:
                odd.append(i)
        return even + odd

    '''
    Pytbon だとこういう書き方ができる。（やってることは同じ）
    '''
    def sortArrayByParity2(self, A):
        return ([x for x in A if x % 2 == 0] +
                [x for x in A if x % 2 == 1])

    '''
    左右から順にみていって、
    左が奇数かつ右が偶数だったらスワップ、
    左が偶数だったら左のインデックスを進める、
    右が奇数だったら右のインデックスを進める（小さくしていく）
    とすることで O(N) でメモリは O(1) で解くことが可能
    '''
    def sortArrayByParity3(self, A):
        i, j = 0, len(A) - 1
        while i < j:
            if A[i] % 2 > A[j] % 2:
                A[i], A[j] = A[j], A[i]

            if A[i] % 2 == 0: i += 1
            if A[j] % 2 == 1: j -= 1

        return A

sol = Solution()
A  = [3,1,2,4]
print(sol.sortArrayByParity(A))