# abc026_c.py
def calc_max():
    return 0


def calc_min():
    return 0


N = int(input())

B = [0]
B += [int(input()) for i in range(1, N)]

salary = [1] * N
counter = N
while counter >= 0:
    min_salary = calc_min()
    max_salary = calc_max()
    salary[counter] = min_salary+max_salary+1
    counter -= 1
