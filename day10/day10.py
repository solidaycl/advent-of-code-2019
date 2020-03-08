import math

#
# part 1
#

"""
f = open("input", "r")

astroidLocations = []

width = 0
height = 0
for line in f.readlines():
    x = 0
    for char in line:
        if(char == "#"):
            astroidLocations.append([x, height])
        x += 1
    width = x
    height += 1

max = -1
for stationCandidate in astroidLocations:

    relativeAstroids = []
    # make all astroids relative to the candidate
    for i in range(0, len(astroidLocations)):
        relativeAstroids.append([astroidLocations[i][0] -stationCandidate[0],astroidLocations[i][1] -stationCandidate[1]])

    possibleAstroids = list.copy(relativeAstroids)

    for astroid in possibleAstroids:
        x = astroid[0]
        y = astroid[1]

        gcd = math.gcd(abs(x), abs(y))
        if(gcd == 0): 
            gcd = 1
        x_factored = x/ gcd
        y_factored = y/ gcd

        j = 1
        while(abs(x_factored) * j < width and abs(y_factored)*j < height and not(x == y and y == 0)):
            if(possibleAstroids.__contains__([x_factored * j, y_factored * j]) and j != gcd):
                possibleAstroids.remove([x_factored * j, y_factored * j])
                #print([x_factored * j, y_factored * j])
                #print(str(gcd) + " = " + str(j))
            j += 1

    if(len(possibleAstroids)-1 > max or max == -1):
        max = len(possibleAstroids) -1

#print(max)

f.close()
"""


def polar(x, y):
    return math.hypot(x, y), math.degrees(math.atan2(y, x)) + 90


#
# part 2
#
f = open("input", "r")

astroidLocations = []

width = 0
height = 0
for line in f.readlines():
    x = 0
    for char in line:
        if (char == "#"):
            astroidLocations.append([x, height])
        x += 1
    width = x
    height += 1

max = -1
bestAstroid = ()
for stationCandidate in astroidLocations:
    relativeAstroids = []
    polarAstroids = []
    for i in range(0, len(astroidLocations)):

        # make all astroids relative to the candidate
        relativeAstroids.append(
            [astroidLocations[i][0] - stationCandidate[0], astroidLocations[i][1] - stationCandidate[1]])

        # convert to positive y up and negative down
        relativeAstroids[i] = relativeAstroids[i][0], relativeAstroids[i][1]

        # convert to polar coords
        polarAstroids.append(polar(relativeAstroids[i][0], relativeAstroids[i][1]))

        # convert - degrees into 
        if (polarAstroids[i][1] < 0):
            polarAstroids[i] = polarAstroids[i][0], abs(polarAstroids[i][1]) + 180

    # remove this astroid
    polarAstroids.remove((0.0, 90.0))
    # sort the polar coords according to distance
    sortedPolarAstroids = sorted(polarAstroids, key=lambda astroid: (astroid[1], astroid[0]))

    # remove all the duplicates
    lastDegrees = 361
    l = len(sortedPolarAstroids)
    i = 0
    while (i < l):
        if (math.isclose(sortedPolarAstroids[i][1], lastDegrees)):
            lastDegrees = sortedPolarAstroids[i][1]
            l -= 1
            sortedPolarAstroids.remove(sortedPolarAstroids[i])
        else:
            lastDegrees = sortedPolarAstroids[i][1]
            i += 1

    if (len(sortedPolarAstroids) > max):
        bestAstroid = stationCandidate
        max = len(sortedPolarAstroids)

print(str(bestAstroid) + ": " + str(max))

f.close()
