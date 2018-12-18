def solve_puzzle(input_path):
    with open(input_path) as f:
        content = f.read()
    sum_ = sum(int(line) for line in content.split('\n'))
    return sum_


if __name__ == '__main__':
    INPUT_PATH = 'input.txt'
    res = solve_puzzle(INPUT_PATH)
    print(res)
