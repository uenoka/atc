# abc147_c.py
'''
嘘つきと正直者の問題
各人Aiが嘘つきか正直者かを0,1で管理して、2^15 の探索を行う基本的なBit全探索。
証言のYijも嘘つき=0, 正直者=1 で表せるから、評価を論理和とか論理積とかでやってもいいかも。
'''
import itertools


def match(xy,pattern,n):
    lies = [-1]*n
    for i,v in enumerate(pattern):
        print("lies,xy",lies)
        if lies[i] != -1 and lies[i] != v:
            return
        lies[i] = v

        if v == 0:
            print("continue",i,v)
            continue
        else:
            for j in xy[i]:
                print("i,j",i,j)
                if lies[j[0]-1] == -1 :
                    lies[j[0]-1] = j[1]
                elif lies[j[0]-1] != v:
                    return
    print(pattern,"is true")
    return True


N = int(input())
XY = [0]*N
for i in range(N):
    A = int(input())
    a = []
    for _ in range(A):
        a.append(list(map(int, input().split())))
    XY[i] = a
status = [(0, 1) for _ in range(N)]
state = list(itertools.product(*status))
ans = []
for i in state:
    if match(XY,i,N):
        ans.append(i)
print(ans)
