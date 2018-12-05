import sys
from sys import argv
from os.path import exists

#function definitions
def logParse(line):
    #do something here
    split_line = line.split()
    return {
    split_line[0]: split_line[5]+' '+split_line[6]
    }

def logRead(logfile):
    #read file by print_line
    for line in logfile:
        #print line
        linedict = logParse(line)
        print linedict

script, in_file = argv
if not len(sys.argv) > 1:
    print "need more than one arg\nUsage: <script> <logfile>"
    sys.exit(1)

try:
    logfile = open(in_file, 'r+')
except IOError:
    print "file doesnt exist"
    print (__doc__)
    sys.exit(1)

logRead(logfile)
logfile.close()
