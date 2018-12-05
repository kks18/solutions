a = [1, 3, 8, 11, 24]

print "Values in list are:", a

val = int( raw_input("Enter a value:"))
for i in range(0, len(a)):
    for j in range(i+1, len(a)):
        if a[i] + a[j] == val:
            print "values in index that equals to %d are: %d, %d" %(val, a[i], a[j])
            print "index values are: ", i, j
        else:
            retval = 0
if retval == 0:
    print "neither index values of list equals %d please try again" %val
