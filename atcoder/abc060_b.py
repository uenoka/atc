# abc060_b.py
'''
A,B,Cの関係を調べればO(1)で解ける問題だが、そんなことしなくても
いくつかAの倍数を選んだ時の総和はAの倍数なので、愚直にAの倍数を全探索する方法でやるほうが楽。
'''
A, B, C = map(int, input().split())
ans = 'NO'
for i in range(1, 1000):
    if A*i % B == C:
        ans = 'YES'
        break
print(ans)
