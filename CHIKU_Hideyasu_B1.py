import sys

StrYear = input("Enter any year>>")
IntYear = int(StrYear)

devFour = IntYear % 4
devHundred = IntYear % 100
devFHundred = IntYear % 400

if devFour == 0 and (devHundred != 0 or devFHundred == 0) :
    print(StrYear + " is a leap year")
else :
    print(StrYear + " is not a leap year")
