#
# part 1
#
#f = open("input", "r")
f = open("input2", "r")

adjacency = {}

for x in f:
    conn = x.strip().split(")")

    if(adjacency.get(conn[0]) != None):
        adjacency.update({conn[0] : adjacency.get(conn[0]) + "|" + conn[1]})
    else:
        adjacency.update({conn[0] : conn[1]});

def recCount(start, count):
    if(adjacency.get(start) == None):
        return count;
    sum = 0
    for x in list(adjacency.get(start).split("|")):
        sum += count + recCount(x, count+1)
    return sum

print(str(recCount(adjacency.get("COM"), 0)))