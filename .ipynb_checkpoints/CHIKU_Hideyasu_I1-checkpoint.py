# In this program, assume the following input
"""
2,1
5,6
"""
import sys

compA = input("Enter the first complex number in the form ""2,1"">>").split(",")
compB = input("Enter the second complex number in the form ""5,6"">>").split(",")

A = complex(int(compA[0]),int(compA[1]))
B = complex(int(compB[0]),int(compB[1]))

print('{:.2f}'.format(A+B))
print('{:.2f}'.format(A-B))
print('{:.2f}'.format(A*B))
dev = A/B
print('{:.2f}'.format(dev))
print('{:.2f}'.format(abs(A)))
print('{:.2f}'.format(abs(B)))
