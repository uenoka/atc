# arc096_a.py
'''
以前解いていたが、結構わからなかった。
結局のところ、難しく A, B, C の値段の関係を考えるのではなく
C を i*2 枚買うときには、A,B はそれぞれX-i, Y-i 枚必要になるので
それを全探索して最少をみつけるのがよい。
'''
A,B,C,X,Y = map(int,input().split())
ans = 10**9+7
list_ = []
for i in range(10**5+1):
    if ans > (2*C*i + max(0,Y-i)*B + max(0,X-i)*A ):
        ans = (2*C*i + max(0,Y-i)*B + max(0,X-i)*A )
print(ans)
