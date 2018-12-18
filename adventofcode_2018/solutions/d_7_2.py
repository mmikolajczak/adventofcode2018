from collections import defaultdict


BASE_STEP_SECONDS = 60


def parse_data(f_content):
    possible_states = set()
    requirements = defaultdict(list)
    for line in f_content.split('\n'):
        req, step = line[5], line[-12]
        requirements[step].append(req)
        possible_states.add(req)
        possible_states.add(step)
    return possible_states, requirements


def step_to_required_seconds(step):
    return BASE_STEP_SECONDS + (ord(step) - ord('A') + 1)


def is_being_done_by_some_worker(step, workers):
    for worker in workers:
        if worker is not None and worker['step'] == step:
            return True
    return False


def get_steps_that_might_be_done(possible_steps, finished_steps, requirements, workers):
    might_be_done = sorted([st for st in possible_steps
                            if (st not in finished_steps) and (st not in requirements)
                            and not is_being_done_by_some_worker(st, workers)])
    return might_be_done


def assign_possible_jobs_to_workers(workers, might_be_done):
    for i in range(len(workers)):
        if workers[i] is None and might_be_done:
            step_to_do = might_be_done[0]
            workers[i] = {'step': step_to_do,
                          'sec_to_complete': step_to_required_seconds(step_to_do)}
            might_be_done = might_be_done[1:]


def update_workers_jobs_progress(workers, requirements, finished_steps):
    for i in range(len(workers)):
        if workers[i] is not None:
            workers[i]['sec_to_complete'] -= 1
            if workers[i]['sec_to_complete'] == 0:
                cur_step = workers[i]['step']
                workers[i] = None
                finished_steps.append(cur_step)
                for st in requirements:
                    if cur_step in requirements[st]:
                        requirements[st].remove(cur_step)
                requirements = {k: v for k, v in requirements.items() if len(v) != 0}
    return requirements  # requirements returned instead of modified inplace like others - just easier way


def solve_puzzle(input_path):
    with open(input_path) as f:
        content = f.read()
    possible_steps, requirements = parse_data(content)

    workers = [None for _ in range(4)]
    finished_steps = []
    total_time = 0
    time_interval = 1

    while len(finished_steps) != len(possible_steps):
        might_be_done = get_steps_that_might_be_done(possible_steps, finished_steps, requirements, workers)
        assign_possible_jobs_to_workers(workers, might_be_done)
        requirements = update_workers_jobs_progress(workers, requirements, finished_steps)
        total_time += time_interval
    return total_time


if __name__ == '__main__':
    INPUT_PATH = 'input.txt'
    res = solve_puzzle(INPUT_PATH)
    print(res)
