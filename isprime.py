
#function definitions

def IsNum(x):
    if x % 2 == 0:
        print "%d is not a prime number" %x
    elif x == 1:
        print "1 is a prime number indeed"
    else:
        print "%s is a prime number" %x

x = input('enter a number')
IsNum(x)
