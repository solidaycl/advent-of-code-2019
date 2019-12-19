#
# part 1
#
f = open("input", "r")

imageData = f.read()

numPixelsPerLayer = 25*6

i = 0
layers = []
while i < len(str(imageData)):
    start = i
    end = i+numPixelsPerLayer
    layerData = str(imageData)[start : end]
    layers.append(layerData)
    i+= numPixelsPerLayer


fewestZeroes = -1
fewestZeroesLayer = ""
for x in layers:
    if(x.count("0") < fewestZeroes or fewestZeroes == -1):
        fewestZeroesLayer = x
        fewestZeroes = x.count("0")

print(fewestZeroesLayer.count("1") * fewestZeroesLayer.count("2"))

f.close()


#
# part 2
#
image = layers[0]
for layer in layers:
    for i in range(0, len(layer)):
        if((layer[i] == str(1) or layer[i] == str(0)) and image[i] == str(2)):
            s = list(image)
            s[i] = layer[i]
            image = "".join(s)

#print image
for i in range(0, len(image)):
    if(i%25 == 0):
        print()
    if(image[i] == str(2)):
        print(" ", end="")
    elif(image[i] == str(0)):
        print(" ", end="")
    else:
        print(image[i], end="")
print()