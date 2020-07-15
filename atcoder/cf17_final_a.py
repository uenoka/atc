# cf17_final_a.py
import re
S = input()
if re.fullmatch('A?KIHA?BA?RA?', S):
    print('YES')
else:
    print('NO')
