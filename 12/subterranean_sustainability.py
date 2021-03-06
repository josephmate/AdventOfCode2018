import sys
import re
from functional import seq
from collections import deque

PLANT = "#"
DEAD = "."

def initialStateRaw(stateStr, startposn):
    initialState = {}
    posn = startposn
    for char in list(stateStr):
        if char == PLANT:
            initialState[posn] = char
        posn += 1

    return initialState

initialStateRegex = re.compile(r'initial state: (.*)')
def initialStateFromStr(starStr):
    m = initialStateRegex.match(starStr)
    return initialStateRaw(m.group(1), 0)


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

def sumSolution(state, minPosn, maxPosn):
    soln = 0
    for i in range(minPosn, maxPosn + 1):
        if i in state:
            soln += i
    return soln


# i=18724 min=18683 max=18820
# ###.........###..........###..................................................###.........###.......###................................###
# i=18725 min=18684 max=18821
# ###.........###..........###..................................................###.........###.......###................................###
# i=18726 min=18685 max=18822
# ###.........###..........###..................................................###.........###.......###................................###
# it takes too long to compute step by step until 5,000,000,000
# notice that the relative positions of the plants do not change,
# it's moving sideways one by one
# 18726 - 18685 = 41
# 18726 - 18822 = -96
# 50,000,000,000 - 41 = 49999999959
# 50,000,000,000 + 96 = 50000000096
 
solnState = initialStateRaw(
    '###.........###..........###..................................................###.........###.......###................................###',
    49999999959)
#                              ###          ###
#                              #  ###       #  ###
#                              #  #  ###    #  #  ###
print(sumSolution(solnState, 49999999959, 50000000096))

#printState(state, minPosn, maxPosn)
for i in range(1, 50000000000+1):
    state = iterateGeneration(state, minPosn, maxPosn, transformMap)
    (minPosn, maxPosn) = getMinMax(state)
    #print(f'i={i} min={minPosn} max={maxPosn}')
    #printState(state, minPosn, maxPosn)


print(sumSolution(state,minPosn,maxPosn))


