from typing import List, Tuple


def read_input(fn: str):
    with open(fn, "r") as f:
        instructions = list(map(lambda x: (x[0], int(x[1:])), f.read().splitlines()))
    return instructions


def manhattan_distance(instructions: List[Tuple[str, int]]) -> int:
    dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]  # ordered clockwise
    cur_dir = 0
    x_dir, y_dir = dirs[cur_dir]
    x, y = 0, 0

    for action, value in instructions:
        if action == "N":
            y += value
        elif action == "S":
            y -= value
        elif action == "E":
            x += value
        elif action == "W":
            x -= value
        elif action == "R":
            cur_dir = (cur_dir + value // 90) % 4
            x_dir, y_dir = dirs[cur_dir]
        elif action == "L":
            cur_dir = (cur_dir - value // 90) % 4
            x_dir, y_dir = dirs[cur_dir]
        elif action == "F":
            x += value * x_dir
            y += value * y_dir

    return abs(x) + abs(y)


def manhattan_distance_waypoint(instructions: List[Tuple[str, int]]) -> int:
    rotate = {
        90: lambda x, y: (-y, x),
        180: lambda x, y: (-x, -y),
        270: lambda x, y: (y, -x),
    }

    x, y = 0, 0
    w_x, w_y = 10, 1  # waypoint relative coordinates

    for action, value in instructions:
        if action == "N":
            w_y += value
        elif action == "S":
            w_y -= value
        elif action == "E":
            w_x += value
        elif action == "W":
            w_x -= value
        elif action == "R":
            w_x, w_y = rotate[360 - value](w_x, w_y)
        elif action == "L":
            w_x, w_y = rotate[value](w_x, w_y)
        elif action == "F":
            x += value * w_x
            y += value * w_y

    return abs(x) + abs(y)


instructions = read_input("day 12/in")
print(manhattan_distance(instructions))
print(manhattan_distance_waypoint(instructions))

assert manhattan_distance(read_input("day 12/sample")) == 25
assert manhattan_distance_waypoint(read_input("day 12/sample")) == 286
assert set(val for act, val in instructions if act in "LR") == set([90, 180, 270])
