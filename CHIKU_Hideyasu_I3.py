# In this program, assume the following input
"""
1 10 5 -1
2 -3 -1 0
"""
import numpy as np

def cos_sim(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

fileName = input("Enter a fileName containing vector info>>")

fo = open(fileName,"r")

def createVec():
    "create vector from file"
    arr = fo.readline().strip().replace("\n","").split(" ")

    vec = np.array(arr)

    # convert to int
    vec = vec.astype(np.int8)

    return vec

vec1 = createVec()
vec2 = createVec()

fo.close()

print(cos_sim(vec1,vec2))
