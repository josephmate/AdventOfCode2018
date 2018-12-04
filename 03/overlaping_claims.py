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
        innerMap[row].add(claim.claimId)
    else:
        innerMap[row] = {claim.claimId}

def appendClaimToClaimMap(claimMap, claim):
    for c in range(0, claim.colLen):
        for r in range(0, claim.rowLen):
            appendPositionToClaimMap(claimMap, claim, claim.col + c, claim.row + r)

claims = (seq(sys.stdin)
                .map(lambda line: line.rstrip())  # remove the newline that readlines keeps
                .filter(lambda line: claimRegex.match(line))  # remove the newline that readlines keeps
                .map(lambda line: claimFromEncodedStr(line))     
             )

claimMap = {}
for claim in claims:
    appendClaimToClaimMap(claimMap, claim)

numContestedClaims = 0
for c in claimMap:
    innerMap = claimMap[c]
    for r in innerMap:
        if len(innerMap[r]) >= 2:
            numContestedClaims += 1

print(f'number of inches with two or more claims: {numContestedClaims}')



