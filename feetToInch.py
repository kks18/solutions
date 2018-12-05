myft = 5
myinch = 9

def feetTocenti (myft,myinch):
  myfloat = myft * 30.48
  myfloat = myfloat + myinch * 2.54
  return myfloat
mylength = feetTocenti(myft,myinch)
print "My height in cm is %.2f" %mylength
