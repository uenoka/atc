# unique-morse-code-words.py


class Solution:

    def uniqueMorseRepresentations(self, words) -> int:
        morseCode = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--",
                     "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--.."}
        morsedWords = set()
        for word in words:
            morsedWord = ""
            for char in word:
                morsedWord += morseCode[char]
            morsedWords.add(morsedWord)
        return len(morsedWords)


sol = Solution()
words = ["gin", "zen", "gig", "msg"]
print(sol.uniqueMorseRepresentations(words))
