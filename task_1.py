time =  '1h 45m,360s,25m,30m 120s,2h 60s'
sum_min = 0
for i in time.split(','):
    x = i.split()
    for y in x:
        if 'h' in y:
            eqv = int(y.replace('h',''))
            sum_min += eqv * 60
        elif 'm' in y:
            eqv = int(y.replace('m',''))
            sum_min += eqv
        elif 's' in y:
            eqv = int(y.replace('s',''))
            sum_min += eqv / 60
print(int(sum_min))

