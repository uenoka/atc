# fizz-buzz.py
'''
普通のFizzBuzz。後はワンライナーにしてみたりくらいしかやることなさそう。
3の時にFizz?Buzz?どっち?って毎回なる
'''


class Solution:
    # def fizzBuzz(self, n: int) -> List[str]:
    def fizzBuzz(self, n: int):
        ans = []
        for i in range(1, n+1):
            if i % 15 == 0:
                ans.append("FizzBuzz")
            elif i % 3 == 0:
                ans.append("Fizz")
            elif i % 5 == 0:
                ans.append("Buzz")
            else:
                ans.append(str(i))
        return ans


sol = Solution()
n = 15
print(sol.fizzBuzz(n))
