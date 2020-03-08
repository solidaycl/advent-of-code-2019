import itertools
#
# part 1
#
def getDataVal(data, paramMode, index, relativeBase):
    if(paramMode == 1):
        return data[index]
    elif(paramMode == 0):
        return data[data[index]]
    elif(paramMode == 2):
        return data[index + relativeBase]


def compute(input):

    inputIndex = 0;

    relativeBase = 0

    output = []

    f = open("input", "r")

    data = f.read().split(",")
    #convert to int
    for i in range(0, len(data)):
        data[i] = int(data[i])

    # add memory 100 times the size of the program
    for i in range(0, len(data)*100):
        data.append(0)

    i = 0
    while i < len(data):

        instruction = str(data[i]).zfill(5)
        opcode = int(instruction[-2:])
        paramMode1 = int(instruction[2])
        paramMode2 = int(instruction[1])
        paramMode3 = int(instruction[0])

        if(opcode == 99):
            return output;
        elif(opcode == 1):
            data[data[i+3]] = getDataVal(data, paramMode1, i+1, relativeBase) + getDataVal(data, paramMode2, i+2, relativeBase)
            i+=4
        elif(opcode == 2):
            data[data[i+3]] = getDataVal(data, paramMode1, i+1, relativeBase) * getDataVal(data, paramMode2, i+2, relativeBase)
            i+=4
        elif(opcode == 3): 
            data[data[i+1]] = input[inputIndex] #Cycle through inputs
            #inputIndex += 1;
            i+=2
        elif(opcode == 4):
            print(getDataVal(data, paramMode1, i+1, relativeBase))
            output.append(getDataVal(data, paramMode1, i+1, relativeBase))
            i+=2
        elif(opcode == 5):
            if(getDataVal(data, paramMode1, i+1, relativeBase) != 0):
                i = getDataVal(data, paramMode2, i+2, relativeBase)
            else: 
                i+=3
        elif(opcode == 6):
            if(getDataVal(data, paramMode1, i+1, relativeBase) == 0):
                i = getDataVal(data, paramMode2, i+2, relativeBase)
            else: 
                i+=3
        elif(opcode == 7):
            if(getDataVal(data, paramMode1, i+1, relativeBase) < getDataVal(data, paramMode2, i+2, relativeBase)):
                data[data[i+3]] = 1
            else:
                data[data[i+3]] = 0
            i+=4
        elif(opcode == 8):
            if(getDataVal(data, paramMode1, i+1, relativeBase) == getDataVal(data, paramMode2, i+2, relativeBase)):
                data[data[i+3]] = 1
            else:
                data[data[i+3]] = 0
            i+=4
        elif(opcode == 9):
            print(str(relativeBase) + " + "  + str(getDataVal(data, paramMode1, i+1, relativeBase)))
            relativeBase += int(getDataVal(data, paramMode1, i+1, relativeBase))
            i+=2

    f.close()
    print("returning none from end")
    return None


print(compute([1]))
