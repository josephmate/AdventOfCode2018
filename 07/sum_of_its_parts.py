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

stepDeps = (seq(sys.stdin)
                .map(lambda line: line.rstrip())  # remove the newline that readlines keeps
                .map(lambda line: fromStrToStepDependency(line))  
                .list() # save to a list, because multiple iterations of sys.stdin is not possible
             )

print(stepDeps)

dependencyGraph = {}
for stepDep in stepDeps:
    if not stepDep.before in dependencyGraph:
        dependencyGraph[stepDep.before] = set()
    if not stepDep.after in dependencyGraph:
        dependencyGraph[stepDep.after] = set()

for stepDep in stepDeps:
    dependencyGraph[stepDep.after].add(stepDep.before)

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

