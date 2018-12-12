import sys
import re
from functional import seq
from collections import deque

DEBUG = False

def getHundredthDigit(digits):
    return (
            (digits % 1000) # keep only the last 3 digits
            // 100          # keep only the 3rd digit
            )

def computeGrid(gridSerial):
    grid = []
    for y in range(0, 300):
        xs = []
        for x in range(0, 300):
            # need to translate from 0 index to 1
            rackID = (x+1) + 10
            if DEBUG and x == 2 and y == 4: print(f'{x+1} + 10 = {rackID}')
            # need to translate from 0 index to 1
            powerLevel1 = rackID * (y+1)
            if DEBUG and x == 2 and y == 4: print(f'{rackID} * {y+1} = {powerLevel1}')
            powerLevel2 = powerLevel1 + gridSerial
            if DEBUG and x == 2 and y == 4: print(f'{powerLevel1} + {gridSerial} = {powerLevel2}')
            powerLevel3 = powerLevel2 * rackID
            if DEBUG and x == 2 and y == 4: print(f'{powerLevel2} * {rackID} = {powerLevel3}')
            powerLevel4 = getHundredthDigit(powerLevel3) - 5
            if DEBUG and x == 2 and y == 4: print(f'{getHundredthDigit(powerLevel3)} - 5 = {powerLevel4}')
            xs.append(powerLevel4)
        grid.append(xs)
    return grid


def powerLevel(grid, x, y):
    x = x - 1 # translate from 1 index, to 0 index
    y = y - 1
    return grid[y][x]

def totalPower(grid, x, y):
    return None

def chronalCharge(gridSerial):
    return None



print(f'Fuel cell at     3,5, grid serial number  8: power level  4 actual: {powerLevel(computeGrid( 8),   3,  5)}')
print(f'Fuel cell at  122,79, grid serial number 57: power level -5 actual: {powerLevel(computeGrid(57), 122, 79)}')
print(f'Fuel cell at 217,196, grid serial number 39: power level  0 actual: {powerLevel(computeGrid(39), 217, 196)}')
print(f'Fuel cell at 101,153, grid serial number 71: power level  4 actual: {powerLevel(computeGrid(71), 101, 153)}')

print(f'{chronalCharge(18)}: should return 33,45 (with a total power of 29')
print(chronalCharge(18))
