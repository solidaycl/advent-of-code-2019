#
# part 1
#
f = open("input", "r")


def getPathCoords(wirePath):
    wireCoords = []
    xPos = 0
    yPos = 0

    for i in range(0, len(wirePath)):
        for _ in range(int(wirePath[i][1:])):
            if (wirePath[i][:1] == "R"):
                xPos += 1
            if (wirePath[i][:1] == "L"):
                xPos -= 1
            if (wirePath[i][:1] == "U"):
                yPos += 1
            if (wirePath[i][:1] == "D"):
                yPos -= 1
            wireCoords.append(str(xPos) + "," + str(yPos))

    return wireCoords


wire1Coords = getPathCoords(f.readline().split(","))
wire2Coords = getPathCoords(f.readline().split(","))

intersection = list(set(wire1Coords).intersection(wire2Coords))

smallestManhattan = -1
for i in range(0, len(intersection)):
    dist = abs(int(intersection[i].split(",")[0])) + abs(int(intersection[i].split(",")[1]))
    if (dist < smallestManhattan or smallestManhattan == -1):
        smallestManhattan = dist

print(smallestManhattan)

#
# part 2
#
smallestIntersection = -1
for i in range(0, len(intersection)):
    steps = 2 + wire1Coords.index(str(intersection[i])) + wire2Coords.index(str(intersection[i]))
    if (steps < smallestIntersection or smallestIntersection == -1):
        smallestIntersection = steps
print(smallestIntersection)

f.close()
