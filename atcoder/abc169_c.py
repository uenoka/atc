# abc169_c.py
import decimal

A, B = input().split()
A = decimal.Decimal(A)
B = decimal.Decimal(B)
ans = A*B

print(int(ans))
