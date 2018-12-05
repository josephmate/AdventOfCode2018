import sys
import re
from functional import seq



guardLogs = (seq(sys.stdin)
                .map(lambda line: line.rstrip())  # remove the newline that readlines keeps
                .list() # save to a list, because multiple iterations of sys.stdin is not possible
             )
guardLogs.sort()


claimRegex = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')
# [1518-03-18 00:01] Guard #89 begins shift
gaurdStartRegex = re.compile(r'\[\d\d\d\d-\d\d-\d\d \d\d:\d\d\] Guard #(\d+) begins shift')
# [1518-03-18 00:35] falls asleep
gaurdSleepRegex = re.compile(r'\[\d\d\d\d-\d\d-\d\d \d\d:(\d\d)\] falls asleep')
# [1518-03-18 00:59] wakes up
gaurdWakeRegex = re.compile(r'\[\d\d\d\d-\d\d-\d\d \d\d:(\d\d)\] wakes up')


class GuardShift:
    def __init__(self, guardId):
        self.guardId = guardId
        self.sleeping = []
        for i in range(0, 60):
            self.sleeping.append(False)


# map of date 
sleepMap = [] 
for guardLog in guardLogs:
    if gaurdStartRegex.match(guardLog):
        parsedRecord = gaurdStartRegex.match(guardLog)
        currentShift = GuardShift(int(parsedRecord.group(1)))
        sleepMap.append(currentShift)
    elif gaurdSleepRegex.match(guardLog):
        parsedRecord = gaurdSleepRegex.match(guardLog)
        sleepStart = int(parsedRecord.group(1))
    elif gaurdWakeRegex.match(guardLog):
        parsedRecord = gaurdWakeRegex.match(guardLog)
        sleepEnd = int(parsedRecord.group(1))
        for i in range(sleepStart, sleepEnd):
            currentShift.sleeping[i] = True

    else:
        print('UNRECOGNIZED: ' + guardLog)

counter = 0
for sleepEntry in sleepMap:
    sys.stdout.write(f'{counter}\t{sleepEntry.guardId}')
    sys.stdout.write('\t|')
    for isSleeping in sleepEntry.sleeping:
        if isSleeping:
            sys.stdout.write(' ')
        else:
            sys.stdout.write('#')
    sys.stdout.write('\n')
    counter+=1
        
