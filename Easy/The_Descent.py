# game loop
while True:
    mountain_heights = [int(input()) for i in range(8)]
    print(mountain_heights.index(max(mountain_heights)))
