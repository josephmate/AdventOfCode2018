import sys
import re
from functional import seq



guardLogs = (seq(sys.stdin)
                .map(lambda line: line.rstrip())  # remove the newline that readlines keeps
                .list() # save to a list, because multiple iterations of sys.stdin is not possible
             )
guardLogs.sort()

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

###########################
# map of date to the record of the guard's shift that date
# dates are from 0 to number of days recorded - 1
# exploits the fact that there is an entry for every day
# Treating the date as number instead of date object greatly simplifies
# dealing with the dates.
###########################
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
   
guardSleepTimes = {}
for sleepEntry in sleepMap:
    minutesAsleep = 0
    for isSleeping in sleepEntry.sleeping:
        if isSleeping:
            minutesAsleep += 1
    if sleepEntry.guardId in guardSleepTimes:
        guardSleepTimes[sleepEntry.guardId] += minutesAsleep
    else:
        guardSleepTimes[sleepEntry.guardId] = minutesAsleep

mostMinutesSlept = 0
for guardId in guardSleepTimes:
    if guardSleepTimes[guardId] > mostMinutesSlept:
        mostTiredGuard = guardId
        mostMinutesSlept = guardSleepTimes[guardId]

print(f'guard {mostTiredGuard} slept {mostMinutesSlept} minutes')

minuteSleepFreq = {}
for sleepEntry in sleepMap:
    if sleepEntry.guardId == mostTiredGuard:
        for minute in range(0, 60):
            if sleepEntry.sleeping[minute]:
                if minute in minuteSleepFreq:
                    minuteSleepFreq[minute] += 1
                else:
                    minuteSleepFreq[minute] = 1


freqOfMostSleep = 0
for minute in minuteSleepFreq:
    if minuteSleepFreq[minute] > freqOfMostSleep:
        freqOfMostSleep = minuteSleepFreq[minute]
        minuteWithMostFreqSleeps = minute

print(f'guard {mostTiredGuard} slept {freqOfMostSleep} times on minute {minuteWithMostFreqSleeps}')
answer = minuteWithMostFreqSleeps*mostTiredGuard
print(f'{minuteWithMostFreqSleeps}*{mostTiredGuard}={answer}')

# map of guardId -> minute -> frequency slept
allGuardSleepFreq = {}
for guardId in guardSleepTimes:
    allGuardSleepFreq[guardId] = {}

for sleepEntry in sleepMap:
    for minute in range(0, 60):
        if sleepEntry.sleeping[minute]:
            if minute in allGuardSleepFreq[sleepEntry.guardId]:
                allGuardSleepFreq[sleepEntry.guardId][minute] += 1
            else:
                allGuardSleepFreq[sleepEntry.guardId][minute] = 1
freqOfMostSleep = 0
for guardId in allGuardSleepFreq:
    for minute in allGuardSleepFreq[guardId]:
        if allGuardSleepFreq[guardId][minute] > freqOfMostSleep:
            freqOfMostSleep = allGuardSleepFreq[guardId][minute]
            minuteWithMostFreqSleeps = minute
            guardWithHighestFreq = guardId

print(f'guard {guardWithHighestFreq} slept {freqOfMostSleep} times on minute {minuteWithMostFreqSleeps}')
answer = minuteWithMostFreqSleeps*guardWithHighestFreq
print(f'{minuteWithMostFreqSleeps}*{guardWithHighestFreq}={answer}')
