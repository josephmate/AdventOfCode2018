import sys
import re
from functional import seq
from collections import deque

class Star:
    def __init__(self, posn, velocity):
        self.posn = posn
        self.velocity = velocity

    def __str__(self):
        return f'[{self.posn} {self.velocity}]'

    def __repr__(self):
        return f'[{self.posn} {self.velocity}]'

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x} {self.y})'

    def __repr__(self):
        return f'({self.x} {self.y})'

starRegex = re.compile(r'position=< *(-?\d+), *(-?\d+)> velocity=< *(-?\d+), *(-?\d+)>')
def starFromStr(starStr):
    m = starRegex.match(starStr)
    return Star(Point(int(m.group(1)), int(m.group(2))),
                Point(int(m.group(3)), int(m.group(4)))
               )
stars = []
lineNum = 1
for line in sys.stdin:
    line = line.rstrip()
    if starRegex.match(line):
        stars.append(starFromStr(line))
    else:
        print(f'ERROR {lineNum}: {line}')

print(stars)
print(len(stars))
