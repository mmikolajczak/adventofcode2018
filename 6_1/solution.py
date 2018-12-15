from collections import defaultdict


INPUT_PATH = 'input.txt'


def flatten_one_level(nested):
    res = []
    for el in nested:
        res.extend(el)
    return res


def manhattan_distance(vec1, vec2):
    assert len(vec1) and len(vec1) == len(vec2)
    return sum(abs(el_v1 - el_v2) for el_v1, el_v2 in zip(vec1, vec2))


def cords_system_start_to_0_0(cords):
    cords_xs = tuple(pt[0] for pt in cords)
    cords_ys = tuple(pt[1] for pt in cords)
    min_x = min(cords_xs)
    min_y = min(cords_ys)
    return [(pt[0] - min_x, pt[1] - min_y) for pt in cords]


def construct_closest_grid(cords):
    cords_xs = tuple(pt[0] for pt in cords)
    cords_ys = tuple(pt[1] for pt in cords)
    min_x, max_x = min(cords_xs), max(cords_xs)
    min_y, max_y = min(cords_ys), max(cords_ys)
    grid = [[None for x in range(min_x, max_x + 1)]
            for y in range(min_y, max_y + 1)]

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            pt_to_cords_dist = tuple((cord, manhattan_distance(cord, (x, y))) for cord in cords)
            pt_to_cords_dist = sorted(pt_to_cords_dist, key=lambda el: el[1])
            min_dist = pt_to_cords_dist[0][1]
            grid[y][x] = []
            for pt, dist in pt_to_cords_dist:
                if dist == min_dist:
                    grid[y][x].append(pt)
                else:
                    break
    return grid


def filter_out_cords_closest_to_edges(closest_grid, cords):
    edge_points = closest_grid[0] + closest_grid[-1]
    for row in closest_grid[1: -1]:
        edge_points.append(row[0])
        edge_points.append(row[-1])
    edge_points = flatten_one_level(edge_points)
    filtered = [pt for pt in cords if pt not in edge_points]
    return filtered


def calculate_cords_area(closest_grid, cords):
    cords_area = defaultdict(int)
    for y in range(len(closest_grid)):
        for x in range(len(closest_grid[0])):
            if len(closest_grid[y][x]) == 1 and closest_grid[y][x][0] in cords:
                cords_area[closest_grid[y][x][0]] += 1
    return cords_area


def solution_6_1(input_path):
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
    cords = cords_system_start_to_0_0(cords)
    grid_pts_closest_cords = construct_closest_grid(cords)
    cords = filter_out_cords_closest_to_edges(grid_pts_closest_cords, cords)
    cords_area = calculate_cords_area(grid_pts_closest_cords, cords)
    res = max(cords_area.values())
    return res


if __name__ == '__main__':
    res = solution_6_1(INPUT_PATH)
    print(res)
