GRID_SIZE = (300, 300)


def calc_power_level(x, y, grid_sn):
    rack_id = x + 10
    power_level = rack_id * y
    power_level += grid_sn
    power_level *= rack_id
    hundreds = 0 if power_level < 100 else int(str(power_level)[-3])
    power_level = hundreds - 5
    return power_level


def grid_square_sum(grid, top_x, top_y):
    selected_rows = grid[top_y: top_y + 3]
    return sum(sum(row[top_x: top_x + 3]) for row in selected_rows)


def solve_puzzle(input_path):
    with open(input_path) as f:
        content = f.read()
    grid_serial_number = int(content)
    pl_grid = [[calc_power_level(x + 1, y + 1, grid_serial_number) for x in range(GRID_SIZE[1])]
               for y in range(GRID_SIZE[0])]
    squares_pl_sums = {(x + 1, y + 1): grid_square_sum(pl_grid, x, y)
                       for y in range(GRID_SIZE[0]) for x in range(GRID_SIZE[1])}
    return max(squares_pl_sums, key=squares_pl_sums.get)


if __name__ == '__main__':
    INPUT_PATH = 'input.txt'
    res = solve_puzzle(INPUT_PATH)
    print(res)
