# nabc123_b.py
# 調理時間%10=0 をとった後、調理時間%10 が大きい順にとって行く
dishes = [int(input()) for i in range(5)]
lest_time = 0
ans = 0
for dish in dishes:
    if dish%10==0:
        ans += (dish)
    else:
        ans += (dish+10-dish%10)
    if lest_time < 10-dish%10 and dish%10!=0:
        lest_time = 10-dish%10
print(ans-lest_time)    
