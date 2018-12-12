from collections import Counter


INPUT_PATH = 'input.txt'


def solution_2_1(input_path):
    with open(input_path) as f:
        content = f.read()
    nb_pairs = 0
    nb_triplets = 0
    for id_ in content.split('\n'):
        letters_cnt = Counter(id_.strip())
        unique_counts = set(letters_cnt.values())
        nb_pairs += int(2 in unique_counts)
        nb_triplets += int(3 in unique_counts)
    checksum = nb_pairs * nb_triplets
    return checksum


if __name__ == '__main__':
    res = solution_2_1(INPUT_PATH)
    print(res)