
'''
# 問題

二次元平面上に $N$ 個の都市があり、$1$ から $N$ までの番号が付けられています。

都市 $i$ は座標 $(X\_i, Y\_i)$ にあり、都市 $i$ から都市 $j$ までの距離は $\sqrt{(X\_i-X\_j)^2+(Y\_i-Y\_j)^2}$ です。

都市 $1$ から出発し、すべての都市を一度ずつ通った後、都市 $1$ へ戻ってくる経路のうち、合計距離ができるだけ短いものを出力してください。

# 考察

愚直に一番近いところを見ていったら4230 / 1000。
次のアイデアとして、ある程度近い都市をグルーピングして、そのグループを周遊→次のグループということはしたくなるね。
イメージは機械学習のクラスタリングを噛ませるような。

'''

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

N = int(input())
city = []
for _ in range(N):
    X, Y = map(int,input().split())
    city.append([X,Y])
seen = [False for _ in range(N)]
seen[0] = True
current_city = 0
for i in range(N):
    print(current_city+1)
    current_city = find_nearest_city(current_city, city, seen)
    seen[current_city] = True
print(1)