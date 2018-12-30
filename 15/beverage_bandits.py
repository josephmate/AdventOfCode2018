import collections

GOBLIN = "G"
ELF = "E"
EMPTY = "."
WALL = "#"

def parse(lines):
    world = []
    fighters = {}
    r = 0
    for line in lines:
        line = line.rstrip()
        c = 0
        row = []
        for char in list(line):
            if char == GOBLIN or char == ELF:
                worldChar = "."
                fighters[(r,c)] = (char, 200)
            else:
                worldChar = char
            row.append(worldChar)
            c += 1
        world.append(row)
        r += 1

    fightersSorted = collections.OrderedDict(sorted(fighters.items()))
    return (world, fightersSorted)

def printState(world, fighters):
    r = 0
    for row in world:
        c = 0
        hps = []
        for char in row:
            if (r,c) in fighters:
                print(fighters[(r,c)][0], end='')
                hps.append(fighters[(r,c)][1])
            else:
                print(char, end='')
            c += 1
        print(hps)
        r += 1

    fightersSorted = collections.OrderedDict(sorted(fighters.items()))
    return (world, fightersSorted)


def solvePart1(lines):
    (world, fighters) = parse(lines)
    printState(world, fighters)


with open('sample.txt') as sampleFile:
    solvePart1(sampleFile)

with open('input.txt') as sampleFile:
    solvePart1(sampleFile)
