def reaction_occurs(el1, el2):
    return el1.lower() == el2.lower() and ((el1.isupper() and el2.islower()) or (el1.islower() and el2.isupper()))


def reduce_chain(chain):
    possible_chars = set(chain.lower())
    old_chain = chain
    while True:
        for c in possible_chars:
            chain = chain.replace(c.upper() + c, '').replace(c + c.upper(), '')
        if old_chain == chain:
            break
        old_chain = chain
    return chain


def find_shortest_chain_with_single_unit_type_removed(chain):
    possible_chars = set(chain.lower())
    chains_w_unit_type_removed = {c: reduce_chain(chain.replace(c, '').replace(c.upper(), '')) for c in possible_chars}
    shortest_len = len(min(chains_w_unit_type_removed.values(), key=lambda ch: len(ch)))
    return shortest_len


def solve_puzzle(input_path):
    with open(input_path) as f:
        content = f.read()
    res = find_shortest_chain_with_single_unit_type_removed(content)
    return res


if __name__ == '__main__':
    INPUT_PATH = 'input.txt'
    res = solve_puzzle(INPUT_PATH)
    print(res)
