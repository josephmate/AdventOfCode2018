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

    def move(self):
        return Star(Point(self.posn.x + self.velocity.x,
                          self.posn.y + self.velocity.y
                         ),
                    Point(self.velocity.x, self.velocity.y)
                   )

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x} {self.y})'

    def __repr__(self):
        return f'({self.x} {self.y})'

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

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

# count how many points are next to other points
def calcAdjacency(stars):
    points = set()
    for star in stars:
        points.add(star.posn)

    adjacency = 0
    # we iterate over points instead of stars because some stars might be ontop
    # of eachother and so we should reduce the adjacency count in that case
    for point in points: 
        if Point(point.x+1, point.y) in points: adjacency += 1
        if Point(point.x-1, point.y) in points: adjacency += 1
        if Point(point.x, point.y+1) in points: adjacency += 1
        if Point(point.x, point.y-1) in points: adjacency += 1
        if Point(point.x+1, point.y+1) in points: adjacency += 1
        if Point(point.x-1, point.y+1) in points: adjacency += 1
        if Point(point.x+1, point.y-1) in points: adjacency += 1
        if Point(point.x-1, point.y-1) in points: adjacency += 1

    return adjacency


def moveStars(stars):
    newStar = []
    for star in stars:
        newStar.append(star.move())
    return newStar

def printStars(stars):
    minX = min(seq(stars).map(lambda star: star.posn.x))
    maxX = max(seq(stars).map(lambda star: star.posn.x))
    minY = min(seq(stars).map(lambda star: star.posn.y))
    maxY = max(seq(stars).map(lambda star: star.posn.y))

    points = set()
    for star in stars:
        points.add(star.posn)
    
    for y in range (minY, maxY+1):
        for x in range (minX, maxX+1):
            if Point(x, y) in points:
                print('#', end='')
            else:
                print(' ', end='')
        print('\n', end='')



starIterator = stars
maxAdjacency = 0
for i in range(0, 15000):
    adjacency = calcAdjacency(starIterator)
    if adjacency > maxAdjacency:
        maxAdjacency = adjacency
        whenMaxAdjacency = i
    starIterator = moveStars(starIterator)
    

starIterator = stars
for i in range(0, whenMaxAdjacency+50):
    if i > whenMaxAdjacency - 50 and  i < whenMaxAdjacency + 50:
        printStars(starIterator)
        print(i)
        print(calcAdjacency(starIterator))
        print('==========================')
    starIterator = moveStars(starIterator)
