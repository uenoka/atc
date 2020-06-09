# arc091_a.py
# def canGo(y,x):
#     if x>=0 and y>=0 and x<W and y<H:
#         return True
#     return False

# def operate(h,w):
#     dx = [-1,0,1]
#     dy = [-1,0,1]
#     for x in dx:
#         for y in dy:
#             if canGo(h+y,w+x):
#                 print("can go",h+y,w+x)
#                 glid[h+y][w+x] += 1


H,W = map(int,input().split())
h = H-2
w = W-2
if H==1:
    h=1
if W==1:
    w=1
print(h*w)
# glid = [[0]*W for _ in range(H)]
# print(glid)
# print("#######")
# for i in range(H):
#     for j in range(W):
#         print(i,j)
#         operate(i,j)
# print(glid)
