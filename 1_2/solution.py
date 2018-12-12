INPUT_PATH = 'input.txt'


def solution_1_1(input_path):
    with open(input_path) as f:
        content = f.read()
    sum_ = sum(int(line) for line in content.split('\n'))
    return sum_


if __name__ == '__main__':
    res = solution_1_1(INPUT_PATH)
    print(res)
