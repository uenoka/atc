# arc033_2.py
'''
要約すると、A,Bの共通文字列の数/A,Bのどちらかに含まれている文字列の数
共通する文字列の数をCとすると求める答えは、かぶったところを引くので
C/(A+B-C) 
になる。
なので単純にCを高速に求めていきたい、という問題になる。
'''
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
