import os


def solution():
    packages = load_data()

    total =0

    for i in range(len(packages)):
        l = int(packages[i][0])
        w = int(packages[i][1])
        h = int(packages[i][2])
        sides = [l*w, w*h, h*l]
        sides.sort()
        total += 2*l*w + 2*w*h + 2*h*l + sides[0]

    return total


def load_data():
    values = []
    with open(os.path.dirname(os.path.realpath(__file__)) + '/input.txt', 'r') as file:
        for line in file:
            package=line.strip().split('x')
            values.append(package)
    return values


print("Solution: " + str(solution()))
