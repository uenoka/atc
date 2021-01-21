# ALDS1_5_C.py
def koch_curve(start, end, n):
    if n == 0:
        return
    s, u, t = calc(start, end)
    koch_curve(start, s, n-1)
    print(s)
    koch_curve(s, u, n-1)
    print(u)
    koch_curve(u, t, n-1)
    print(t)
    koch_curve(t, end, n-1)


def calc(start, end):
    s = ((2*start[0]+end[0])/3, (2*start[1]+end[1])/3)
    t = ((start[0]+2*end[0])/3, (start[1]+2*end[1])/3)
    # u = (t[0]-s[0])*cos(th)

    return (1, 2, 3)


N = int(input())
koch_curve((0, 0), (100, 0), N)
