import sys
# 基本方針：動的計画法
# 制約上は2桁の10進数（少数可）だったので、10000のような値はなさそう

for line in sys.stdin:
    price,paid = line.split(";")
if price>paid:
    print("ERROR")
    exit()
if price==paid:
    print("ZERO")
    exit()

charge = paid-price
# 縦軸に通貨、横軸にお釣りを設定したDPテーブルを用意する
dp = [[0]*(int(charge*100)+1) for i in range(13)]
currency = [0,1,5,10,25,50,100,200,500,1000,2000,5000,10000]
for i in range(1,13):
    
print(price,paid,end="")