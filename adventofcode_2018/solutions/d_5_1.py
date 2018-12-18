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


def solve_puzzle(input_path):
    with open(input_path) as f:
        content = f.read()
    reduced_chain = reduce_chain(content)
    res = len(reduced_chain)
    return res


if __name__ == '__main__':
    INPUT_PATH = 'input.txt'
    res = solve_puzzle(INPUT_PATH)
    print(res)
