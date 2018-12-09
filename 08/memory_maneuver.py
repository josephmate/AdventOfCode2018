import sys
import re
from functional import seq

class TreeNode:
    def __init__(self, children, metadata):
        self.children = children
        self.metadata = metadata

    def printTree(self, spacing):
        moreSpacing = spacing + ' '
        res = f'{spacing}{self.metadata}'
        for child in self.children:
            res += f'\n{spacing}{child.printTree(moreSpacing)}'
        return res

    def __str__(self):
        return self.printTree('')

    def __repr__(self):
        return self.printTree('')
    

    def sum(self):
        return (seq(self.metadata).sum()
                    + seq(self.children).map(lambda subTree: subTree.sum()).sum()
                )

    def value(self):
        if len(self.children) == 0:
            return seq(self.metadata).sum()
        
        res = 0
        for childIdx in self.metadata:
            childIdx = childIdx - 1
            if childIdx < len(self.children):
                res += self.children[childIdx].value()

        return res


def parseTreeSpec(treeSpec, index):
    numOfChildren = treeSpec[index];
    index += 1;
    numOfMetaData = treeSpec[index];
    index += 1;
    
    children = []
    for i in range(0, numOfChildren):
        (subTree, index) = parseTreeSpec(treeSpec, index)
        children.append(subTree)
    
    metadata = []
    for i in range(0, numOfMetaData):
        metadata.append(treeSpec[index])
        index += 1;

    return TreeNode(children, metadata), index


treeSpec = (seq(sys.stdin.readline().rstrip().split(' '))
                .map(lambda string: int(string))
                .list()
           )



print(treeSpec)

(tree, indexesConsumed) = parseTreeSpec(treeSpec, 0)
print(tree.sum())
print(tree.value())
