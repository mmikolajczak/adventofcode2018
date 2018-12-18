import re
from collections import  deque


def is_special_marble(marble):
    return marble % 23 == 0


def parse_input(f_content):
    match = re.search(r'(\d+) .* (\d+) points', f_content)
    nb_players = int(match.group(1))
    last_marble = int(match.group(2))
    return nb_players, last_marble


def solve_puzzle(input_path):
    with open(input_path) as f:
        content = f.read()
    nb_players, last_marble = parse_input(content)
    players_pts = [0 for _ in range(nb_players)]

    nb_marbles_placed = 1
    cur_player = 0
    marbles_circle = deque([0])

    while nb_marbles_placed < last_marble:
        if is_special_marble(nb_marbles_placed):
            marbles_circle.rotate(7)
            players_pts[cur_player] += nb_marbles_placed + marbles_circle.pop()
            marbles_circle.rotate(-1)  # rollback required after pop
        else:
            marbles_circle.rotate(-1)
            marbles_circle.append(nb_marbles_placed)
        nb_marbles_placed += 1
        cur_player = (cur_player + 1) % nb_players
    return max(players_pts)


if __name__ == '__main__':
    INPUT_PATH = 'input.txt'
    res = solve_puzzle(INPUT_PATH)
    print(res)
