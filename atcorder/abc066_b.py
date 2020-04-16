#abc066_b
def is_odd_str(str):
    length=len(str)
    if length%2==1:
        return False
    else:
        if str[:length//2]==str[length//2:]:
            return True
        else :
            return False
S = input()
rep = len(S)
for i in range(rep):
    S = S[:-1]
    if is_odd_str(S):
        print(len(S))
        break