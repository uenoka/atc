---
title: "ABC 162 D"
---

# abc162_d

## 考えたこと

愚直に 3 重の for ではできないことはわかっていたが、まずは問題の回答が出せる状態をと考えて愚直に、以下のような 3 重 for 文で実装してみた。

```py
N = int(input())
S = input()
ans = 0
for i in range(N):
    for j in range(i,N):
        for k in range(j,N):
            if j-i != k-j:
                if S[i]!=S[j] and S[i]!=S[k] and S[k]!=S[j]:
                    ans += 1
print(ans)
```

当然提出しても TLE になるためいったん落ち着いて眺めてみると、ABSに類似の問題があったことに気づく。（3重for文を2重に落とすテクニック。-> [ABS](https://qiita.com/drken/items/fd4e5e3630d0f5859067#%E7%AC%AC-8-%E5%95%8F--abc-085-c---otoshidama-300-%E7%82%B9) ）  
ただし、上の実装では、k を一意に定めることができずうまくいかなかった。  
その後、S[i], S[j], S[k] が互いに異なるということは、R, G, B をひとつずつとってくることと同義だと気づく。  
ただし、この時に k-i != k-j かつ S[i] != S[j] != S[k] のものを全体から差し引かなくてはいけない、という処理を考えているうちにコンテストが終わった。

最終的にコンテスト後にACしたコードは↓のもの。

```py
n = int(input())
s = input()
r = s.count("R")
g = s.count("G")
b = s.count("B")
cnt= 0
for i in range(n):
    for j in range(i,n):
        if 2*j-i<n:
            if s[i] != s[j] and s[i] != s[2*j-i] and s[j] != s[2*j-i]:
                cnt += 1
print(r*g*b-cnt)

```

## 参考にしたもの

けんちょんさんのブログがちょうど自分と同じ解法だったので、参考にさせていただきました。[けんちょんさんのブログ](https://drken1215.hatenablog.com/entry/2020/04/12/225900)

## 感想

正直これはできたかったなぁ…、ただ、けんちょんさんの解法を読んでいるうちに j-i!=k-j のところをうまう扱って k = 2j-i として 3 重ループを消しており、コンテスト中にこの発想が自分にできただろうかというと微妙なところなので、この考え方を身に着けたいなというところ。

## 別解

コンテスト後に、Dは累積和でやったという人がいたので、そっちも後々別解の考え方をきちんとできるようにしておきたい。（覚えてたら後で書く）
