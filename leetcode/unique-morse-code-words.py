# unique-morse-code-words.py


class Solution:

    def makeMorseWords(self, words):
        morseCode = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--",
                     "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--.."}
        morsedWords = set()
        for word in words:
            morsedWord = ""
            for char in word:
                morsedWord += morseCode[char]
            morsedWords.add(morsedWord)
        return morsedWords

    def uniqueMorseRepresentations(self, words) -> int:
        morsedWords = self.makeMorseWords(words)
        return len(morsedWords)


sol = Solution()
words = ["gin", "zen", "gig", "msg"]
print(sol.uniqueMorseRepresentations(words))
