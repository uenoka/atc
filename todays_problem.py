# 1373_a.py
import random
problem_list = [
    ['数学',
     ['https://atcoder.jp/contests/abc149/tasks/abc149_b',
      'https://atcoder.jp/contests/abc139/tasks/abc139_d',
      'https://atcoder.jp/contests/abc150/tasks/abc150_d',
      'https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_e',
      'https://atcoder.jp/contests/ddcc2020-qual/tasks/ddcc2020_qual_d',
      'https://atcoder.jp/contests/tenka1-2018-beginner/tasks/tenka1_2018_d',
      'https://atcoder.jp/contests/s8pc-1/tasks/s8pc_1_e',
      'http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=NTL_1_B&lang=ja',
      'https://atcoder.jp/contests/abc084/tasks/abc084_d',
      'http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=NTL_1_A&lang=ja']],

    ['その他の問題',
     ['https://atcoder.jp/contests/joi2008ho/tasks/joi2008ho_a',
      'https://atcoder.jp/contests/joi2013ho/tasks/joi2013ho1',
      'https://atcoder.jp/contests/s8pc-5/tasks/s8pc_5_b',
      'https://atcoder.jp/contests/abc144/tasks/abc144_d',
      'http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1193&lang=jp',
      'https://atcoder.jp/contests/s8pc-3/tasks/s8pc_3_b',
      'http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1149&lang=jp']],

    ['union find',
     ['http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_1_A&lang=ja',
      'https://atcoder.jp/contests/abc075/tasks/abc075_c?lang=ja',
      'https://atcoder.jp/contests/abc120/tasks/abc120_d']],

    ['累積和',
     ['https://atcoder.jp/contests/nikkei2019-final/tasks/nikkei2019_final_a',
      'https://atcoder.jp/contests/joi2010ho/tasks/joi2010ho_a',
      'https://atcoder.jp/contests/joi2011ho/tasks/joi2011ho1',
      'https://atcoder.jp/contests/abc106/tasks/abc106_d',
      'https://atcoder.jp/contests/gigacode-2019/tasks/gigacode_2019_d',
      'https://atcoder.jp/contests/abc014/tasks/abc014_3',
      'http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2013',
      'https://atcoder.jp/contests/joi2015ho/tasks/joi2015ho_a',
      'https://atcoder.jp/contests/joi2012ho/tasks/joi2012ho4']],

    ['逆元',
     ['https://atcoder.jp/contests/abc034/tasks/abc034_c',
      'https://atcoder.jp/contests/abc145/tasks/abc145_d',
      'https://atcoder.jp/contests/abc021/tasks/abc021_d',
      'https://atcoder.jp/contests/abc149/tasks/abc149_f']],

    ['最小全域木',
     ['https://atcoder.jp/contests/abc065/tasks/arc076_b',
      'http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1127',
      'https://atcoder.jp/contests/joisc2010/tasks/joisc2010_finals',
      'http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_2_A&lang=ja']],

    ['ワーシャルフロイド法',
     ['http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_C&lang=ja',
      'https://atcoder.jp/contests/abc012/tasks/abc012_4',
      'https://atcoder.jp/contests/abc079/tasks/abc079_d',
      'https://atcoder.jp/contests/abc074/tasks/arc083_b']],

    ['ダイクストラ法',
     ['http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_A&lang=ja',
      'https://atcoder.jp/contests/joi2008yo/tasks/joi2008yo_f',
      'https://atcoder.jp/contests/joi2016yo/tasks/joi2016yo_e',
      'https://atcoder.jp/contests/joi2014yo/tasks/joi2014yo_e']],

    ['DP(basic)',
     ['http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_10_A&lang=ja',
      'http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_B&lang=ja',
      'http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_C&lang=ja',
      'http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_A&lang=ja',
      'http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_10_C&lang=ja']],

    ['DP(ナップザックDP)',
     ['https://atcoder.jp/contests/joi2011yo/tasks/joi2011yo_d',
      'https://atcoder.jp/contests/joi2012yo/tasks/joi2012yo_d',
      'https://atcoder.jp/contests/joi2013yo/tasks/joi2013yo_d',
      'https://atcoder.jp/contests/joi2015yo/tasks/joi2015yo_d',
      'https://atcoder.jp/contests/pakencamp-2019-day3/tasks/pakencamp_2019_day3_d',
      'http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1167&lang=jp',
      'http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2199&lang=jp']],

    ['DP(区間DP)',
     ['http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_10_B&lang=ja',
      'https://atcoder.jp/contests/joi2015ho/tasks/joi2015ho_b',
      'http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1611&lang=jp']],

    ['DP(bit DP)',
     ['http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_2_A&lang=ja',
      'https://atcoder.jp/contests/s8pc-1/tasks/s8pc_1_g',
      'https://atcoder.jp/contests/joi2014yo/tasks/joi2014yo_d',
      'https://atcoder.jp/contests/joi2017yo/tasks/joi2017yo_d']],

    ['DP(other)',
     ['http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_D&lang=ja',
      'https://atcoder.jp/contests/abc006/tasks/abc006_4',
      'https://atcoder.jp/contests/abc134/tasks/abc134_e']],

    ['BFS',
     ['http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_C&lang=ja',
      'https://atcoder.jp/contests/abc007/tasks/abc007_3',
      'https://atcoder.jp/contests/joi2011yo/tasks/joi2011yo_e',
      'https://atcoder.jp/contests/joi2012yo/tasks/joi2012yo_e',
      'http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1166&lang=jp',
      'https://atcoder.jp/contests/abc088/tasks/abc088_d']],

    ['DFS',
     ['http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_B',
      'http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1160&lang=jp',
      'https://atcoder.jp/contests/abc138/tasks/abc138_d',
      'https://atcoder.jp/contests/joi2009yo/tasks/joi2009yo_d']],

    ['二分探索',
     ['http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_4_B&lang=ja',
      'https://atcoder.jp/contests/joi2009ho/tasks/joi2009ho_b',
      'https://atcoder.jp/contests/abc077/tasks/arc084_a',
      'https://atcoder.jp/contests/abc023/tasks/abc023_d',
      'https://atcoder.jp/contests/arc054/tasks/arc054_b',
      'https://atcoder.jp/contests/joi2008ho/tasks/joi2008ho_c']],

    ['順列全探索',
     ['https://atcoder.jp/contests/abc145/tasks/abc145_c',
      'https://atcoder.jp/contests/abc150/tasks/abc150_c',
      'http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_13_A&lang=ja']],

    ['Bit 全探索',
     ['http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_5_A&lang=ja',
      'https://atcoder.jp/contests/abc128/tasks/abc128_c',
      'https://atcoder.jp/contests/abc002/tasks/abc002_4',
      'https://atcoder.jp/contests/joi2008yo/tasks/joi2008yo_e',
      'https://atcoder.jp/contests/s8pc-4/tasks/s8pc_4_b']],

    ['全探索',
     ['http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_7_B&lang=ja',
      'https://atcoder.jp/contests/abc106/tasks/abc106_b',
      'https://atcoder.jp/contests/abc122/tasks/abc122_b',
      'https://atcoder.jp/contests/pakencamp-2019-day3/tasks/pakencamp_2019_day3_c',
      'https://atcoder.jp/contests/abc095/tasks/arc096_a',
      'https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_d',
      'https://atcoder.jp/contests/joi2007ho/tasks/joi2007ho_c',
      'https://atcoder.jp/contests/s8pc-6/tasks/s8pc_6_b',
      'https://atcoder.jp/contests/joi2008yo/tasks/joi2008yo_d'
      ]]
]
cnt = 0
todays_problem = [random.randint(0, 100) for i in range(3)]
for theme in problem_list:
    for problem in theme[1]:
        if cnt in todays_problem:
            print(theme[0])
            print(problem)
        cnt += 1
