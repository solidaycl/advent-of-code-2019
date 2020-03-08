#
# part 1
#
def compute(noun, verb):
    f = open("input", "r")

    data = f.read().split(",")
    # convert to int
    for i in range(0, len(data)):
        data[i] = int(data[i])

    # set the noun and the verb
    data[1] = noun
    data[2] = verb

    for i in range(len(data)):
        if (i % 4 == 0):
            if (data[i] == 99):
                break;
            if (data[i] == 1):
                data[data[i + 3]] = data[data[i + 1]] + data[data[i + 2]]
            if (data[i] == 2):
                data[data[i + 3]] = data[data[i + 1]] * data[data[i + 2]]
    f.close()
    return data[0]


print(compute(12, 2))


#
# part 2
#
def findResult(result):
    for i in range(0, 99):
        for j in range(0, 99):
            if (compute(i, j) == result):
                return (100 * i) + j


print(findResult(19690720))
