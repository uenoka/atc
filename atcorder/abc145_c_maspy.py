# abc145_c_maspy.py
'''
maspy さんの提出（学習用）
'''

H,W = map(int,input().split())
S = [input() for _ in range(H)]
answer = [[0 if cell == '.' else '#' for cell in row] for row in S]
print(answer,S)

import itertools
for i in range(H):
  for j in range(W):
    if S[i][j] != '#':
      continue
    for dx,dy in itertools.product([-1,0,1],repeat=2):
      print(dx,dy)
      x = i+dx
      y = j+dy
      if x < 0 or x >= H:
        continue
      if y < 0 or y >= W:
        continue
      if S[x][y] == '#':
        continue
      answer[x][y] += 1

  
for row in answer:
  print(*row,sep='')
