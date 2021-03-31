# longest-palindromic-substring.py
'''
普通の全探索で実装（1000文字の文字列だとTLEするのでとりあえずsが回文かどうかを最初に判定）
他の解法として
・Manacher's Algorithm
  -> O(N) でできるアルゴリズム。ただしこれがコーディングインタビューで出ることはまずない(面白いから見ておくといいけどね、とのこと)
・Expand Around Center (O(N^2))
  -> 中心を広げていく方法？これはちょっとよくわからない
・DP O(N^2)
  -> 全探索を改善する方法。
     ababa という文字列があった時に、すでに bab が回文であるということが分かっていれば、 bab に同じ文字を追加しているので回文ということが分かる
・Longest Common Substring (LCS) O(N^2) 
  -> 逆順にした s' と s の最長共通部分を求めることで答えが出る
がある。
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(s):
            head = s
            tail = s[::-1]
            if head == tail:
                return True
            return False

        length = len(s)
        if isPalindrome(s):
            return s
        m = ''
        # print('===start===',s)
        for i in range(length):
            for j in range(i,length+1):
                # print(i,j,s[i:j+1])
                if isPalindrome(s[i:j]):
                    if len(m)<(j-i):
                        m = s[i:j]
        return m

testcases=[
    'cbbd',
    'babad',
    'ac',
    'a',
    'aa',
    'aaa',
    'aaaa',
    "ymgkhlrxcabgwziguqjfjqfbfoacyywccbbofqyvmutocnqdrdjpjpvkmhadghbmjgtrafaxgwjfausrurxsfoazyuidvtwavwtojuktafoqzhrofcyvubdnqgmrktuesieqfhcohflyrgwtrtxqvkelyyzrgbltcesqhlvadmdztpkhaqrbhnvekebzkbjtpyuyrzppahembgczswkzbifukzwslsyxngwumeimuvtgkrrvvhbmbgtjymgbvaoebswgkruzgjenucrxxzldeifuqshjnyhcahzsjalqenojbxtnohfdrxozrtclqesuyyerthwbvfrmrprxnevbtqhsxufkxrcgexixfhtteairjlmqobprxblyqcojhbbxykwudnaanduwkyxbbhjocqylbxrpboqmljriaetthfxixegcrxkfuxshqtbvenxrprmrfvbwhtreyyuseqlctrzoxrdfhontxbjoneqlajszhachynjhsqufiedlzxxrcunejgzurkgwsbeoavbgmyjtgbmbhvvrrkgtvumiemuwgnxyslswzkufibzkwszcgbmehappzryuyptjbkzbekevnhbrqahkptzdmdavlhqsectlbgrzyylekvqxtrtwgrylfhochfqeiseutkrmgqndbuvycforhzqofatkujotwvawtvdiuyzaofsxrursuafjwgxafartgjmbhgdahmkvpjpjdrdqncotumvyqfobbccwyycaofbfqjfjqugizwgbacxrlhkgmy"
]
for s in testcases:
    sol = Solution().longestPalindrome(s)
    print(sol)
