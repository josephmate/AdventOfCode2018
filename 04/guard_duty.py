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
gaurdStartRegex = re.compile(r'\[(\d\d\d\d-\d\d-\d\d) (\d\d):(\d\d)\] Guard #(\d+) begins shift')
# [1518-03-18 00:35] falls asleep
gaurdSleepRegex = re.compile(r'\[(\d\d\d\d-\d\d-\d\d) (\d\d):(\d\d)\] falls asleep')
# [1518-03-18 00:59] wakes up
gaurdWakeRegex = re.compile(r'\[(\d\d\d\d-\d\d-\d\d) (\d\d):(\d\d)\] wakes up')

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def toString(self):
        return f'[{self.year}-{self.month}-{self.day}]'

class GuardShift:
    def __init__(self, guardId):
        self.guardId = guardId

# map of date 
sleepMap = {} 

for guardLog in guardLogs:
    if gaurdStartRegex.match(guardLog):
        None
    elif gaurdSleepRegex.match(guardLog):
        None
    elif gaurdWakeRegex.match(guardLog):
        None
    else:
        print('UNRECOGNIZED: ' + guardLog)

