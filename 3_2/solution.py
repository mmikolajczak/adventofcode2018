from collections import defaultdict


INPUT_PATH = 'input.txt'


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


def find_not_overlapping_claim(claims, claimed_material_map):
    for claim in claims:
        id_, x, y, h, w = parse_claim(claim)
        try:
            for i in range(y, y + h):
                for j in range(x, x + w):
                    if claimed_material_map[(i, j)] != 1:
                        raise RuntimeError('Claim overlapping')
            return id_
        except RuntimeError:
            pass


def solution_3_1(input_path):
    with open(input_path) as f:
        content = f.read()
    claims = content.split('\n')
    claimed_material_map = prepare_claimed_material_map(claims)
    not_overlapping_id = find_not_overlapping_claim(claims, claimed_material_map)
    return not_overlapping_id


if __name__ == '__main__':
    res = solution_3_1(INPUT_PATH)
    print(res)
