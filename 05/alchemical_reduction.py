import sys
import re
from functional import seq
from collections import deque

def willRecact(a, b):
    #print(f'{a} != {b}: {a != b}')
    #print(f'{a.upper()} == {b.upper()}: {a.upper() == b.upper()}')
    return ( a != b
            and a.upper() == b.upper()
            )

chars = list(sys.stdin.readline().rstrip())
# tried using list in my previous soltuion and then it was taking forever
# tried using a moving index, since we already know characters before the index will not react
# but that turned out to be really complicated.
# tried searching for a doubly linked list in python and found a deque.
# same thing as a doubly linked list, but instead we have this 'rotate' method for moving
# the list forward when we do not see a reaction
# our 'pointer' is the left most element
dq = deque()

dq.append("FIRST") # prevents us from rotating to the 
for c in chars:
    # message
    # append m to right most
    # m
    # append e to right most
    # me
    # append s to right most
    # mes
    # ... etc
    dq.append(c)
dq.append("END")
#   |
#   V
# FIRST message END
dq.rotate(-1)
# |
# V
# message END FIRST 
print(dq)

while True:
    print(dq)
    # arrived at the end, nothing left to read
    currentChar = dq.popleft()
    if currentChar == "END":
        break;

    # arrived at the end, nothing left to read,
    # but need to put back the previous character
    nextChar = dq.popleft()
    if nextChar == "END":
        dq.appendleft(currentChar)
        break;

    if willRecact(currentChar, nextChar):
        print(f'{currentChar} reacted with {nextChar}')
        # do not put the characters back
        # need to rotate to left once because maybe the previous character might react
        # example
        #  VV
        # abBA
        #  VV
        # aA
        # rotating back one
        # vv
        # aA
        dq.rotate(-1)
        checkFirst = dq.popleft()
        dq.appendleft(checkFirst)
        # make sure we're not at the "FIRST"
        if checkFirst == "FIRST":
            dq.rotate(1)
    # a reaction did not occur so we can advance the 'pointer'
    else:
        # VV
        # message END FIRST
        # VV
        # essage END FIRST m
        dq.appendleft(nextChar)
        dq.appendleft(currentChar)
        dq.rotate(-1)

print(dq)
print(len(dq) - 1) # -1 because FIRST is still in the list
