# abc166_c.py
'''
道でつながっている展望台のうち一番高いものを探す問題。
高さが同じ場合を考える必要があるかもしれないが、結局のところ「連結されたグラフ内で最大の値を探し出す」問題。
ということはいくつ連結グラフがあるかだけでいい…?ここがコーナーケースかな?
-> 題意読み違え。隣り合ったノードの中で一番大きいかどうか、だから連結グラフみたいなのは不要。
'''
N, M = map(int,input().split())
H = list(map(int,input().split()))
glaph = [[] for i in range(N)]
for i in range(M):
    a,b = map(int,input().split())
    glaph[a-1].append(b-1) 
    glaph[b-1].append(a-1)
highest = [False for i in range(N)]
for i in range(N):
    now = H[i]
    is_highest = True
    for neiber in glaph[i]:
        # print("now is",i,"neiber is",neiber,"Hi,Hneiber",H[i] , H[neiber])
        if highest[neiber] or H[i] <= H[neiber]:
            is_highest = False
            continue
    if is_highest:
        highest[i] = True
print(highest.count(True))
