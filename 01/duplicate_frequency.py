import sys
from functional import seq

lines = sys.stdin.readlines()
frequency = (seq(lines)
                .map(lambda line: line.rstrip())
                .map(lambda line: line.replace('+', ''))
                .map(lambda line: int(line))
                .sum()
             )

print(f'Frequency: {frequency}')
    

