# abc108_b.py
# 与えられた正方形が外接する、辺がX,Y軸に平行な正方形を考えるとわかりやす。
x1,y1,x2,y2 = map(int,input().split())
a = x2-x1
b = y2-y1
print(x2-b,y2+a,x1-b,y1+a)
