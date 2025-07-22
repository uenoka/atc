
'''
# 問題

二次元平面上に $N$ 個の都市があり、$1$ から $N$ までの番号が付けられています。

都市 $i$ は座標 $(X\_i, Y\_i)$ にあり、都市 $i$ から都市 $j$ までの距離は $\sqrt{(X\_i-X\_j)^2+(Y\_i-Y\_j)^2}$ です。

都市 $1$ から出発し、すべての都市を一度ずつ通った後、都市 $1$ へ戻ってくる経路のうち、合計距離ができるだけ短いものを出力してください。

# 考察

書籍の局所探索法をやってみる。
書籍では近傍を逆順にすることである程度良い回答が得られるといっているが、
その解法以外にいい方法はないかとかも調べたい。

'''
import time
start_time = time.time()
import random
def find_nearest_city(current_city, city, seen):
    xi,yi = city[current_city]
    min_distance = 10**9
    min_city = 0
    for city_number,xy in enumerate(city):
        # print(city_number,xy)
        xj,yj = xy
        if current_city == city_number:
            # print(f'now is current_city = city_number')
            continue
        if seen[city_number]:
            # print(f'current_city is already seen')
            continue
        if min_distance > ((xi-xj)**2+(yi-yj)**2)**0.5:
            # print(f'mindist is update')
            min_distance = ((xi-xj)**2+(yi-yj)**2)**0.5
            min_city = city_number
    return min_city

def reverse_slice(data, start, end):
    if not (0 <= start <= end <= len(data)):
        raise ValueError("無効なインデックス範囲です。")
    head = data[:start]
    middle = list(reversed(data[start:end]))
    tail = data[end:]
    return head + middle + tail

def calc(calc_route):
    # print(f'now calc {calc_route}')
    dist = 0
    for idx in range(2,len(calc_route)-1):
        start_city = city[calc_route[idx-2]-1]
        end_city = city[calc_route[idx-1]-1]
        # print(f'idx is {idx}, start city is {calc_route[idx-1]}, {start_city}, end city is {calc_route[idx]}, {end_city}')
        dist += ((start_city[0]-start_city[1])**2+(end_city[0]-end_city[1])**2)**0.5
    start_city = city[len(calc_route)-1]
    end_city = city[1]
    dist += ((start_city[0]-start_city[1])**2+(end_city[0]-end_city[1])**2)**0.5
    return dist

def local_search(local_route):
    while time.time() - start_time < 0.9:
        # print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
        start = random.randint(1,len(local_route)-1)
        end = random.randint(start,len(local_route)-1)
        if start == end:
            continue
        # print(f"start,end : {start} {end}")
        reversed_route = reverse_slice(local_route, start, end)
        # print(f'local search reversed route is : {reversed_route}')
        route_point = calc(local_route)
        reversed_point = calc(reversed_route)
        print(f'route point is {route_point}, reversed_point is {reversed_point}')
        if route_point>reversed_point:
            local_route = reversed_route
            # print(f'this route {local_route} is current minimum !')        
    return local_route

N = int(input())
city = []
for _ in range(N):
    X, Y = map(int,input().split())
    city.append([X,Y])
seen = [False for _ in range(N)]
seen[0] = True
current_city = 0
route = []
for i in range(N):
    route.append(current_city+1)
    current_city = find_nearest_city(current_city, city, seen)
    seen[current_city] = True
route = local_search(route)
for r in route:
    print(r)
print(1)