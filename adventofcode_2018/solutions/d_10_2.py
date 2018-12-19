import re


def manhattan_distance(vec1, vec2):
    assert len(vec1) and len(vec1) == len(vec2)
    return sum(abs(el_v1 - el_v2) for el_v1, el_v2 in zip(vec1, vec2))


def update_point_pos(point):
    return {'x': point['x'] + point['vel_x'],
            'y': point['y'] + point['vel_y'],
            'vel_x': point['vel_x'],
            'vel_y': point['vel_y']}


def parse_input(f_content):
    points = []
    for line in f_content.split('\n'):
        match = re.search(r'position=<([ |-]\d+), ([ |-]\d+)> velocity=<([ |-]\d+), ([ |-]\d+)>', line)
        x, y, vel_x, vel_y = int(match.group(1)), int(match.group(2)), int(match.group(3)), int(match.group(4))
        points.append({'x': x,
                       'y': y,
                       'vel_x': vel_x,
                       'vel_y': vel_y})
    return points


def are_all_stars_close(points):
    for i in range(len(points)):
        if not any(manhattan_distance([points[i]['x'], points[i]['y']], [points[j]['x'], points[j]['y']]) <= 2
                   for j in range(len(points)) if j != i):
            return False
    return True


def draw_constellation(points):
    min_x, max_x = min(points, key=lambda pt: pt['x'])['x'], max(points, key=lambda pt: pt['x'])['x']
    min_y, max_y = min(points, key=lambda pt: pt['y'])['y'], max(points, key=lambda pt: pt['y'])['y']

    constellation = [['.' for _ in range(max_x - min_x + 1)] for _ in range(max_y - min_y + 1)]

    for pt in points:
        constellation[pt['y'] - min_y][pt['x'] - min_x] = '#'

    return '\n'.join([''.join(row) for row in constellation])


def solve_puzzle(input_path):
    with open(input_path) as f:
        content = f.read()
    points = parse_input(content)

    total_seconds = 0
    while True:
        points = [update_point_pos(pt) for pt in points]
        total_seconds += 1
        if are_all_stars_close(points):
            return total_seconds


if __name__ == '__main__':
    INPUT_PATH = 'input.txt'
    res = solve_puzzle(INPUT_PATH)
    print(res)
