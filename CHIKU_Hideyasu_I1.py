import numpy as np

# (i) create matrix
with open("iris.data","r") as fo:
    list = np.array([])
    for line in fo:
        number = line.split(",")
        del number[-1]
        if len(number) != 0 :
            # print(number)
            FloatNumber = [float(s) for s in number]
            list = np.append(list,FloatNumber)

list = list.reshape(150,4)
list = list.T
print(list)

# (ii) count the number of specified lines
