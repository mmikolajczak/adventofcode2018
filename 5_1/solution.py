INPUT_PATH = 'input.txt'


def reaction_occurs(el1, el2):
    return el1.lower() == el2.lower() and ((el1.isupper() and el2.islower()) or (el1.islower() and el2.isupper()))


def reduce_chain(chain):  # Note: probably can be done in (MUCH) more efficient way.
    while True:
        reduction_occurred = False
        for i in range(0, len(chain) - 1):
            if reaction_occurs(chain[i], chain[i + 1]):
                chain = chain[:i] + chain[i + 2:]
                reduction_occurred = True
                break
        if not reduction_occurred:
            break
    return chain


def solution_5_1(input_path):
    with open(input_path) as f:
        content = f.read()
    reduced_chain = reduce_chain(content)
    res = len(reduced_chain)
    return res


if __name__ == '__main__':
    res = solution_5_1(INPUT_PATH)
    print(res)
