from collections import defaultdict


INPUT_PATH = 'input.txt'
DISTANCE_THRESH = 10000


def manhattan_distance(vec1, vec2):
    assert len(vec1) and len(vec1) == len(vec2)
    return sum(abs(el_v1 - el_v2) for el_v1, el_v2 in zip(vec1, vec2))


def count_pts_within_dist_thresh(cords, dist_thresh):
    cords_xs = tuple(pt[0] for pt in cords)
    cords_ys = tuple(pt[1] for pt in cords)
    min_x, max_x = min(cords_xs), max(cords_xs)
    min_y, max_y = min(cords_ys), max(cords_ys)

    cnt = 0
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if sum(manhattan_distance((x, y), cord) for cord in cords) < dist_thresh:
                cnt += 1
    return cnt


def solution_6_2(input_path):
    with open(input_path) as f:
        content = f.read()
    # cords = [(int(x), int(y)) for line in content.split('\n') for (x, y) in line.split(', ')] # ?
    cords = []
    for line in content.split('\n'):
        x, y = line.split(', ')
        cords.append((int(x), int(y)))
    # method goes as follows:
    # - for each point in grid, calculate the closest cords
    # - for future processing, exclude cords that are closest to any point of grid edges (infinite)
    # - calculate area for remaining cords
    # - find maximum
    res = count_pts_within_dist_thresh(cords, DISTANCE_THRESH)
    return res


if __name__ == '__main__':
    res = solution_6_2(INPUT_PATH)
    print(res)
