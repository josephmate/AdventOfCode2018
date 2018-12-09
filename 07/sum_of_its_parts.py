import sys
import re
from functional import seq

class StepDependency:
    def __init__(self, before, after):
        self.before = before
        self.after = after

    def __str__(self):
        return f'{self.before}-->{self.after}'

    def __repr__(self):
        return f'{self.before}-->{self.after}'

stepRegex = re.compile(r'Step (\w+) must be finished before step (\w+) can begin.')
def fromStrToStepDependency(strEncodedStepDependency):
    m = stepRegex.match(strEncodedStepDependency)
    return StepDependency(m.group(1), m.group(2))

def makeDepGraph(stepDeps):
    dependencyGraph = {}
    for stepDep in stepDeps:
        if not stepDep.before in dependencyGraph:
            dependencyGraph[stepDep.before] = set()
        if not stepDep.after in dependencyGraph:
            dependencyGraph[stepDep.after] = set()

    for stepDep in stepDeps:
        dependencyGraph[stepDep.after].add(stepDep.before)

    return dependencyGraph

stepDeps = (seq(sys.stdin)
                .map(lambda line: line.rstrip())  # remove the newline that readlines keeps
                .map(lambda line: fromStrToStepDependency(line))  
                .list() # save to a list, because multiple iterations of sys.stdin is not possible
             )

print(stepDeps)


# no parallel workers
dependencyGraph = makeDepGraph(stepDeps)
path = ""
while len(dependencyGraph) > 0:
    availableMoves = (seq(dependencyGraph)
                        .filter(lambda step: len(dependencyGraph[step]) == 0)
                        .list()
                     )
    nextMove = min(availableMoves)
    path += nextMove
    del dependencyGraph[nextMove]
    for step in dependencyGraph:
        if nextMove in dependencyGraph[step]:
            dependencyGraph[step].remove(nextMove)
print(path)


def getTimeToComplete(step):
    return ord(list(step)[0]) - 64 + 60

availableWork = set()
numWorkers = 5
workInProgress = {}
dependencyGraph = makeDepGraph(stepDeps)
currentTime = 0
path = ""
while len(dependencyGraph) > 0 or len(availableWork) > 0:

    # add newly available work as a result of completion
    availableMoves = (seq(dependencyGraph)
                        .filter(lambda step: len(dependencyGraph[step]) == 0)
                        .list()
                     )
    for move in availableMoves:
        availableWork.add(move)
        del dependencyGraph[move]

    # assign work to workers
    while len(workInProgress) < numWorkers and len(availableWork) > 0:
        nextMove = min(availableWork)
        availableWork.remove(nextMove)
        workInProgress[nextMove] = currentTime + getTimeToComplete(nextMove)
    
    # get the earliest work done
    finishedWork = min(workInProgress, key=lambda workStep: workInProgress[workStep])
    currentTime = workInProgress[finishedWork]
    del workInProgress[finishedWork]
    path += finishedWork
    for step in dependencyGraph:
        if finishedWork in dependencyGraph[step]:
            dependencyGraph[step].remove(finishedWork)


print(path)
print(currentTime)
