def chars_difference(str1, str2):
    assert len(str1) == len(str2)
    diff = 0
    for c1, c2 in zip(str1, str2):
        if c1 != c2:
            diff += 1
    return diff


def common_sequence(str1, str2):
    assert len(str1) == len(str2)
    res = ''.join([str1[i] for i in range(len(str1)) if str1[i] == str2[i]])
    return res


def solve_puzzle(input_path):
    with open(input_path) as f:
        content = f.read()
    ids = content.split('\n')
    for i in range(len(ids)):
        for j in range(i, len(ids)):
            if i == j:
                continue
            if chars_difference(ids[i], ids[j]) == 1:
                common_chars_str = common_sequence(ids[i], ids[j])
                return common_chars_str
    raise RuntimeError('Results not found')


if __name__ == '__main__':
    INPUT_PATH = 'input.txt'
    res = solve_puzzle(INPUT_PATH)
    print(res)
