# In this program, assume the following input
# Sample file I4 has the following inputs
"""
1 10 5 -1
2 -3 -1 0
"""
import pandas as pd

# s = pd.Series([1,2,3,4],index = ["a","b","c","d"])
#
# print(s[:3])

data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=["name","age"])

print(df)

d = {'one' : pd.Series([1, 2, 3,4], index=['a', 'b', 'c', 'd']),
   'two' : pd.Series([1, 2, 3], index=['a', 'b', 'c'])}

df = pd.DataFrame(d)
print(df)

print(df["two"])


d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)

# Adding a new column to an existing DataFrame object with column label by passing new series

print ("Adding a new column by passing as Series:")
df['three']=pd.Series([10,20,30],index=['a','b','c'])
print(df)

print ("Adding a new column using the existing columns in DataFrame:")
df['four']=df['two']+df['three']

print(df)

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print(df)
print(df.loc['b'])


df = pd.DataFrame([[1, 2], [3, 4]], columns = ['a','b'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a','b'])

df = df.append(df2)

# Drop rows with label 0
df = df.drop(0)

print(df)



# import numpy as np
#
# def cos_sim(v1, v2):
#     return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
#
# fileName = input("Enter a fileName containing vector info>>")
#
# fo = open(fileName,"r")
#
# def createVec():
#     "create vector from file"
#     arr = fo.readline().strip().replace("\n","").split(" ")
#
#     vec = np.array(arr)
#
#     # convert to int
#     vec = vec.astype(np.int8)
#
#     return vec
#
# vec1 = createVec()
# vec2 = createVec()
#
# fo.close()
#
# print(cos_sim(vec1,vec2))
