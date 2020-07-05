# abc002_3.py
Xa,Ya,Xb,Yb,Xc,Yc = map(int,input().split())
Xb -= Xa
Yb -= Ya
Xc -= Xa
Yc -= Ya
print(abs(Xb*Yc-Xc*Yb)/2)