from collections import deque

with open('input.txt') as f:
    deck1, deck2 = f.read().strip().split('\n\n')

deck1 = deque(int(x) for x in deck1.split('\n')[1:])
deck2 = deque(int(x) for x in deck2.split('\n')[1:])


def final_score(cards):
    return sum(card * (pos + 1) for pos, card in enumerate(list(cards)[::-1]))


def stringify(cards1, cards2):
    return ','.join(map(str, cards1)) + ':' + ','.join(map(str, cards2))


def play_game(player1, player2, recursive=True):
    hist = set()
    while True:
        if stringify(player1, player2) in hist:
            return 1, None
        hist.add(stringify(player1, player2))

        card1 = player1.popleft()
        card2 = player2.popleft()
        if recursive and card1 <= len(player1) and card2 <= len(player2):
            winner, _ = play_game(deque(list(player1)[:card1]), deque(list(player2)[:card2]))
        else:
            winner = 1 if card1 > card2 else 2

        if winner == 1:
            player1.extend((card1, card2))
        elif winner == 2:
            player2.extend((card2, card1))

        if len(player1) == 0:
            return 2, final_score(player2)
        elif len(player2) == 0:
            return 1, final_score(player1)


print(play_game(deck1.copy(), deck2.copy(), False))
print(play_game(deck1, deck2))
