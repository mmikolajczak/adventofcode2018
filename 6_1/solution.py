import math
from collections import Counter


INPUT_PATH = 'input.txt'
GRID_PADDING = 100
_MULTIPLE_CLOSEST_PTS = 'multi_pts'


def flatten_one_level(nested):
    res = []
    for el in nested:
        res.extend(el)
    return res


def manhattan_distance(vec1, vec2):
    assert len(vec1) and len(vec1) == len(vec2)
    return sum(abs(el_v1 - el_v2) for el_v1, el_v2 in zip(vec1, vec2))


def construct_grid(cords, grid_padding=101):
    cords_xs = tuple(pt[0] for pt in cords)
    cords_ys = tuple(pt[1] for pt in cords)
    min_x, max_x = min(cords_xs), max(cords_xs)
    min_y, max_y = min(cords_ys), max(cords_ys)
    grid = [[None for x in range(min_x - grid_padding, max_x + grid_padding + 1)]
            for y in range(min_y - grid_padding, max_y + grid_padding + 1)]
    return grid


def find_closest_points(grid, cords):
    closest_pts_grid = grid.copy()
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            pt_to_cords_dist = tuple((cord, manhattan_distance(cord, (x, y))) for cord in cords)
            pt_to_cords_dist = sorted(pt_to_cords_dist, key=lambda el: el[1])
            closest_pts_grid[y][x] = (pt_to_cords_dist[0][0] if pt_to_cords_dist[0][1] != pt_to_cords_dist[1][1]
                                      else _MULTIPLE_CLOSEST_PTS)
    return closest_pts_grid


def count_up_closest(cords, grid_padding):
    grid_points = construct_grid(cords, grid_padding)
    closest_pts_grid = find_closest_points(grid_points, cords)
    closest_pts_counts = Counter(flatten_one_level(closest_pts_grid))
    del closest_pts_counts[_MULTIPLE_CLOSEST_PTS]
    return closest_pts_counts


def solution_6_1(input_path):
    with open(input_path) as f:
        content = f.read()
    # cords = [(int(x), int(y)) for line in content.split('\n') for (x, y) in line.split(', ')] # ?
    cords = []
    for line in content.split('\n'):
        x, y = line.split(', ')
        cords.append((int(x), int(y)))
    # assumption - closest points are counted for a grid with some padding, if for a grid
    # with padding greater (+1) than that count for particular coordinate is greater - it
    # is counted as infinity.
    coords_closest_pts_counts_grid_norm = count_up_closest(cords, GRID_PADDING)
    coords_closest_pts_counts_grid_ext = count_up_closest(cords, GRID_PADDING + 1)
    for key in coords_closest_pts_counts_grid_norm:
        if coords_closest_pts_counts_grid_norm[key] != coords_closest_pts_counts_grid_ext[key]:
            coords_closest_pts_counts_grid_norm[key] = math.inf
    res = max(v for v in coords_closest_pts_counts_grid_norm.values() if v != math.inf)
    return res


if __name__ == '__main__':
    res = solution_6_1(INPUT_PATH)
    print(res)
