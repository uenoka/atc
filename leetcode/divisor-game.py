# divisor-game.py
'''
概要：
あるゲームをアリスとボブが行う。
ゲームのルール：
N が与えられ x ( 0 < x < N and N%x = 0) を引き、N を N - x で置き換える。
アリスからこのゲームを始めて、操作が行えなくなったら最後に操作を行った人の勝ち。
アリスとボブが最適な手を取る場合、アリスが勝利するかどうかを判定する。
-> どう行動するのが最適といえる??ってのがむずい。たとえば N = 36 の時にどうすれば良いんだ?一番大きい約数を引くのがいいのか、約数によって異なるのか?
1 を踏んだら負け（操作できない）
2 を踏んだら勝ち（1 を引いて相手に 1 を渡す）
3 を踏んだら負け（1 を引いて相手に 2 を渡す）
4 を踏んだら勝ち（1 を引いて相手に 3 を渡せば勝ち）
5 を踏んだら負け（1 を引いて相手に 4 を渡す）
…みたいなのがあるはずだから、ボトムアップで行けば見えてくるかも??
-> これが DP ということかな?
ある数字が現れたらそれをメモしていくという形でメモ化再帰でいけるのかも
-> 実装方法：1,2 は決め打ちで False, True にする。
   その後は下からボトムアップで、 i の約数で相手が負ける（DP配列の中では False となっているもの）状態があれば勝ちとする、という流れで進めた。
-> 別解：偶奇見ればよかったらしいorz
'''
class Solution:
    def make_divisors(self,n):
            divisors = []
            for i in range(1, int(n**0.5)+1):
                if n % i == 0:
                    divisors.append(i)
                    if i != n // i and i != 1:
                        divisors.append(n//i)
            #divisors.sort()
            return divisors

    def divisorGame(self, N: int) -> bool:
        if N==1:
            return False
        dp = [False]*(N+1) # 1 based index
        dp[2] = True
        for i in range(3,N+1):
            divs = self.make_divisors(i)
            # print(i,divs)
            for j in divs:
                # print('i,j',i,j,dp[i-j])
                if dp[i-j] == False:
                    # print('here')
                    dp[i] = True
                
        # print(dp)
        return dp[N]

N = 999+1
sol = Solution().divisorGame(N)
print(sol)

