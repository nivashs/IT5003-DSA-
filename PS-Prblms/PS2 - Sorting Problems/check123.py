import sys

total = [] # [ [log_one]. [], [log_two] ]
log = []

for line in sys.stdin:
    if line == '\n':
        total.append(log)
        log = []
        total.append([])
    else:
        log.append(line.count('*'))
if log:
    total.append(log)
    log = []
    total.append([])


for entry in total[:-1]:
    if entry == []:
        print()
        index = 0
    else:
        col = sum(entry)
        index = 0
        for i in entry:
            index += i
            print( '.'*(col-index) + '*'*i + '.'*(index-i))