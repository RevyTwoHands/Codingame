# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
x, y, tx, ty = [int(i) for i in input().split()]

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.
    direction = ''

    if y < ty:
        direction += 'N'
        ty -= 1
    elif y > ty:
        direction += 'S'
        ty += 1
    if x < tx:
        direction += 'W'
        tx -= 1
    elif x > tx:
        direction += 'E'
        tx += 1
    print(direction)


