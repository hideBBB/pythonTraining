import numpy as np

# (i) create matrix
with open("iris.data","r") as fo:
    list = np.array([])
    for line in fo:
        number = line.split(",")
        del number[-1]
        if len(number) != 0 :
            FloatNumber = [float(s) for s in number]
            list = np.append(list,FloatNumber)

list = list.reshape(150,4)
print("(i)\n",list,"\n")

# (ii) count the number of specified lines
cnt = 0
for num in list:
    if num[0] > 5:
        cnt += 1

print("(ii)\n",cnt,"\n")


# (iii) report the average
multi = np.array([])
for num in list:
    multi = np.append(multi,num[0]*num[1])

avg = multi.mean()
print("(iii)\n",avg,"\n")

# (iv) what is the std deviation
print("(iv)\n",np.std(list,axis=0)[3],"\n")

# (v) find specified rows
ans = np.array([])
cnt = 0
for num in list:
    if num[2]*num[3] > 1.0:
        ans = np.append(ans,num)
        cnt += 1

ans = ans.reshape(cnt,4)
print("(v)\n",ans)

np.save("small_petal",ans)

# b = np.load("small_petal.npy")
# print(b)
