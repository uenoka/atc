# goal-parser-interpretation.py
'''
実験してみる
・普通に replace するとどのくらいかかるか -> 28ms
・deque とかにしてpopしていくとどのくらいかかるか -> 32ms
普通に replace のが早くて草
というかなんでdequeにした。。。どう考えてもidx のほうがいいじゃん（いいじゃん）
こういうdequeかなぁみたいな発想をした瞬間に他の実装を検討できないのダメだなぁ
とはいえidxのほうでも 32 ms だからreplace が一番早いな…
'''
from collections import deque
class Solution:
    def interpret(self, command: str) -> str:
        def interpretIdx(command):
            ans = ''
            for i in range(len(command)):
                if command[i] == 'G':
                    ans += 'G'
                elif command[i] == '(':
                    i += 1
                    if command[i]==')':
                        ans += 'o'
                    else:
                        ans+= 'al'
                        i += 2 
            return ans

        def interpretDeque(command):
            command = deque(list(command))
            ans = ''
            while command:
                str = command.popleft()
                if str == '(':
                    str2 = command.popleft()
                    if str2 == ')':
                        ans += 'o'
                    else:
                        ans += 'al'
                        command.popleft()
                        command.popleft()
                else:
                    ans += 'G'
            return ans
        def interpretReplace(command):
            return command.replace('(al)','al').replace('()','o')

        # return interpretDeque(command)
        # return interpretReplace(command)
        return interpretIdx(command)


testcases =[
    "G()(al)",
    "G()()()()(al)",
    "(al)G(al)()()G"
]
for command in testcases:
    sol = Solution().interpret(command)
    print(sol)
