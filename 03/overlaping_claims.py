import sys
import re
from functional import seq




class Claim:
    def __init__(self, claimId, col, row, colLen, rowLen):
        self.claimId = claimId
        self.col = col
        self.row = row
        self.colLen = colLen
        self.rowLen = rowLen

    def toString(self):
        return f'#{self.claimId} @ {self.col},{self.row}: {self.colLen}x{self.rowLen}'


# 
claimRegex = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')
# ...........
# ...........
# ...#####...
# ...#####...
# ...#####...
# ...#####...
# ...........
# ...........
# ...........
def claimFromEncodedStr(strEncodedClaim):
    m = claimRegex.match(strEncodedClaim)
    return Claim(int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5)))
    
def appendPositionToClaimMap(claimMap, claim, col, row):

    if not col in claimMap:
        claimMap[col] = {}

    innerMap = claimMap[col]

    if row in innerMap:
        innerMap[row] = innerMap[row] + 1
    else:
        innerMap[row] = 1 

def appendClaimToClaimMap(claimMap, claim):
    for c in range(0, claim.colLen):
        for r in range(0, claim.rowLen):
            appendPositionToClaimMap(claimMap, claim, claim.col + c, claim.row + r)

claimMap = {}
lineNum = 1
for line in sys.stdin:
    line = line.rstrip()

    if claimRegex.match(line):
        claim = claimFromEncodedStr(line)
        appendClaimToClaimMap(claimMap, claim)

        
    else:
        print(f'{lineNum}: {line} does not match claim regex')

    lineNum += 1

numContestedClaims = 0
for c in claimMap:
    innerMap = claimMap[c]
    for r in innerMap:
        if innerMap[r] >= 2:
            numContestedClaims += 1

print(f'number of inches with two or more claims: {numContestedClaims}')

