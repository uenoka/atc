# first-unique-character-in-a-string.py
'''
python だったら Collection.counter でやるのが楽そう。
それか dict を前処理で作ってあげて、元の文字列で全探索
'''
from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(list(s))
        for i, c in enumerate(s):
            if counter[c] == 1:
                return i
        return -1
