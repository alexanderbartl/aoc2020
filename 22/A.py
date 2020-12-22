from collections import deque

with open('input.txt') as f:
    player1, player2 = f.read().strip().split('\n\n')

player1 = deque(int(x) for x in player1.split('\n')[1:])
player2 = deque(int(x) for x in player2.split('\n')[1:])


def end_game(cards):
    print(sum(card * (pos + 1) for pos, card in enumerate(list(cards)[::-1])))
    raise SystemExit


while True:
    card1 = player1.popleft()
    card2 = player2.popleft()
    if card1 > card2:
        player1.extend((card1, card2))
    else:
        player2.extend((card2, card1))

    if len(player1) == 0:
        end_game(player2)
    elif len(player2) == 0:
        end_game(player1)
