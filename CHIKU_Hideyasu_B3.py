# The following program is for the sentences in the file
import re
import pickle

fileName = input("Enter any fileName>>")

def createDict(fo):
    "create dict from file"
    wordlist = re.split("[ \n]",fo.read().strip())

    dict = {}
    for word in wordlist:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
    return dict


try:
    fo = open(fileName,"r")
except Exception as e:
    print(e.args[1])
else:
    dict = createDict(fo)
    fo.close()

    try:
        pickling_on = open("count.pkl","wb")
    except Exception as e:
        print(e.args[1])
    else:
        pickle.dump(dict,pickling_on)
        pickling_on.close()
