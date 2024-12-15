import os


def solution():
    packages = load_data()

    total =0

    for i in range(len(packages)):
        widths = packages[i]
        widths.sort()
        length=(int(widths[0])*2)+(int(widths[1])*2)
        length+=int(widths[0])*int(widths[1])*int(widths[2])
        total += length


    return total


def load_data():
    values = []
    with open(os.path.dirname(os.path.realpath(__file__)) + '/input.txt', 'r') as file:
        for line in file:
            package=line.strip().split('x')
            # convert to ints
            for i in range(len(package)):
                package[i]=int(package[i])
            values.append(package)
    return values


print("Solution: " + str(solution()))
