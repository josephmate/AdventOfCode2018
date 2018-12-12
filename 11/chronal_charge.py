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

def computeTotalPower(grid, size):
    totalPowerGrid = []
    for y in range(0, 300-size):
        xs = []
        for x in range(0, 300-size):
            totalPower = 0
            for yincement in range(0, size):
                for xincement in range(0, size):
                    totalPower += grid[y+yincement][x+xincement]
            xs.append(totalPower)
        totalPowerGrid.append(xs)
    return totalPowerGrid

def subChronalCharge(grid, size):
    totalPowerGrid = computeTotalPower(grid, size)
    maxVal = size * size * - 5 - 1
    for y in range(0, 300-size):
        for x in range(0, 300-size):
            if totalPowerGrid[y][x] > maxVal:
                maxVal = totalPowerGrid[y][x]
                maxX = x
                maxY = y

    return maxX + 1, maxY + 1, maxVal

def chronalCharge(gridSerial):
    grid = computeGrid(gridSerial)

    maxVal = 300 * 300 * - 5 - 1
    for size in range(0, 300):
        newX, newY, newVal = subChronalCharge(grid, size)
        if newVal > maxVal:
            maxX = newX
            maxY = newY
            maxSize = size
            maxVal = newVal

    return maxX + 1, maxY + 1, size, maxVal



print(f'Fuel cell at     3,5, grid serial number  8: power level  4 actual: {powerLevel(computeGrid( 8),   3,  5)}')
print(f'Fuel cell at  122,79, grid serial number 57: power level -5 actual: {powerLevel(computeGrid(57), 122, 79)}')
print(f'Fuel cell at 217,196, grid serial number 39: power level  0 actual: {powerLevel(computeGrid(39), 217, 196)}')
print(f'Fuel cell at 101,153, grid serial number 71: power level  4 actual: {powerLevel(computeGrid(71), 101, 153)}')

print(f'{subChronalCharge(computeGrid(18), 3)}: should return 33,45 (with a total power of 29)')
print(subChronalCharge(computeGrid(2187), 3))

print(f'For grid serial number 18, the largest total square (with a total power of 113) is 16x16 and has a top-left corner of 90,269, so its identifier is 90,269,16. {chronalCharge(18)}')
print(f'For grid serial number 42, the largest total square (with a total power of 119) is 12x12 and has a top-left corner of 232,251, so its identifier is 232,251,12. {chronalCharge(42)}')
print(chronalCharge(2187))
