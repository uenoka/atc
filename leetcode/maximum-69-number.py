# maximum-69-number.py
class Solution:
    def maximum69Number(self, num: int) -> int:
        listNum = list(str(num))
        for i in range(len(listNum)):
            if listNum[i] == "6":
                listNum[i] = "9"
                break
        return int("".join(listNum))


sol = Solution()
num = 699996
print(sol.maximum69Number(num))
