'''
input : 数字
return : a^p,b^q,...,c^r を {a:p,b:q,...,c:r} の dict で表したもの
'''
def can_div(z):
    target = [2,3,4,5,7,8,9,11,13,16,17,19,23,25,27,31,36,37,41,47,49]
    if z in target:
        return True
    return False

def choice(_min,n):
    z = _min
    while True:
        z+=1
        if z%N != 0:
            continue
        if not can_div(z):
            continue
    # z はNで割り切れる
    # z は素数のe乗で表せる
    # もし選べなかったら-1でbreak条件にする
    return z