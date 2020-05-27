# abc114_c.py
'''
再帰関数で実装するとわかりやすいらしいが、
3,5,7すべてを利用しているという条件と、カウントが難しい
'''
N = int(input())
def bfs(A,use,counter):
    if A > N:
        return
    if use == 0b111:
        counter += 1
    bfs(A*10+7,use|0b011,counter)
    bfs(A*10+5,use|0b010,counter)
    bfs(A*10+3,use|0b100,counter)
res = 0
bfs(0,0,res)
print(res)
