import sys
import re
from functional import seq
from collections import deque


class GameSpec:
    def __init__(self, players, lastMarble):
        self.players = players
        self.lastMarble = lastMarble

    def __str__(self):
        return f'{self.players} {self.lastMarble}'

    def __repr__(self):
        return f'{self.players} {self.lastMarble}'

gameSpecRegex = re.compile(r'(\d+) players; last marble is worth (\d+) points')
def gameSpecFromStr(gameSpecStr):
    m = gameSpecRegex.match(gameSpecStr)
    return GameSpec(int(m.group(1)), int(m.group(2)))

gameSpecs = (seq(sys.stdin)
                .map(lambda line: line.rstrip())
                .map(lambda line: gameSpecFromStr(line))
                .list()
           )

def solveGameSpec(gameSpec):
    print(gameSpec)
    dq = deque()
    dq.append(0)
    print(dq)
    for i in range(1, gameSpec.lastMarble + 1):
        # Then, each Elf takes a turn placing the lowest-numbered remaining
        # marble into the circle between the marbles that are 1 and 2 marbles
        # clockwise of the current marble. (When the circle is large enough,
        # this means that there is one marble between the marble that was just
        # placed and the current marble.) The marble that was just placed then
        # becomes the current marble.
        dq.rotate(-1)
        dq.append(i)
        print(dq)
        



solveGameSpec(gameSpecs[0])
