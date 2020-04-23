#abc128_b.py
'''
こういうのも苦手、配列とか Map のソートとか SQL の order by で書きたくなる…
とりあえず解説ACというか、回答読んで理解する。
tuple の配列は sorted 関数使うと左から順に昇順になるってことらしい
↓が詳しそう。
https://qiita.com/tag1216/items/95dc6bff5422e26601bf
'''
n = int(input())
rs = []
for i in range(n):
    s, p = input().split()
    p = int(p)
    rs.append((s, -p, i+1))
rs = sorted(rs)
for r in rs:
    print(r[2])