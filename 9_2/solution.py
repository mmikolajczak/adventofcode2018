import re


INPUT_PATH = 'input.txt'


def is_special_marble(marble):
    return marble % 23 == 0


def parse_input(f_content):
    match = re.search(r'(\d+) .* (\d+) points', f_content)
    nb_players = int(match.group(1))
    last_marble = int(match.group(2))
    return nb_players, last_marble


def calc_rm_marble_idx(marbles_circle, cur_marble):
    pos = marbles_circle.index(cur_marble) - 7
    if pos < 0:
        pos += len(marbles_circle)
    return pos


def calc_added_marble_idx(marbles_circle, cur_marble):
    return (marbles_circle.index(cur_marble) + 2) % len(marbles_circle)


def solution_9_2(input_path):
    with open(input_path) as f:
        content = f.read()
    nb_players, last_marble = parse_input(content)
    players_pts = [0 for _ in range(nb_players)]

    nb_marbles_placed = 1
    cur_marble = 0
    cur_player = 0
    marbles_circle = [0]

    while nb_marbles_placed < last_marble:
        if is_special_marble(nb_marbles_placed):
            players_pts[cur_player] += nb_marbles_placed
            marble_to_rm_pos = calc_rm_marble_idx(marbles_circle, cur_marble)
            cur_marble = marbles_circle[marble_to_rm_pos + 1 if marble_to_rm_pos + 1 < len(marbles_circle) else 0]
            players_pts[cur_player] += marbles_circle[marble_to_rm_pos]
            del marbles_circle[marble_to_rm_pos]
        else:
            new_marble_pos = calc_added_marble_idx(marbles_circle, cur_marble)
            marbles_circle.insert(new_marble_pos, nb_marbles_placed)
            cur_marble = nb_marbles_placed
        nb_marbles_placed += 1
        cur_player = (cur_player + 1) % nb_players
    return max(players_pts)


# Note: just input is changed, runs too slow - will try to come up with something better
# (probably manipulating standard Python lists really slows it down)
if __name__ == '__main__':
    res = solution_9_2(INPUT_PATH)
    print(res)
