import sys
from functional import seq

lines = sys.stdin.readlines()
preProcessed = (seq(lines)
                .map(lambda line: line.rstrip())
                .map(lambda line: line.replace('+', ''))
                .map(lambda line: int(line))
             )

frequency = preProcessed.sum()
print(f'Frequency: {frequency}')

duplicateFrequency = 0;
frequenciesSeen = {0}
searching = True
frequency = 0

while searching:
    for line in lines:
        line.rstrip()
        line.replace('+', '')
        frequency = frequency + int(line)

        if searching:
            if frequency in frequenciesSeen:
                searching = False
                duplicateFrequency = frequency
            else:
                frequenciesSeen.add(frequency)

print(f'Repeat frequency: {duplicateFrequency}')
