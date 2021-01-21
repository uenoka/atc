# hamming-distance.py
'''
bin 関数と format 関数が2進数表記するときに使える。
ただし帰ってくるのが文字列なのでそれの扱い方が結構面倒。今回は xor をとってそのあと xor の各桁が1なら0, 1 が違うということで for 文で回した。
'''
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = format(x ^ y, 'b')
        cnt = 0
        for i in xor:
            if i == '1':
                cnt += 1
        return cnt


sol = Solution()
x = 1
y = 4
print(sol.hammingDistance(x, y))
