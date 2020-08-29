# ALDS1_2_D.py

# def insertsort(A, n, g):
#     global cnt
#     for i in range(g, n):
#         v = A[i]
#         j = i-g
#         while j >= 0 and A[j] > v:
#             A[j+g], A[j] = A[j], A[j+g]
#             j = j-g
#             cnt += 1


# n = int(input())
# A = [int(input()) for i in range(n)]
# cnt = 0

# G = [1]


# def G_choice(n):
#     for i in range(1, n):
#         point = 3*G[i-1]+1
#         if point >= n:
#             break
#         else:
#             G.append(point)


# G_choice(n)

# m = len(G)
# G.reverse()

# for i in range(m):
#     insertsort(A, n, G[i])

# print()
# print(m)
# print(*G)
# print(cnt)
# print(*A, sep="\n")
