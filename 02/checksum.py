import sys
from functional import seq

def hasNumOfOccurences( charCount, numOfOccurences ) :
    for key, value in charCount.items():
        if value == numOfOccurences:
            return True
    return False


def countLetters( listOfChars ):
    res = {}
    for c in listOfChars:
        if c in res:
            res[c] = res[c] + 1
        else:
            res[c] = 1
    return res

def positionalDiff( a, b ) :
    lenA = len(a)
    lenB = len(b)

    lenDiff = abs(lenA-lenB)
    maxLen = max(lenA, lenB)

    diffCount = 0
    for i in range(0, maxLen):
        if a[i] != b[i]:
            diffCount += 1
            

    return diffCount + lenDiff

lines = sys.stdin.readlines()
preProcessed = (seq(lines)
                .map(lambda line: line.rstrip())  # remove the newline that readlines keeps
                .map(lambda line: list(line))     # convert from string to list of characters
             )
charMapped = preProcessed.map(lambda chars: countLetters(chars))

twoCount =  (charMapped
        .count(lambda charCount: hasNumOfOccurences(charCount, 2))
        )

threeCount =  (charMapped
        .count(lambda charCount: hasNumOfOccurences(charCount, 3))
        )

checkSum = twoCount * threeCount
print(f'checkSum: {checkSum}')

# unfortunately, I couldn't come up with a better way than comparing all possible pairs
# O(N^2)
# The problem does not benefit from sorting, because the difference could be anywhere
def findDiffersInOnePosition( listOfListOfChars ):
    for i in listOfListOfChars:
        for j in listOfListOfChars:
            if positionalDiff(i,j) == 1:
                return [i, j]

    # not found. specification of the problem says this shouldn't happen
    return None 

differsBy1 = findDiffersInOnePosition(preProcessed)
print( ''.join(differsBy1[0]) )
print( ''.join(differsBy1[1]) )


def getCommonChars( a, b ):
    res = []
    for i in range(0, len(a)):
        if a[i] == b[i]:
            res.append(a[i])
    return res

print(''.join(getCommonChars(differsBy1[0],differsBy1[1])))
