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
    #print(gameSpec)

    scores = {}
    dq = deque()
    dq.append(0)
    #print(dq)
    for i in range(1, gameSpec.lastMarble + 1):
        playerId = (i-1) % gameSpec.players
        # However, if the marble that is about to be placed has a number which
        # is a multiple of 23, something entirely different happens. First, the
        # current player keeps the marble they would have placed, adding it to
        # their score. In addition, the marble 7 marbles counter-clockwise from
        # the current marble is removed from the circle and also added to the
        # current player's score. The marble located immediately clockwise of
        # the marble that was removed becomes the new current marble.
        if i % 23 == 0:

            if playerId in scores:
                scores[playerId] += i
            else:
                scores[playerId] = i

            dq.rotate(7)
            removed = dq.pop()
            scores[playerId] += removed
            dq.rotate(-1)

        # Then, each Elf takes a turn placing the lowest-numbered remaining
        # marble into the circle between the marbles that are 1 and 2 marbles
        # clockwise of the current marble. (When the circle is large enough,
        # this means that there is one marble between the marble that was just
        # placed and the current marble.) The marble that was just placed then
        # becomes the current marble.
        else:
            dq.rotate(-1)
            dq.append(i)
        #print(f'{playerId}: {dq}')

    
    bestPlayer = max(scores, key=lambda playerId: scores[playerId])
    print(f'{bestPlayer}: {scores[bestPlayer]}')


for gameSpec in gameSpecs:
    solveGameSpec(gameSpec)
