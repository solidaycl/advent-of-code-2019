#
# part 1
#
f = open("input", "r")

adjacencyForward = {}

for x in f:
    conn = x.strip().split(")")

    if (adjacencyForward.get(conn[0]) != None):
        adjacencyForward.update({conn[0]: adjacencyForward.get(conn[0]) + "|" + conn[1]})
    else:
        adjacencyForward.update({conn[0]: conn[1]});


def recTraverse(start, depth):
    if (adjacencyForward.get(start) == None):
        return depth;

    sum = depth
    for x in list(adjacencyForward.get(start).split("|")):
        sum += recTraverse(x, depth + 1)
    return sum


print(str(recTraverse("COM", 0)))

f.close()

#
# part 2
#
f = open("input", "r")

adjacencyBackward = {}

for x in f:
    conn = x.strip().split(")")

    if (adjacencyBackward.get(conn[1]) != None):
        adjacencyBackward.update({conn[1]: adjacencyBackward.get(conn[1]) + "|" + conn[0]})
    else:
        adjacencyBackward.update({conn[1]: conn[0]});


def findSanta(lastPlanet, currentPlanet, depth):
    if (currentPlanet == "SAN"):
        return depth;

    sum = 0
    if (adjacencyForward.get(currentPlanet) != None):
        for x in list(adjacencyForward.get(currentPlanet).split("|")):
            if (x != lastPlanet):
                sum += findSanta(currentPlanet, x, depth + 1)

    if (adjacencyBackward.get(currentPlanet) != None):
        for x in list(adjacencyBackward.get(currentPlanet).split("|")):
            if (x != lastPlanet):
                sum += findSanta(currentPlanet, x, depth + 1)
    return sum;


print(str(findSanta(None, "YOU", 0) - 2))

f.close()
