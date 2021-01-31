# Repeated_squares.py
def myPow(x,n):
    if n<0:
        x = 1/x
        n = -n
    if n==0:
        return 1
    if n==1:
        return x
    if n%2 == 1:
        return x * myPow(x**2,n//2)
    return myPow(x**2, n//2)


x = 32.34
n = 100
print(myPow(x,n))
