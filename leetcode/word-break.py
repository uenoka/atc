# word-break.py
'''
BFS or DFS での解法
最初に s を deque (BFS, DFS 両方でできるようにしているだけ) に入れて、各 wordDict で始まるかを判定する
いづれかの wordDict で始まる場合は seen に「その wordDict を排除した文字列」を登録することで一意に残りの文字列を管理している。
seen を管理することで残りの文字列をメモ化するのと同等の方法になる。（残りの文字列が同じであればT/Fは同じになるので重複せずに済む）
'''
class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        from collections import deque
        q = deque([s])
        seen = set()
        while q:
            s = q.popleft()    # popleft() = BFS ; pop() = DFS
            for word in wordDict:
                if s.startswith(word):
                    new_s = s[len(word):]
                    if new_s == "": 
                        return True
                    if new_s not in seen:
                        q.append(new_s)
                        seen.add(new_s)
        return False


# s = "leetcode"
# wordDict = ["leet", "code"]
s = "catsanddog"
wordDict = ["cat","s","dog",  "and", "cats"]
sol = Solution().wordBreak(s,wordDict)
print(sol)
