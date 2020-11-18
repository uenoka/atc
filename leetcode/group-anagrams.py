# group-anagrams.py
class Solution:
    def groupAnagrams(self, strs):
        find = {}
        for s in strs:
            settedstr = str(sorted(s))
            if find.get(settedstr):
                find[settedstr].append(s)
            else:
                find[settedstr] = [s]
        return find.values()


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
sol = Solution().groupAnagrams(strs)
print(sol)
