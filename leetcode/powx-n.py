# powx-n.py
'''
math を使っちゃいようにして実装するとすると、繰り返し二乗法なんだろうな。出来るかな??
負の数になった場合は、一旦正数にして逆数をとれば後は同じ処理をすればよいという発想。なるほど。
'''
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        if n<0:
            n = -n
            x = 1/x
        return self.myPow(x**2, n/2) if n % 2 == 0 else x*self.myPow(x**2, n//2)

x= 34.00515
n=-3
sol = Solution().myPow(x,n)
print(sol)
