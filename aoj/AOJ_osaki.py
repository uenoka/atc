# AOJ_osaki.py
def calc_imos(one_day):
    day = []
    cum_sum = 0
    for i in one_day:
        cum_sum += i
        day.append(cum_sum)
    return max(day)

def calc_time(time):
    h,m,s = map(int,time.split(":")) 
    return h*60*60 + m*60 + s

while True:
    N = int(input())
    if N==0:break
    one_day = [0]*(24*60*60+1) # 秒数で1日を管理する
    for i in range(N):
        start, end = input().split()
        # 時間を1日の秒数に直す
        # one_dayに累積和を登録していく
        start = calc_time(start)
        end = calc_time(end)
        one_day[start+1] += 1
        one_day[end+1] -= 1
    print(calc_imos(one_day))
# 累積和を計算して本数を計算するw