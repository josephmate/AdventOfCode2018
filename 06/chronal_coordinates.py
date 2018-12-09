import sys
import re
from functional import seq

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x, self.y}'

    def __repr__(self):
        return f'{self.x, self.y}'

    def manhattanDistance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def closest(self, points):
        closestDist = self.manhattanDistance(min(points, key=lambda other: self.manhattanDistance(other)))
        closestPoints = (seq(points)
                            .filter(lambda other: self.manhattanDistance(other) == closestDist)
                            .list()
                        )
        if len(closestPoints) == 1:
            return closestPoints[0]
        else:
            return None
        
points = (seq(sys.stdin)
                .map(lambda line: line.rstrip())  # remove the newline that readlines keeps
                .map(lambda line: line.split(','))  
                .map(lambda strArr: Point(int(strArr[0]), int(strArr[1].lstrip())))
                .list() # save to a list, because multiple iterations of sys.stdin is not possible
             )

maxX = max(points, key=lambda point: point.x).x
maxY = max(points, key=lambda point: point.y).y
print(maxX)
print(maxY)

closestPointGrid = []
for x in range(0, maxX + 2):
    yClosests = []
    for y in range(0, maxY + 2):
        yClosests.append( Point(x,y).closest(points) )
    closestPointGrid.append(yClosests)

infinitePoints = set()
for x in range(0, maxX + 2):
    infinitePoints.add(closestPointGrid[x][0])
    infinitePoints.add(closestPointGrid[x][maxY+1])
for y in range(0, maxY + 2):
    infinitePoints.add(closestPointGrid[0][y])
    infinitePoints.add(closestPointGrid[maxX+1][y])

areas = {}
for x in range(0, maxX + 2):
    for y in range(0, maxY + 2):
        if not closestPointGrid[x][y] in infinitePoints:
            if closestPointGrid[x][y] in areas:
                areas[closestPointGrid[x][y]] += 1
            else:
                areas[closestPointGrid[x][y]] = 1

print(areas)

maxAreaPoint = max(areas, key=lambda point: areas[point])

print(maxAreaPoint)
print(areas[maxAreaPoint])
