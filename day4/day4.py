#
# part 1
#
start = 272091
stop = 815432

def has6Digits(s):
    if(len(s) == 6):
        return True
    else: 
        return False

def contains2Same(s):
    for i in range(0, len(s)-1):
        if(s[i] == s[i+1]):
            return True
    return False

def neverDecreases(s):
    for i in range(0, len(s)-1):
        if(int(s[i]) > int(s[i+1])):
            return False
    return True

count = 0
for i in range(start, stop):
    strValue = str(i)
    if(has6Digits(strValue) and contains2Same(strValue) and neverDecreases(strValue)):
        count += 1

print(count)


#
# part 2
#
def notPartOfLargermatching(s):
    sequences = []
    sequenceIndex = 0
    i = 0
    while(i < len(s)-1):
        sequences.append(1);
        while(i < len(s)-1 and s[i] == s[i+1] ):
            sequences[sequenceIndex] += 1
            i += 1
        sequenceIndex += 1
        i+=1
    return sequences.__contains__(2) 

count = 0
for i in range(start, stop):
    strValue = str(i)
    if(has6Digits(strValue) and contains2Same(strValue) and neverDecreases(strValue) and notPartOfLargermatching(strValue)):
        # print(strValue)
        count += 1

print(count)