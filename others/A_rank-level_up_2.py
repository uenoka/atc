# A_rank-level_up_2.py
x, y, n = map(int, input().split())
current = "N"
start = (x, y)
dir = {"N": {"L": "W", "R": "E"},
       "S": {"L": "E", "R": "W"},
       "W": {"L": "S", "R": "N"},
       "E": {"L": "N", "R": "S"},
       }

mov = {"N": (0, -1),
       "S": (0, 1),
       "W": (-1, 0),
       "E": (1, 0)}

for i in range(n):
    next_dir = input()
    current = dir[current][next_dir]
    start = (start[0] + mov[current][0], start[1] + mov[current][1])
    print(*start)
