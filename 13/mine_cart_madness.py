RIGHT_TO_UP = '/'
LEFT_TO_DOWN = '/'
DOWN_TO_LEFT = '/'
UP_TO_RIGHT = '/'
RIGHT_TO_DOWN = '\\'
LEFT_TO_UP = '\\'
DOWN_TO_RIGHT = '\\'
UP_TO_LEFT = '\\'
UP_DOWN = '|'
LEFT_RIGHT = '-'
INTERSECT = '+'
CART_UP = '^'
CART_DOWN= 'v'
CART_LEFT = '<'
CART_RIGHT = '>'


class CartState:
    def __init__(self, direction, intersectCounter):
        self.direction = direction
        self.intersectCounter = intersectCounter

def printBoard(state, carts):
    row = 0
    for rowData in state:
        col = 0
        for colData in rowData:
            if (row, col) in carts:
                print(carts[(row,col)].direction, end="")
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
                carts[(row,col)] = CartState(char, 0)
            elif char == CART_LEFT or char == CART_RIGHT:
                rowState.append(LEFT_RIGHT)
                carts[(row,col)] = CartState(char, 0)
            else:
                rowState.append(char)
            col += 1
        currentState.append(rowState)
        row += 1
    return (carts, currentState)

def updateCartPosn(state, cartPosn, cartState):
    cartDirection = cartState.direction
    intersectCount = cartState.intersectCounter

    if cartDirection == CART_UP:
        newPosn = (cartPosn[0]-1, cartPosn[1])
    elif cartDirection == CART_DOWN:
        newPosn = (cartPosn[0]+1, cartPosn[1])
    elif cartDirection == CART_LEFT:
        newPosn = (cartPosn[0], cartPosn[1]-1)
    else: #cartDirection == CART_RIGHT:
        newPosn = (cartPosn[0], cartPosn[1]+1)

    #print(f'"{cartDirection} : "{cartPosn} -> {newPosn}')
    
    newIntersectCount = intersectCount
    newTrack = state[newPosn[0]][newPosn[1]]
    if cartDirection == CART_RIGHT and newTrack == RIGHT_TO_UP:
        newDirection = CART_UP
    elif cartDirection == CART_LEFT and newTrack == LEFT_TO_DOWN:
        newDirection = CART_DOWN
    elif cartDirection == CART_DOWN and newTrack == DOWN_TO_LEFT:
        newDirection = CART_LEFT
    elif cartDirection == CART_UP and newTrack == UP_TO_RIGHT:
        newDirection = CART_RIGHT
    elif cartDirection == CART_RIGHT and newTrack == RIGHT_TO_DOWN:
        newDirection = CART_DOWN
    elif cartDirection == CART_LEFT and newTrack == LEFT_TO_UP:
        newDirection = CART_UP
    elif cartDirection == CART_DOWN and newTrack == DOWN_TO_RIGHT:
        newDirection = CART_RIGHT
    elif cartDirection == CART_UP and newTrack == UP_TO_LEFT:
        newDirection = CART_LEFT
    elif newTrack == UP_DOWN:
        newDirection = cartDirection
    elif newTrack == LEFT_RIGHT:
        newDirection = cartDirection
    else: #newTrack == INTERSECT:
        newIntersectCount = intersectCount + 1
        #it turns left the first time
        if intersectCount % 3 == 0:
            if cartDirection == CART_UP:
                newDirection = CART_LEFT
            elif cartDirection == CART_DOWN:
                newDirection = CART_RIGHT
            elif cartDirection == CART_LEFT:
                newDirection = CART_DOWN
            else: #cartDirection == CART_RIGHT:
                newDirection = CART_UP
        #goes straight the second time
        elif intersectCount % 3 == 1:
            newDirection = cartDirection
        #turns right the third time
        else: #intersectCount % 3 == 2:
            if cartDirection == CART_UP:
                newDirection = CART_RIGHT
            elif cartDirection == CART_DOWN:
                newDirection = CART_LEFT
            elif cartDirection == CART_LEFT:
                newDirection = CART_UP
            else: #cartDirection == CART_RIGHT:
                newDirection = CART_DOWN

    #print(f'"{cartDirection} : "{cartPosn} -> {newPosn} : {newDirection}')
    
    return (newPosn, CartState(newDirection, newIntersectCount))

# returns 0: Colision location. None if no collision
#         1: New position of the carts
def iterate(state, carts):
    newCarts = {}
    for cart in carts:
        (newPosn, newDirection) = updateCartPosn(state, cart, carts[cart])
        if newPosn in newCarts:
            # there was a colision
            return (newPosn, newCarts)
        newCarts[newPosn] = newDirection

    return (None, newCarts)

def solve(lines):
    (carts, state) = parse(lines)
    collision = None
    printBoard(state, carts)
    i = 1
    while collision == None:
        (collision, carts) = iterate(state, carts)
        print(i)
        printBoard(state, carts)
        i += 1

    print(collision)
    


with open('sample.txt') as sampleFile:
    solve(sampleFile)

with open('input.txt') as sampleFile:
    solve(sampleFile)
