# count-the-number-of-consistent-strings.py
class Solution:
    def countConsistentStrings(self, allowed: str, words) -> int:
        allowed = set(list(allowed))
        cnt = 0
        for word in words:
            for c in word:
                if c not in allowed: 
                    cnt += 1
                    break
        return len(words)-cnt

testcases = [
    ["ab", ["ad", "bd", "aaab", "baa", "badab"]],
    ["abc",["a", "b", "c", "ab", "ac", "bc", "abc"]],
    ["cad",["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]],
    ["exdohslrwipnt",["xrwlstne", "rs", "ioetdll", "lwi", "r", "pieonois", "r", "xtp", "stia", "gicfuvmnr", "hdntpxse", "sodxws", "v", "hstirooon", "d"]]]
for allowed,words in testcases:
    sol = Solution().countConsistentStrings(allowed, words)
    print(sol)
