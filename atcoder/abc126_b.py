# abc126_b.py
def mm(n):
    if 0 < n and n < 13:
        return True
    else:
        return False

S = input()

head = int(S[:2])
tail = int(S[2:])
head_mm = mm(head)
tail_mm = mm(tail)
if head_mm and tail_mm:
    print("AMBIGUOUS")
elif head_mm:
    print("MMYY")
elif tail_mm:
    print("YYMM")
else:
    print("NA")