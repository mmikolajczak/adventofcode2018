import re
from datetime import datetime
from enum import Enum
from collections import defaultdict
from statistics import mode


class EventType(Enum):
    BEGINS_SHIFT = 'BEGINS_SHIFT'
    FALLS_ASLEEP = 'FALLS_ASLEEP'
    WAKES_UP = 'WAKES_UP'


def extract_datetime_from_line(line):
    return datetime.strptime(line.split('] ')[0].lstrip('['), '%Y-%m-%d %H:%M')


def extract_event_from_line(line):
    event_txt = line.split('] ')[1]
    if event_txt == 'falls asleep':
        return EventType.FALLS_ASLEEP
    elif event_txt == 'wakes up':
        return EventType.WAKES_UP
    elif event_txt.startswith('Guard'):
        return EventType.BEGINS_SHIFT
    else:
        raise RuntimeError('Error during event extraction')


def try_extract_id_from_line(line):
    try:
        id_ = int(re.search(r'Guard #(\d+) begins shift', line.split('] ')[1]).group(1))
        return id_
    except Exception:
        return -1


def load_and_order_shifts_data(input_path):
    with open(input_path) as f:
        content = f.read()
    ordered = sorted(content.split('\n'), key=extract_datetime_from_line)
    return ordered


def sleep_interval_to_minutes(start_dt, end_dt):
    interval_minutes = [start_dt.minute + i for i in range(end_dt.minute - start_dt.minute)]  # assuming all times in hour after midnight
    return interval_minutes


def collect_guards_sleep_time(shifts_data):
    guards_sleep = defaultdict(list)
    i = 0
    while i < len(shifts_data):
        cur_event = extract_event_from_line(shifts_data[i])
        if cur_event == EventType.BEGINS_SHIFT:
            cur_id_ = try_extract_id_from_line(shifts_data[i])
            i += 1
        else:
            guards_sleep[cur_id_].extend(sleep_interval_to_minutes(extract_datetime_from_line(shifts_data[i]),
                                                                   extract_datetime_from_line(shifts_data[i + 1])))
            i += 2
    return guards_sleep


def solve_puzzle(input_path):
    shifts_data = load_and_order_shifts_data(input_path)
    guards_sleep_minutes = collect_guards_sleep_time(shifts_data)
    heaviest_sleeper_id = max(guards_sleep_minutes, key=lambda k: len(guards_sleep_minutes.get(k)))
    sleep_minutes_mode = mode(guards_sleep_minutes[heaviest_sleeper_id])
    res = heaviest_sleeper_id * sleep_minutes_mode
    return res


if __name__ == '__main__':
    INPUT_PATH = 'input.txt'
    res = solve_puzzle(INPUT_PATH)
    print(res)
