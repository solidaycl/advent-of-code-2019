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
    jump_if_true = 5            # if the first parameter is non-zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
    jump_if_false = 6           # if the first parameter is zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
    less_than = 7               # if the first parameter is less than the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
    equals = 8                  # if the first parameter is equal to the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
    adjust_relative_base = 9    # adjusts the relative base by the value of its only parameter.
    halt = 99


class IntcodeDAO:

    instruction_pointer = 0
    relative_base_pointer = 0
    data = []
    output = []

    def __init__(self, path="input"):
        f = open(path, "r")
        self.data = f.read().split(",")
        # convert to int
        for i in range(0, len(self.data)):
            self.data[i] = int(self.data[i])
        # add memory 100 times the size of the program
        for i in range(0, len(self.data) * 100):
            self.data.append(0)
        f.close()

    def get(self, address, mode = Mode.immediate):
        if mode == Mode.immediate:
            return self.get(index)
        elif mode == Mode.position:
            return self.get(self.get(address))
        elif mode == Mode.relative_position:
            return self.get(self.get(self.relative_base_pointer))

    def set(self, address, val):
            self.data[address] = val

    # get the value of the parameter number specified, including modes
    def get_param(self, param_num):

        instruction = str(data[instruction_pointer]).zfill(5)
        opcode = int(instruction[-2:])

        param1Mode = int(instruction[2])
        param2Mode = int(instruction[1])
        param3Mode = int(instruction[0])

        if param_num == 1:
            return self.get(self.instruction_pointer + 1, param1Mode)
        if param_num == 2:
            return self.get(self.instruction_pointer + 2, param2Mode)
        if param_num == 3:
            return self.get(self.instruction_pointer + 3, param3Mode)

    def get_op_code(self):
        instruction = str(get(self.instruction_pointer)).zfill(5)
        return int(instruction[-2:])

    def get_instruction_mode(self):
        return 0

    def inc_instruction_pointer(self, num):
        self.instruction_pointer += num

    def set_instruction_pointer(self, num):
        self.instruction_pointer = num

    def inc_relative_base_pointer(self, num):
        self.relative_base_pointer += num

    def set_relative_base_pointer(self, num):
        self.relative_base_pointer = num

def compute(self, inputPath):

    program = IntcodeDAO(inputPath)

    while instruction_pointer < len(data):

        op_code = program.get_op_code()

        if op_code == OpCode.halt:
            return 0    # output

        elif op_code == OpCode.add:
            program.set(
                program.get_param(3),
                program.get_param(1) + program.get_param(2)
            )
            program.inc_instruction_pointer(4)

        elif op_code == OpCode.multiply:
            program.set(
                program.get_param(3),
                program.get_param(1) * program.get_param(2)
            )
            program.inc_instruction_pointer(4)

        # elif op_code == OpCode.input:
        #     data[data[instruction_pointer + 1]] = input[input_index]  # Cycle through inputs
        #     # inputIndex += 1;
        #     program.inc_instruction_pointer(2)
        elif op_code == OpCode.output:
            print(program.get_param(1))
            # output.append(getDataVal(data, paramMode1, instruction_pointer + 1, relative_base))
            program.inc_instruction_pointer(2)

        elif op_code == OpCode.jump_if_true:
            if program.get_param(1) != 0:
                program.set_instruction_pointer(program.get_param(2))
            else:
                program.inc_instruction_pointer(3)

        elif op_code == OpCode.jump_if_false:
            if program.get_param(1) == 0:
                program.set_instruction_pointer(program.get_param(2))
            else:
                program.inc_instruction_pointer(3)

        elif op_code == OpCode.less_than:
            if program.get_param(1) < program.get_param(2):
                program.set(program.get_param(3), 1)
            else:
                program.set(program.get_param(3), 0)
            program.inc_instruction_pointer(4)

        elif op_code == OpCode.equals:
            if program.get_param(1) == program.get_param(2):
                program.set(program.get_param(3), 1)
            else:
                program.set(program.get_param(3), 0)
            program.inc_instruction_pointer(4)

        elif op_code == 9:
            print("adjusting base pointer")
            program.inc_relative_base_pointer(program.get_param(1))
            program.inc_instruction_pointer(2)

    print("returning none from end")
    return None


compute("input")
