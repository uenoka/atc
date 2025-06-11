'''
# 問題

$1$ 以上 $N$ 以下の整数のうち、 $3,5$ のいずれかで割り切れるものは何個ありますか。

# 考察

3で割り切れる+5で割り切れる-15で割り切れる

'''
N = int(input())
three = N // 3
five = N // 5
fifteen = N // 15
print(three + five - fifteen) 