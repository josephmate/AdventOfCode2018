import sys
import re
from functional import seq


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
    return GameSpec(m.group(1), m.group(2))

gameSpecs = (seq(sys.stdin)
                .map(lambda line: line.rstrip())
                .map(lambda line: gameSpecFromStr(line))
                .list()
           )

def solveGameSpec(gameSpec):
    print(gameSpec)


for gameSpec in gameSpecs:
    solveGameSpec(gameSpec)
