# abc064_c.py
def _min(rates):
    return max(len(rates)-rates.count(0),1)

def _max(rates,free):
    return min(len(rates)-rates.count(0)+free,n)

n = int(input())
a = list(map(int,input().split()))
rates = [0]*8
free = 0
for i in a:
    if i<400: #gray
        rates[0] += 1
    elif i<800: #cha
        rates[1] += 1
    elif i<1200: #green
        rates[2] += 1
    elif i<1600: #water
        rates[3] += 1
    elif i<2000: #blue
        rates[4] += 1
    elif i<2400: #yellow
        rates[5] += 1
    elif i<2800: #daidai
        rates[6] += 1
    elif i<3200: #red
        rates[7] += 1
    else:
        free += 1
print(_min(rates),_max(rates,free))
