def powersum(power, *args):
    total = 0
    for i in args:
        total += pow(i, power)
    return total

print powersum(2,3,4)
print powersum(4,5)
a = 3433
b = int(a);
print b