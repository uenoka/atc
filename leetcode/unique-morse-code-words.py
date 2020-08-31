# unique-morse-code-words.py


class Solution:
    def makeMorseWords(self, words):
        morseCode = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--",
                     "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--.."}
        morsedWords = []
        for word in words:
            morsedWord = ""
            for char in word:
                morsedWord += morseCode[char]
            morsedWords.append(morsedWord)
        return morsedWords

    def uniqueMorseRepresentations(self, words) -> int:
        morsedWords = self.makeMorseWords(words)
        import collections
        C = collections.Counter(morsedWords)
        return len(C)


sol = Solution()
words = ["gin", "zen", "gig", "msg"]
print(sol.uniqueMorseRepresentations(words))
