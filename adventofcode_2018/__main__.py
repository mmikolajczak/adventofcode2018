import os.path as osp
import re
import importlib
import time
from statistics import mean, stdev
import click


def timeit(func, *args):
    times = []
    for _ in range(10):
        t_start = time.time()
        res = func(*args)
        times.append(time.time() - t_start)
    return {'answer': res,
            'nb_runs': 10,
            'mean': mean(times),
            'std': stdev(times),
            'best': min(times),
            'worst': max(times)}


def print_stats(stats):
    print('In total, {} function calls were run.'.format(stats['nb_runs']))
    print('Average execution time for call is: {0:.4f} +/- {0:.4f}s'.format(stats['mean'], stats['std']))
    print('Best time is: {0:.4f}s'.format(stats['best']))
    print('Worst time is: {0:.4f}s'.format(stats['worst']))


@click.command()
@click.argument('puzzle')
@click.option('--input_path', default=None, help='Path to file with puzzle input.')
@click.option('--stats', type=bool, default=True, help='Whether or not show statistics of execution speed.')
def cli(puzzle, input_path, stats):
    m = re.match(r'^(\d+)_([12])$', puzzle)
    if m is None:
        print('Puzzle identifiers should be passed in {day}_{part} format, e.g. 3_1')
        exit(-1)
    day, part = m.group(1), m.group(2)
    solution_module = importlib.import_module('solutions.d_{}_{}'.format(day, part))
    if input_path is None:
        print('Using default input for puzzle...')
        input_path = osp.join(osp.abspath(__file__), '..', '..', 'inputs', 'd{}.txt'.format(day))
    if not osp.exists(input_path):
        print('File with input do not exists!')
        exit(-1)
    if stats:
        stats = timeit(solution_module.solve_puzzle, input_path)  # not ideal - lambda adds some overhead
        print_stats(stats)
        p_ans = stats['answer']
    else:
        p_ans = solution_module.solve_puzzle(input_path)
    print('Puzzle answer is:', p_ans)


if __name__ == '__main__':
    cli()
