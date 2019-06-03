import sys

fo = open("matrix.txt","r")

def createMat():
    "create matrix from file"
    format = fo.readline().strip().replace("\n","").split(" ")
    rowCnt = int(format[0])
    columnCnt = int(format[1])

    mat = []
    cnt = 0
    while cnt < rowCnt:
        line = fo.readline().strip().replace("\n","").split(" ")
        mat.append(line)
        cnt += 1

    return mat,rowCnt,columnCnt

mat1Ele = createMat()
mat2Ele = createMat()
mat1 = mat1Ele[0]
mat2 = mat2Ele[0]
fo.close()

if mat1Ele[2] != mat2Ele[1]:
    # validation
    print("invalid matrix combination")
else:
    ans = []
    for i in range(mat1Ele[1]):
        line = []
        for j in range(mat2Ele[2]):
            sum = 0
            for k in range(mat1Ele[2]):
                sum += int(mat1[i][k])*int(mat2[k][j])
            line.append(sum)
        ans.append(line)
    print(ans)
