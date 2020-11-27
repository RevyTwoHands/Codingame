import math

rounds = int(input())
cash = int(input())

for i in range(rounds):
    play = input().split()

    bet = math.ceil(0.25 * cash)  # The amount of money he bet

    if play[1] == 'PLAIN':
        if play[0] == play[2]:  # If he got his bet correct
            cash += 35 * bet
        else:
            cash -= bet

    else:
        x = int(play[0])
        if play[1] == 'ODD' and x % 2 == 1 or play[1] == 'EVEN' and x % 2 == 0 and x != 0:
            cash += bet
        else:
            cash -= bet
print(cash)

# OR
# win = {
#     'EVEN': lambda x: 1 if int(x) != 0 and int(x) % 2 == 0 else -1,
#     'ODD': lambda x: 1 if int(x) % 2 == 1 else -1,
#     'PLAIN': lambda x, y: 35 if x == y else -1
# }
#
#
# def game(ball, call, number=""):
#     return win[call](ball, number) if number else win[call](ball);
#
#
# rounds = int(input())
# cash = int(input())
# for i in range(rounds):
#     bet = math.ceil(cash / 4)
#     play = input().split()
#     cash += bet * game(*play)
#
# print(cash)
