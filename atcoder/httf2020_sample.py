import math
import string
import itertools
import fractions
import heapq
import collections
import re
import array
import bisect
import sys
import copy
import functools
import time
import random

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(): return [list(map(int, l.split())) for l in sys.stdin.readlines()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)
def pe(s): return print(str(s), file=sys.stderr)
def JA(a, sep): return sep.join(map(str, a))
def JAA(a, s, t): return s.join(t.join(map(str, b)) for b in a)


EMPTY = 0
GOAL = 1
BLOCK = 2
USE = 3
tt = 0


def main():
    starttime = time.time()
    random.seed()
    N, M, B = LI()
    A = [[0]*N for _ in range(N)]
    gy, gx = LI()
    A[gy][gx] = GOAL
    ddi = {}
    ddi['U'] = 0
    ddi['R'] = 1
    ddi['D'] = 2
    ddi['L'] = 3
    ddc = ['U', 'R', 'D', 'L']
    C = []
    CK = []
    for i in range(M):
        y, x, c = LS()
        C.append((int(y), int(x), ddi[c]))
        CK.append(int(y)+(int(x) << 6)+(ddi[c] << 12))
    bb = [LI() for _ in range(B)]
    for y, x in bb:
        A[y][x] = BLOCK

    def search(sa, ll):
        global tt
        stt = time.time()
        d = collections.defaultdict(lambda: ll)
        q = []
        for sy, sx in sa:
            for di in range(4):
                s = sy+(sx << 6)+(di << 12)
                d[s] = 0
                heapq.heappush(q, (0, s))
        v = collections.defaultdict(bool)
        while len(q):
            k, u = heapq.heappop(q)
            if v[u]:
                continue
            v[u] = True
            uy = u % 64
            ux = (u >> 6) % 64
            uc = u >> 12

            for di in range(4):
                vd = k
                if di == uc:
                    vy = (uy - dd[di][0]) % N
                    vx = (ux - dd[di][1]) % N
                    if A[vy][vx] == BLOCK:
                        continue
                else:
                    vy = uy
                    vx = ux
                    vd += 1

                uv = vy+(vx << 6)+(di << 12)
                if v[uv]:
                    continue
                if d[uv] > vd:
                    d[uv] = vd
                    heapq.heappush(q, (vd, uv))

        tt += time.time() - stt
        return d

    SD = search([(gy, gx)], 100)
    pe(len(SD))
    MK = {}
    MSC = inf
    mkv = set()

    lf = True
    ttt = 0
    while lf:
        ttt += 1
        A = [[0]*N for _ in range(N)]
        A[gy][gx] = GOAL
        for y, x in bb:
            A[y][x] = BLOCK
        D = collections.defaultdict(lambda: 100)
        for k, v in SD.items():
            D[k] = v
        K = {}
        NK = set()
        while True:
            gt = time.time() - starttime
            if gt > 2.9:
                lf = False
                break
            mc = inf
            mi = -1
            tc = 1
            for ci in CK:
                t = D[ci]
                if t == 0:
                    continue
                if t < mc:
                    mc = t
                    mi = ci
                    tc = 1
                elif t == mc:
                    tc += 1
                    if random.randrange(tc) == 0:
                        mc = t
                        mi = ci
            # pe("{}, {}, {}".format(mc,mi,tc))

            if mi == -1 or mc == 10:
                break

            ty = mi % 64
            tx = mi // 64 % 64
            tc = mi >> 12
            f = True
            kk = []
            sf = True
            while True:
                tk = D[ty+(tx << 6)+(tc << 12)] - 1
                if tk < 0:
                    break

                mi = -1
                for i in range(N):
                    uy = (ty + dd[tc][0] * i) % N
                    ux = (tx + dd[tc][1] * i) % N
                    if A[uy][ux] == BLOCK:
                        break
                    mc = 0
                    for di in range(4):
                        if di == tc or (uy, ux, di) in NK:
                            continue
                        dk = D[uy+(ux << 6)+(di << 12)]
                        if dk <= tk:
                            mc += 1
                            if random.randrange(mc) == 0:
                                tk = dk
                                mi = (uy, ux, di)

                if mi == -1:
                    break
                kk.append(mi)
                my, mx, mc = mi
                ty, tx, tc = mi
                A[ty][tx] = USE

            ksa = []
            for ki in kk:
                my, mx, mc = ki
                # pe(ki)
                for i in range(1, N):
                    uy = (my + dd[mc][0] * i) % N
                    ux = (mx + dd[mc][1] * i) % N
                    if A[uy][ux] != EMPTY:
                        break
                    di = mc ^ 2
                    NK.add((uy, ux, di))
                    # pe("add {} {} {}".format(uy,ux,di))
                K[(my, mx)] = mc
                ksa.append((ki[0], ki[1]))
            kd = search(ksa, 2)
            for k, v in kd.items():
                if v < D[k]:
                    D[k] = v

        kv = set()
        kv.add((gy, gx))
        for y, x, c in C:
            ff = True
            while (y, x) not in kv or ff:
                ff = False
                if A[y][x] == GOAL or A[y][x] == BLOCK:
                    break
                if (y, x) in K:
                    c = K[(y, x)]
                kv.add((y, x))
                for i in range(1, N):
                    uy = (y + dd[c][0] * i) % N
                    ux = (x + dd[c][1] * i) % N
                    if A[uy][ux] != EMPTY:
                        y, x = uy, ux
                        break
                    kv.add((uy, ux))

        TK = {}
        for k, v in K.items():
            if k in kv:
                TK[k] = v
        score = len(TK) * 10 - len(kv)
        for ci in CK:
            score += D[ci] * 100000
        # pe("{} {} {} {}".format(gt,1000 - score, len(K), len(kv)))
        # pe(sorted(kv))
        if score < MSC:
            MSC = score
            MK = TK
            mkv = kv

    gt = time.time() - starttime
    pe("{} {} {} {} {}".format(1000-MSC, len(MK), ttt, gt, tt))
    # pe(sorted(mkv))
    RK = [str(len(MK))]
    for yx, c in MK.items():
        y, x = yx
        RK.append("{} {} {}".format(y, x, ddc[c]))
    return JA(RK, "\n")


print(main())
