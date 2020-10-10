# test.py
'''
方針
・基本的には、いづれかのソートアルゴリズムを実装するような感じで進める
・上下関係は一意に決まるので、安定ソートである必要はない

聞かないとわからないこと
・モンスターの強さ（上下関係）は変更されうるか
  →されうるなら毎回APIを叩くことになるし、ランダムな順序なのでヒープソートやマージソートなどの早いソートを利用する
  →変更されない場合は以下のような戦略が取れそう
    ・一度比較を行ったデータはこっちで持っておいて、再度 API をたたかなくてもいいようにする
    ・まだ　cache していないデータが含まれているときのみ API をたたく
    ・cache しているデータが多い場合は Insertion sort とか、nearly sorted で早いアルゴリズムを使うなどを検討
    ・これは 引数の数と cache しているデータの数である程度出来そう?

・検証したいこと
  ・sort アルゴリズムの速度比較
    ・どのくらいソート済みの状態だとInsertion sortは早い?
      ・たとえば 100 のモンスターを比較するときに、そのうち 20 の順位が分かっている状態 (20% がソート済み) 、30, 40 と増えたときにどうなる??
'''

import json


class API:  # 2つのモンスターを渡されたときに、比較可能であれば比較した結果を返す。不可であれば0を返す（エラーの結果を0で代替）
    def __init__(self):
        self.monsters_lank = {
            'kitaro': 0,
            'griffin': 1,
            'vampire': 2,
            'dragon': 3,
            'troll': 4,
            'medusa': 5
        }

    def can_compare(self, m1, m2):
        if m1 == m2:
            return 0  # 同じモンスターはエラー
        if not m1 in self.monsters_lank or not m2 in self.monsters_lank:  # リストにないモンスターはエラー
            return 0
        return True

    def compare(self, m1, m2):

        if not self.can_compare(m1, m2):
            return 0
        if self.monsters_lank[m1] < self.monsters_lank[m2]:
            return '{"winner":"' + m1 + '", "loser":"' + m2 + '"}'
        else:
            return '{"winner":"' + m2 + '", "loser":"' + m1 + '"}'


def sort_monsters(monsters):
    for i in range(1, len(monsters)):
        v = monsters[i]
        j = i-1
        while j >= 0 and compare(monsters[j], v):
            monsters[j+1] = monsters[j]
            j -= 1
    return monsters


def compare(m1, m2):
    api = API()
    result = api.compare(m1, m2)
    if result == 0:
        print("error occur")
        exit()

    result = json.loads(result)
    print(result)


monsters = ["vampire", "troll", "kitaro"]
print(sort_monsters(monsters))
'''
'kitaro': 0,
'griffin': 1,
'vampire': 2,
'dragon': 3,
'troll': 4,
'medusa': 5
の順で強い
'''
