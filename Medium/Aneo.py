import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

speed = int(input())
light_count = int(input())
lst = []
for i in range(light_count):
    lst.append(list(map(int, input().split())))

for j in range(speed, 0, -1):
    # Starting at the hihest speed
    # Converting km/h into m/s
    speed_ms = j / 3.6
    # Initializing my boolean
    is_ok = True

    for i in range(light_count):

        d = lst[i][0]
        duration = lst[i][1]
        # Je calcule la distance

        # Je calcule le temps que je vais mettre à la vitesse actuelle
        t = d / (j * 10 / 36)
        # Je regarde combien de fois le feu s'est éteint et allumé

        x = t / duration

        if j == 60: print(x, file=sys.stderr, flush=True)

        x = round(x, 3)
        if math.floor(x) % 2 != 0:
            # if int(x)%2 != 0 : # Le feu est au rouge, on passe à la vitesse inférieure
            is_ok = False
            break
        # Le feu est au vert, on passe au prochain

    if is_ok:
        print(j)
        break

