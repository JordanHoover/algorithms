#  Given an input of space separated nums on 2 lines,
#  like 3 3 2 and 1 2 3,
#  find which has more comparison 'points'
#  A = a0, a1, a2
#  B = b0, b1, b2   -> if b0 is greater than a0, then
#  b gets one point, etc

a = map(int, input().split())
b = map(int, input().split())

a_points = 0
b_points = 0

for a_val, b_val in zip(a, b):
    if a_val > b_val:
        a_points += 1
    elif b_val > a_val:
        b_points += 1
print(a_points, b_points)

