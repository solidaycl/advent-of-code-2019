#
# part 1
#
f = open("input", "r")

sum = 0
for x in f:
    sum += int((int(x) / 3) - 2)
print(sum)

f.close()

#
# part 2
#
f = open("input", "r")

sum = 0
for x in f:
    fuel = int((int(x) / 3) - 2)
    while (fuel > 0):
        sum += fuel
        fuel = int((int(fuel) / 3) - 2)
print(sum)

f.close()
