import sys
import math

nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators = [int(i) for
                                                                                                             i in
                                                                                                             input().split()]
elevators = {}  # elevator_pos: position of the elevator on its floor
for i in range(nb_elevators):
    e_floor, e_pos = [int(j) for j in input().split()]
    elevators[e_floor] = e_pos

while True:
    clone_floor, clone_pos, direction = input().split()
    clone_floor, clone_pos = map(int, (clone_floor, clone_pos))
    answer = 'WAIT'

    if clone_floor == exit_floor:
        target = exit_pos
    elif clone_floor in elevators:
        target = elevators[clone_floor]

    if direction == 'RIGHT' and clone_pos > target or direction == 'LEFT' and clone_pos < target:
        answer = 'BLOCK'

    print(answer)