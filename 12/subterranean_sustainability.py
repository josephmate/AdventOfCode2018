import sys
import re
from functional import seq
from collections import deque

PLANT = "#"
DEAD = "."

initialStateRegex = re.compile(r'initial state: (.*)')
def initialStateFromStr(starStr):
    m = initialStateRegex.match(starStr)
    initialState = {}
    posn = 0
    for char in list(m.group(1)):
        initialState[posn] = char
        posn += 1

    return initialState


transformRegex = re.compile(r'(.*) => (.*)')
def transformFromStr(starStr):
    m = transformRegex.match(starStr)
    return (m.group(1), m.group(2))


state = initialStateFromStr(sys.stdin.readline().rstrip())
# bounds for the search
minPosn = 0
maxPosn = len(state)

sys.stdin.readline() # next line is empty, ignore

transformMap = {}
for line in sys.stdin:
    line = line.rstrip()
    (transform, result) = transformFromStr(line)
    if result == PLANT:
        transformMap[transform] = result


#print(state)
#print(minPosn)
#print(maxPosn)
#print(transformMap)

def getMinMax(state): 
    minPosn = float("inf")
    maxPosn = float("-inf")
    for key in state:
        if key < minPosn:
            minPosn = key
        if key > maxPosn:
            maxPosn = key
    return (minPosn, maxPosn)

def lookup(state, posn):
    if posn in state:
        return state[posn]
    return DEAD

def iterateGeneration(state, minPosn, maxPosn, transformMap):
    newState = {}
    for i in range(minPosn-3, maxPosn + 1 + 3):
        transformKey = ''
        for j in range(-2, 2+1):
            transformKey += lookup(state, i+j)
        if transformKey in transformMap:
            #print(transformKey + ' => ' + PLANT)
            newState[i] = PLANT
        else:
            None
            #print(transformKey + ' => ' + DEAD)

    return newState

def printState(state, minPosn, maxPosn):
    toPrint = ""
    for i in range(minPosn, maxPosn + 1):
        toPrint += lookup(state, i)
    print(toPrint)


#printState(state, minPosn, maxPosn)
for i in range(0, 50000000000):
    state = iterateGeneration(state, minPosn, maxPosn, transformMap)
    (minPosn, maxPosn) = getMinMax(state)
    #print(minPosn)
    #print(maxPosn)
    #printState(state, minPosn, maxPosn)

soln = 0
for i in range(minPosn, maxPosn + 1):
    if i in state:
        soln += i

print(soln)
