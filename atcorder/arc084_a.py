# abc077_c.py
'''
多分あとは、Bで重複がある場合は探索しないで個数かけていくとかにしないといけない。
結局自分の方針ではできないことが分かったので解説AC
Bを固定すれば、各Biに対してそれより小さいAの個数*それより大きいCの個数 をそれぞれ足し合わせれば行ける。
このアイデアもすげー天才的…
'''
def is_okC(idx,key,target):
########## wirte criteria here ##########
    if target[idx] > key:
        return True
    return False

def meguru_bisectC(key,target):
    left = -1
    length = len(target)
    right = length
    while (abs(right - left) > 1):
        mid = left + (right - left) // 2
        if is_okC(mid,key,target):
            right = mid
        else:
            left = mid
    return length-right


def is_okA(idx,key,target):
########## wirte criteria here ##########
    if target[idx] >= key:
        return True
    return False

def meguru_bisectA(key,target):
    left = -1
    length = len(target)
    right = length
    while (abs(right - left) > 1):
        mid = left + (right - left) // 2
#        print("mid : " , mid)
        if is_okA(mid,key,target):
            right = mid
        else:
            left = mid
    return right

N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
A.sort()
C.sort()
a = 0
c = 0
ans = 0
#print(A)
#print(B)
#print(C)
for i in B:
    a = meguru_bisectA(i,A)
#    print(A[:a] )
#    print("i : ",i)
    c = meguru_bisectC(i,C)
#    print(C[c:])
    ans += a*c
#    print()

print(ans)