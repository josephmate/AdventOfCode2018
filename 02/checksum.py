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

lines = sys.stdin.readlines()
preProcessed = (seq(lines)
                .map(lambda line: line.rstrip())  # remove the newline that readlines keeps
                .map(lambda line: list(line))     # convert from string to list of characters
                .map(lambda chars: countLetters(chars))
             )

twoCount =  (preProcessed
        .count(lambda charCount: hasNumOfOccurences(charCount, 2))
        )

threeCount =  (preProcessed
        .count(lambda charCount: hasNumOfOccurences(charCount, 3))
        )

checkSum = twoCount * threeCount
    
print(f'checkSum: {checkSum}')

