import sys
import math

def calcDist(x1, x2, y1, y2):
    return (x2 - x1)**2 + (y2 - y1)**2



n = int(input())
for i in range(n):
    p=rh=re= False
    ans = "quadrilateral"
    inputs = input().split()
    print(inputs, file=sys.stderr)
    a = inputs[0]
    x_a = int(inputs[1])
    y_a = int(inputs[2])
    b = inputs[3]
    x_b = int(inputs[4])
    y_b = int(inputs[5])
    c = inputs[6]
    x_c = int(inputs[7])
    y_c = int(inputs[8])
    d = inputs[9]
    x_d = int(inputs[10])
    y_d = int(inputs[11])

    side_AB = calcDist(x_a, x_b, y_a, y_b)
    side_BC = calcDist(x_b, x_c, y_b, y_c)
    side_CD = calcDist(x_c, x_d, y_c, y_d)
    side_DA = calcDist(x_d, x_a, y_d, y_a)

    diag_AC = calcDist(x_c, x_a, y_c, y_a)
    diag_BD = calcDist(x_d, x_b, y_d, y_b)


    if side_AB  == side_CD  and side_BC == side_DA:
        p=True
        if diag_AC == diag_BD:
            re = True
        if side_AB == side_BC:
            rh = True

    if re and rh:
        ans = "square"
    elif rh and not re:
        ans = "rhombus"
    elif re and not rh:
        ans = "rectangle"
    elif p:
        ans = "parallelogram"
    print("{} is a {}.".format(a+b+c+d, ans))