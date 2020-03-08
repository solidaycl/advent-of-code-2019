#
# part 1
#
def getDataVal(data, paramMode, index):
    if (paramMode == 1):
        return data[index]
    elif (paramMode == 0):
        return data[data[index]]


def compute(inputVal):
    f = open("input", "r")

    data = f.read().split(",")
    # convert to int
    for i in range(0, len(data)):
        data[i] = int(data[i])

    i = 0
    while i < len(data):

        instruction = str(data[i]).zfill(5)
        opcode = int(instruction[-2:])
        paramMode1 = int(instruction[2])
        paramMode2 = int(instruction[1])
        paramMode3 = int(instruction[0])

        if (opcode == 99):
            break;
        elif (opcode == 1):
            data[data[i + 3]] = getDataVal(data, paramMode1, i + 1) + getDataVal(data, paramMode2, i + 2)
            i += 4
        elif (opcode == 2):
            data[data[i + 3]] = getDataVal(data, paramMode1, i + 1) * getDataVal(data, paramMode2, i + 2)
            i += 4
        elif (opcode == 3):
            data[data[i + 1]] = inputVal
            i += 2
        elif (opcode == 4):
            print(getDataVal(data, paramMode1, i + 1))
            i += 2
        elif (opcode == 5):
            if (getDataVal(data, paramMode1, i + 1) != 0):
                i = getDataVal(data, paramMode2, i + 2)
            else:
                i += 3
        elif (opcode == 6):
            if (getDataVal(data, paramMode1, i + 1) == 0):
                i = getDataVal(data, paramMode2, i + 2)
            else:
                i += 3
        elif (opcode == 7):
            if (getDataVal(data, paramMode1, i + 1) < getDataVal(data, paramMode2, i + 2)):
                data[data[i + 3]] = 1
            else:
                data[data[i + 3]] = 0
            i += 4
        elif (opcode == 8):
            if (getDataVal(data, paramMode1, i + 1) == getDataVal(data, paramMode2, i + 2)):
                data[data[i + 3]] = 1
            else:
                data[data[i + 3]] = 0
            i += 4
        else:
            break;

    f.close()
    return data[0]


compute(1)

#
# part 2
#
compute(5)
