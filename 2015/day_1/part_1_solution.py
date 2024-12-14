import os


def solution():
    items = load_data()

    floor = 0
    for i in range(len(items)):
        if items[i] == '(':
            floor += 1
        elif items[i] == ')':
            floor -= 1

    return floor


def load_data():
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(script_path + '/input.txt', 'r') as file:
        line = file.readline().strip()
        return list(line)


print("Solution: " + str(solution()))
