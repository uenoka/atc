# word-ladder.py
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        q = deque()
        q.append((beginWord,1))
        while q:
            word,dist = q.popleft()
            if word == endWord:
                return dist
            for i in range(len(word)):
                for c in alphabet:
                    tmpWord = word[:i] + c + word[i+1:]
                    if tmpWord in wordList:
                        q.append((tmpWord,dist+1))
                        wordList.remove(tmpWord)
        return 0


testcases = [
    ["hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]],
    ["hit", "cog", ["hot", "dot", "dog", "lot", "log"]],
]
for beginWord, endWord, wordList in testcases:
    sol = Solution().ladderLength(beginWord, endWord, wordList)
    print(sol)
