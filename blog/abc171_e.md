# abc171_e.md

## 問題

## 要するにこの問題は何すれば通るの?

- それぞれの Ai を全部 XOR とる。（for で回す）

    ```python
    xors = 0
    for i in A:
        xors ^= i
    ```

- すべての Ai の XOR （上のコードの xors ）と、それぞれの Ai との XOR が Bi になるので、出力する。

    ```python
    ans = []
    for i in A:
        ans.append(i^xors)
    ```

## 何でこんなことができるの?

### 重要な法則

- a XOR a = 0
- XOR は結合法則が成り立つ

よくよく考えてみると、すべての Ai の XOR をとった xors は、制約が偶数になっていることから、↓のようなことが言える

```txt
すべて奇数回 XOR をとったものの値
```

その xors と Ai を XOR をとるとどうなるかというと、

```例
Ai = A1 A2 A3 A4
が与えられたとき
xors は、(A2^A3^A4)^(A1^A3^A4)^(A1^A2^A4)^(A1^A2^A3) となる。
これを結合法則で並び変えると、(A1^A1^A1)^(A2^A2^A2)^(A3^A3^A3)^(A4^A4^A4) になる。
ここで Ai は Bi 以外の値を XOR した値なので、↓のように書き換えられる。
A1 = B2^B3^B4
A2 = B1^B3^B4
A3 = B1^B2^B4
A4 = B1^B2^B3
xors = (B2^B3^B4^B2^B3^B4^B2^B3^B4)^(B1^B3^B4^B1^B3^B4^B1^B3^B4)^(B1^B2^B4^B1^B2^B4^B1^B2^B4)^(B1^B2^B3^B1^B2^B3^B1^B2^B3)

（書いてて大変になってきた。。。）

さらにこれを並べ替えて見やすくすると、
xors = (B1^B1^B1^B1^B1^B1^B1^B1^B1)^(B2^B2^B2^B2^B2^B2^B2^B2^B2)^(B3^B3^B3^B3^B3^B3^B3^B3^B3)^(B4^B4^B4^B4^B4^B4^B4^B4^B4)

となります。

（もうちょっと頑張ればきっと見えるはず。。。）

さらに、ためしにこれと A1 を XOR をとってみると

xors^A1 = (B1^B1^B1^B1^B1^B1^B1^B1^B1)^(B2^B2^B2^B2^B2^B2^B2^B2^B2)^(B3^B3^B3^B3^B3^B3^B3^B3^B3)^(B4^B4^B4^B4^B4^B4^B4^B4^B4)^A1

A1 は B2^B3^B4 かけることが分かっているので（大変ですが、がんばって思い出してください。。。！）さらに式変形すると、

xors^A1 = (B1^B1^B1^B1^B1^B1^B1^B1^B1)^(B2^B2^B2^B2^B2^B2^B2^B2^B2)^(B3^B3^B3^B3^B3^B3^B3^B3^B3)^(B4^B4^B4^B4^B4^B4^B4^B4^B4)^A1 = (B1^B1^B1^B1^B1^B1^B1^B1^B1)^(B2^B2^B2^B2^B2^B2^B2^B2^B2)^(B3^B3^B3^B3^B3^B3^B3^B3^B3)^(B4^B4^B4^B4^B4^B4^B4^B4^B4)(B2^B3^B4)

さてあと一歩です！

これを並び変えて見やすくすると
xors^A1 = (B1^B1^B1^B1^B1^B1^B1^B1^B1)^(B2^B2^B2^B2^B2^B2^B2^B2^B2^B2)^(B3^B3^B3^B3^B3^B3^B3^B3^B3^B3)^(B4^B4^B4^B4^B4^B4^B4^B4^B4^B4)
となります。
さらに！ a XOR a = 0 ということなので、偶数個になっているところをすべて消していくと、なんと B2、B3、B4 すべて 0 になってしまいます。
B1は奇数個ですが、1つを残せば偶数個部分が消せるので消してしまいましょう。

xors^A1 = B1^0^0^0

とんでもなくシンプルになってきました。

さらにさらにさらに！
0 XOR a = a が成り立つので、0 は即座に消してしまっていいようです。
とすると、この通り、B1 が求められました。
xors^A1 = B1
```

## XOR とは

### 概要

- `排他的論理和` のこと
- ブール論理やビット演算において、2つの入力のうちどちらかが真，どちらかが偽の時にのみ真になる演算。
- 真偽値表の下のような形になる。

|       | True   | False  |
| ----- | ------ | ------ |
| True  | False  | `True` |
| False | `True` | False  |

- 01 で表すと↓のようになる

|     | 0   | 1   |
| --- | --- | --- |
| 0   | 0   | `1` |
| 1   | `1` | 0   |

- 数字に対して XOR をとる場合、2進数に変換して各桁での XOR をとる
  - 例：3 XOR 4 = 011 XOR 100 = 111 = 7
  - 例：3 XOR 5 = 011 XOR 101 = 110 = 6
  - 例：3 XOR 3 = 011 XOR 011 = 000 = 0
  - etc...

### 性質

- 交換法則が成り立つ
- a XOR a = 0
- ある数 x の b 番目のビットが 1 <=> x mod 2^(b+1) >= 2^b
- 0 <= a のとき, 4a, 4a+1, 4a+2, 4a+3 の XOR 和は 0

### 競技プログラミングでのXOR

#### XOR という題名の問題

- <https://atcoder.jp/contests/abc050/tasks/arc066_b>
- <https://atcoder.jp/contests/abc098/tasks/arc098_b>
- <https://atcoder.jp/contests/abc117/tasks/abc117_d>
- <https://atcoder.jp/contests/abc121/tasks/abc121_d>
- <https://atcoder.jp/contests/abc126/tasks/abc126_f>
- <https://atcoder.jp/contests/abc141/tasks/abc141_f>
- <https://atcoder.jp/contests/abc129/tasks/abc129_e>
- <https://atcoder.jp/contests/abc147/tasks/abc147_d>
- <https://atcoder.jp/contests/abc150/tasks/abc150_f>

ほかにもけんちょんさんのブログでXORカテゴリを見るとリストが見られる。
<https://drken1215.hatenablog.com/archive/category/XOR>

### その他

- 性質が面白いため問題を作りやすい

## 問題の解き方

## 参考

<https://qiita.com/kuuso1/items/778acaa7011d98a3ff3a>
<https://www.hamayanhamayan.com/entry/2017/05/20/145021>
