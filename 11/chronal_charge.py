import sys
import re
from functional import seq
from collections import deque

def computeGrid(gridSerial):
    return None

def powerLevel(grid, x, y):
    x = x - 1 # translate from 1 index, to 0 index
    y = y - 1
    return None

def chronalCharge(gridSerial):
    return None



print(f'Fuel cell at  122,79, grid serial number 57: power level -5 actual: {powerLevel(computeGrid(57), 122, 79)}')
print(f'Fuel cell at 217,196, grid serial number 39: power level  0 actual: {powerLevel(computeGrid(39), 217, 196)}')
print(f'Fuel cell at 101,153, grid serial number 71: power level  4 actual: {powerLevel(computeGrid(71), 101, 153)}')

print(f'{chronalCharge(18)}: should return 33,45 (with a total power of 29')
print(chronalCharge(18))
