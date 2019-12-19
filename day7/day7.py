import itertools
#
# part 1
#
def getDataVal(data, paramMode, index):
    if(paramMode == 1):
        return data[index]
    elif(paramMode == 0):
        return data[data[index]]


def compute(input):

    inputIndex = 0;

    f = open("input", "r")

    data = f.read().split(",")
    #convert to int
    for i in range(0, len(data)):
        data[i] = int(data[i])

    i = 0
    while i < len(data):

        instruction = str(data[i]).zfill(5)
        opcode = int(instruction[-2:])
        paramMode1 = int(instruction[2])
        paramMode2 = int(instruction[1])
        paramMode3 = int(instruction[0])

        if(opcode == 99):
            return None;
        elif(opcode == 1):
            data[data[i+3]] = getDataVal(data, paramMode1, i+1) + getDataVal(data, paramMode2, i+2)
            i+=4
        elif(opcode == 2):
            data[data[i+3]] = getDataVal(data, paramMode1, i+1) * getDataVal(data, paramMode2, i+2)
            i+=4
        elif(opcode == 3): 
            data[data[i+1]] = input[inputIndex] #Cycle through inputs
            inputIndex += 1;
            i+=2
        elif(opcode == 4):
            if(len(input) == inputIndex):
                return getDataVal(data, paramMode1, i+1)
            i+=2
        elif(opcode == 5):
            if(getDataVal(data, paramMode1, i+1) != 0):
                i = getDataVal(data, paramMode2, i+2)
            else: 
                i+=3
        elif(opcode == 6):
            if(getDataVal(data, paramMode1, i+1) == 0):
                i = getDataVal(data, paramMode2, i+2)
            else: 
                i+=3
        elif(opcode == 7):
            if(getDataVal(data, paramMode1, i+1) < getDataVal(data, paramMode2, i+2)):
                data[data[i+3]] = 1
            else:
                data[data[i+3]] = 0
            i+=4
        elif(opcode == 8):
            if(getDataVal(data, paramMode1, i+1) == getDataVal(data, paramMode2, i+2)):
                data[data[i+3]] = 1
            else:
                data[data[i+3]] = 0
            i+=4
        else:
            break;

    f.close()
    print("returning none from end")
    return None


maxSignal = -1

for input in itertools.permutations([0,1,2,3,4]):

    #conver to list of lists
    input = list(input)
    for j in range(0, len(input)):
        input[j] = [input[j]]
        
    input[0].append(0)
    output = int()
    for i in range(0, 5):
        output = compute(input[i])
        input[(i+1) % 5].append(output)
    if(output > maxSignal or maxSignal == -1):
        maxSignal = output

print(maxSignal)


#
# part 2
#
maxSignal = -1

for input in itertools.permutations([5,6,7,8,9]):

    #conver to list of lists
    input = list(input)
    for j in range(0, len(input)):
        input[j] = [input[j]]
        
    input[0].append(0)

    i = 0;
    output = int()
    lastOutput = int()
    while output != None: 
        lastOutput = output
        output = compute(input[i%5])
        input[(i+1) % 5].append(output)
        i += 1

    if(lastOutput > maxSignal or maxSignal == -1):
        maxSignal = lastOutput

print(maxSignal)