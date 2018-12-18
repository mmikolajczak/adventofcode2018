from collections import defaultdict


def parse_claim(claim_raw):
    id_, body = claim_raw.split(' @ ')
    coords, sizes = body.split(': ')
    x, y = coords.split(',')
    w, h = sizes.split('x')
    y, x, w, h = int(y), int(x), int(w), int(h)
    id_ = id_[1:]
    return id_, x, y, h, w


def prepare_claimed_material_map(claims):
    claimed_material_map = defaultdict(int)
    for claim in claims:
        _, x, y, h, w = parse_claim(claim)
        for i in range(y, y + h):
            for j in range(x, x + w):
                claimed_material_map[(i, j)] += 1
    return claimed_material_map


def solve_puzzle(input_path):
    with open(input_path) as f:
        content = f.read()
    claims = content.split('\n')
    claimed_material_map = prepare_claimed_material_map(claims)
    nb_overlaping = sum(1 if v > 1 else 0 for v in claimed_material_map.values())
    return nb_overlaping


if __name__ == '__main__':
    INPUT_PATH = 'input.txt'
    res = solve_puzzle(INPUT_PATH)
    print(res)
