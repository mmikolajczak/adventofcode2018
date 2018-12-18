def solve_puzzle(input_path):
    with open(input_path) as f:
        content = f.read()
    current_freq = 0
    frequencies_seen = {current_freq}
    while True:
        for line in content.split('\n'):
            current_freq += int(line)
            if current_freq in frequencies_seen:
                return current_freq
            else:
                frequencies_seen.add(current_freq)


if __name__ == '__main__':
    INPUT_PATH = 'input.txt'
    res = solve_puzzle(INPUT_PATH)
    print(res)
