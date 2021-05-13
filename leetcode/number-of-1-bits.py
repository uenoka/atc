# number-of-1-bits.py
'''
bit 演算分かんねー
andを取ればよいことまではわかったが、<<=とかよくわからんかった
a <<= 1 で bit の左シフト、a >>= 1 で右シフト（指定する数はシフトするBit数）
'''

class Solution:
    def hammingWeight(self, n: int) -> int:
        mask = 1
        cnt = 0
        for i in range(32):
            if mask & n != 0:
                cnt+=1
            mask<<=1
        return cnt
testcases = [
    0b11111111111111111111111111111101,
    0b00000000000000000000000010000000
]
for n in testcases:
    sol = Solution().hammingWeight(n)
    print(sol)
