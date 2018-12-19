from copy import deepcopy
from itertools import accumulate


GRID_SIZE = (300, 300)


def calc_power_level(x, y, grid_sn):
    rack_id = x + 10
    power_level = rack_id * y
    power_level += grid_sn
    power_level *= rack_id
    hundreds = 0 if power_level < 100 else int(str(power_level)[-3])
    power_level = hundreds - 5
    return power_level


def grid_cumsum(grid):
    return list(zip(*
                (accumulate(row) for row in zip(*
                (accumulate(row) for row in grid)))))


def solve_puzzle(input_path):
    with open(input_path) as f:
        content = f.read()
    grid_serial_number = int(content)
    pl_grid = [[calc_power_level(x + 1, y + 1, grid_serial_number)
               for x in range(GRID_SIZE[1])]
               for y in range(GRID_SIZE[0])]

    pl_cumsum_grid = grid_cumsum(pl_grid)
    squares_pl_sums = {}

    for side in range(1, 301):
        for y in range(side, 300):
            for x in range(side, 300):
                squares_pl_sums[(x - side + 2, y - side + 2, side)] = (pl_cumsum_grid[y][x]
                                                                       - pl_cumsum_grid[y - side][x]
                                                                       - pl_cumsum_grid[y][x - side]
                                                                       + pl_cumsum_grid[y - side][x - side])
    return max(squares_pl_sums, key=squares_pl_sums.get)


if __name__ == '__main__':
    INPUT_PATH = 'input.txt'
    res = solve_puzzle(INPUT_PATH)
    print(res)

