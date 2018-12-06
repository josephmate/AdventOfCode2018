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
doublyLinkedList = deque()


reactionHappen = True
while reactionHappen:
    reactionHappened = False
    for i in range(0, len(chars)):
        if i + 1 < len(chars):
            if willRecact(chars[i], chars[i+1]):
                #print(f'{chars[i]} reacted with {chars[i+1]}')
                del chars[i:i+1]
                reactionHappened = True
                break

print(str(chars))
print(len(chars))
