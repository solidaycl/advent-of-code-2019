import enum


#
# part 1
#
class Mode(enum.Enum):
    position = 0                # causes the parameter to be interpreted as a position
    immediate = 1               # parameter is interpreted as a value
    relative_position = 2       # parameter is interpreted as a position relative to base pointer


class OpCode(enum.Enum):
    add = 1
    multiply = 2
    input = 3
    output = 4
    jump_if_true = 5        # if the first parameter is non-zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
    jump_if_false = 6       # if the first parameter is zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
    less_than = 7           # if the first parameter is less than the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
    equals = 8              # if the first parameter is equal to the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
    halt = 99


def getDataVal(data, paramMode, index, relativeBase):
    if paramMode == Mode.immediate:
        return data[index]
    elif paramMode == Mode.position:
        return data[data[index]]
    elif paramMode == Mode.relative_position:
        return data[data[index + relativeBase]]


def compute(input):
    input_index = 0
    relative_base = 0

    output = []

    f = open("input", "r")

    data = f.read().split(",")
    # convert to int
    for i in range(0, len(data)):
        data[i] = int(data[i])

    # add memory 100 times the size of the program
    for i in range(0, len(data) * 100):
        data.append(0)

    instruction_pointer = 0
    while instruction_pointer < len(data):

        instruction = str(data[instruction_pointer]).zfill(5)
        opcode = int(instruction[-2:])
        paramMode1 = int(instruction[2])
        paramMode2 = int(instruction[1])
        paramMode3 = int(instruction[0])

        if opcode == OpCode.halt:
            return output

        elif opcode == OpCode.add:
            data[data[instruction_pointer + 3]] = \
                getDataVal(data, paramMode1, instruction_pointer + 1, relative_base) \
                + getDataVal(data, paramMode2, instruction_pointer + 2, relative_base)
            instruction_pointer += 4

        elif opcode == OpCode.multiply:
            data[data[instruction_pointer + 3]] = \
                getDataVal(data, paramMode1, instruction_pointer + 1, relative_base) \
                * getDataVal(data, paramMode2, instruction_pointer + 2, relative_base)
            instruction_pointer += 4

        elif opcode == OpCode.input:
            data[data[instruction_pointer + 1]] = input[input_index]  # Cycle through inputs
            # inputIndex += 1;
            instruction_pointer += 2

        elif opcode == OpCode.output:
            print(getDataVal(data, paramMode1, instruction_pointer + 1, relative_base))
            output.append(getDataVal(data, paramMode1, instruction_pointer + 1, relative_base))
            instruction_pointer += 2

        elif opcode == OpCode.jump_if_true:
            if getDataVal(data, paramMode1, instruction_pointer + 1, relative_base) != 0:
                instruction_pointer = getDataVal(data, paramMode2, instruction_pointer + 2, relative_base)
            else:
                instruction_pointer += 3

        elif opcode == OpCode.jump_if_false:
            if getDataVal(data, paramMode1, instruction_pointer + 1, relative_base) == 0:
                instruction_pointer = getDataVal(data, paramMode2, instruction_pointer + 2, relative_base)
            else:
                instruction_pointer += 3

        elif opcode == OpCode.less_than:
            if getDataVal(data, paramMode1, instruction_pointer + 1, relative_base) < getDataVal(data, paramMode2, instruction_pointer + 2, relative_base):
                data[data[instruction_pointer + 3]] = 1
            else:
                data[data[instruction_pointer + 3]] = 0
            instruction_pointer += 4

        elif opcode == OpCode.equals:
            if getDataVal(data, paramMode1, instruction_pointer + 1, relative_base) == \
                    getDataVal(data, paramMode2, instruction_pointer + 2, relative_base):
                data[data[instruction_pointer + 3]] = 1
            else:
                data[data[instruction_pointer + 3]] = 0
            instruction_pointer += 4
        elif opcode == 9:
            print(str(relative_base) + " + " + str(getDataVal(data, paramMode1, instruction_pointer + 1, relative_base)))
            relative_base += int(getDataVal(data, paramMode1, instruction_pointer + 1, relative_base))
            instruction_pointer += 2

    f.close()
    print("returning none from end")
    return None


print(compute([1]))
