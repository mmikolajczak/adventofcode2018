from collections import defaultdict


def parse_data(f_content):
    possible_states = set()
    requirements = defaultdict(list)
    for line in f_content.split('\n'):
        req, step = line[5], line[-12]
        requirements[step].append(req)
        possible_states.add(req)
        possible_states.add(step)
    return possible_states, requirements


def solve_puzzle(input_path):
    with open(input_path) as f:
        content = f.read()
    possible_states, requirements = parse_data(content)
    order = []
    while len(order) != len(possible_states):
        might_be_done = sorted([st for st in possible_states if (st not in order) and (st not in requirements)])
        cur_step = might_be_done[0]
        order.append(cur_step)
        for st in requirements:
            if cur_step in requirements[st]:
                requirements[st].remove(cur_step)
        requirements = {k: v for k, v in requirements.items() if len(v) != 0}
    return ''.join(order)


if __name__ == '__main__':
    INPUT_PATH = 'input.txt'
    res = solve_puzzle(INPUT_PATH)
    print(res)
