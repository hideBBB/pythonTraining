# In this program, assume the following input
"""
2 2
1 2
3 4
2 1
4
5
"""
import numpy as np

fileName = input("Enter a fileName containing matrix info>>")

fo = open(fileName,"r")

def createMat():
    "create matrix from file"
    format = fo.readline().strip().replace("\n","").split(" ")
    rowCnt = int(format[0])
    columnCnt = int(format[1])

    mat = np.array([])
    cnt = 0
    while cnt < rowCnt:
        line = fo.readline().strip().replace("\n","").split(" ")
        mat = np.append(mat,line)
        cnt += 1

    mat = mat.reshape(rowCnt,columnCnt)

    # convert to int
    mat = mat.astype(np.int8)

    return mat

mat1 = createMat()
mat2 = createMat()

fo.close()

print(np.dot(mat1,mat2))
