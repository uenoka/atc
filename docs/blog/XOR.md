---
title: "XOR の性質について学習"
---

# XOR

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