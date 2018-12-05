##############################################################
## Author: Kausik Susarla
## file: getAvg.py version: 0.1
## Reads a log file as DS lists of list, calculates
## elapsed time for each operation in seconds and
## gives average of time for completed operations
##############################################################
##############################################################
##Assumptions made in this Solution :
## 1. all operations are sequential i.e. start and end
## 2. log entries with only one line are considered
##    still in operation and are excluded
## 3. only operations that are completed i.e. which
##    has both Start and End are completed.
## 4. operations that are completed will not repeat again
## 5. delimiters and spacing format in input file are standard
###############################################################
import time
from datetime import datetime, date, time, timedelta

operation = []
time = []

#--function definitions--
#--reads a file by line and creates a DS as list of lists--
def makeList(file):
    for line in open(file):
        operation.append([line.split(" ")[2], line.split(" ")[3], line.split(" ")[0].split("T")[1]])

#--reads list values calculates elapsed time for each completed operation, appends to DS list time in seconds
def getElapsedTime(mylist):
    for i in range(0, len(mylist)):
        for j in range(i+1, len(mylist)):
            if (mylist[i][0] == mylist[j][0]):
                elapsed = datetime.strptime(mylist[j][2], '%H:%M') - datetime.strptime(mylist[i][2], '%H:%M')
                elapsed_insec = elapsed.total_seconds()
                print "Operation: %s started at %s and ended at %s - has elapsed %s h:m:s" %(mylist[i][0], mylist[i][2], mylist[j][2], elapsed)
                time.append(elapsed.total_seconds())
            else:
                #print (mylist[i][0], mylist[j][0])
                #print 'NO'
                continue
    getAvgOp(time)

#--This function calculates average time took in seconds for each completed operation--
def getAvgOp(timelist):
    avg_time = sum(timelist) / len(timelist)
    print "Contents of the list are:", timelist
    print "Average time took for all completed operations in secs: ", avg_time

makeList('ops.log')
getElapsedTime(operation)
