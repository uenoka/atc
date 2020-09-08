def gen_d_prim(n):
    D = [0] * (n+1)
    for i in range(2, n+1):
        if D[i] > 0:
            continue
        for j in range(i, n+1, i):
            D[j] = i
    return D


print(gen_d_prim(100))
