# arc015_2.py
N = int(input())
M = [input().split() for i in range(N)]
temp = [0]*6  # 0:猛暑日、1:真夏日、2:夏日、3:熱帯夜、4:冬日、5:真冬日
MT = []
for n, m in M:
    n = n.replace(".", "")
    m = m.replace(".", "")
    MT.append((int(n), int(m)))
print(MT)
# for n, m in MT:
#     if n
