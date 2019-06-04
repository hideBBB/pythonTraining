# In this program, assume the following input
# Sample file B4 has the following inputs
"""
2,1
5,6
"""
fileName = input("Enter any fileName>>")

with open(fileName,"r") as fo:
    compA = fo.readline().strip().replace("\n","").split(",")
    compB = fo.readline().strip().replace("\n","").split(",")

A = complex(int(compA[0]),int(compA[1]))
B = complex(int(compB[0]),int(compB[1]))

print('{:.2f}'.format(A+B))
print('{:.2f}'.format(A-B))
print('{:.2f}'.format(A*B))
dev = A/B
print('{:.2f}'.format(dev))
print('{:.2f}'.format(abs(A)))
print('{:.2f}'.format(abs(B)))
