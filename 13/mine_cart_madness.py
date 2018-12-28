LEFT_TO_UP = '/'
DOWN_TO_LEFT = '/'
RIGHT_TO_UP = '\\'
DOWN_TO_RIGHT = '\\'
UP_DOWN = '|'
LEFT_RIGHT = '-'
INTERSECT = '+'
CART_UP = '^'
CART_DOWN= 'v'
CART_LEFT = '<'
CART_RIGHT = '>'

def printBoard(state, carts):
    row = 0
    for rowData in state:
        col = 0
        for colData in rowData:
            if (row, col) in carts:
                print(carts[(row,col)], end="")
            else:
                print(colData, end="")
            col += 1
        row += 1
        print()

def parse(lines):
    carts = {}
    currentState = []
    row = 0
    for line in lines:
        col = 0
        rowState = []
        for char in list(line.rstrip()):
            if char == CART_UP or char == CART_DOWN:
                rowState.append(UP_DOWN)
                carts[(row,col)] = char
            elif char == CART_LEFT or char == CART_RIGHT:
                rowState.append(LEFT_RIGHT)
                carts[(row,col)] = char
            else:
                rowState.append(char)
            col += 1
        currentState.append(rowState)
        row += 1
    return (carts, currentState)

# returns 0: Colision location. None if no collision
#         1: New position of the carts
def iterate(state, carts):
    newCarts = {}
    for cart in carts:
        newCarts[cart] = carts[cart]

    return (None, carts)

def solve(lines):
    (carts, state) = parse(lines)
    collision = None
    print(carts)
    printBoard(state, carts)
    i = 1
    while collision == None:
        (collision, carts) = iterate(state, carts)
        print(i)
        print(carts)
        printBoard(state, carts)
        i += 1
    


with open('sample.txt') as sampleFile:
    solve(sampleFile)

with open('input.txt') as sampleFile:
    solve(sampleFile)
