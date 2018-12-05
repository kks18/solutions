import re
from collections import defaultdict
from collections import Counter

afile = 'apache.log'
def TotalAccessCount(afile):
    from os.path import exists
    if not exists(afile):
        print "file doesnt exist"
        quit
    else:
        #access_file = open(afile, 'r+')
        print "file exists, opening in read mode"
        myregex = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        myregex2 = r'".*?"'

        with open(afile) as f:
            l = f.read()
            occurance = {}
            #occurance = dict(ip_list, action_list)
            #for k, v in l:
            #    occurence.setdefault(re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', l), []).append(re.findall(r'.*(".*?")', l))
            occurance = dict(re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*(".*?")', l))
            ip_list = re.findall(myregex,l)
            action_list = re.findall(myregex2,l)
            ip_count = Counter(ip_list)
            for ip, hit in ip_count.items():
                #print("IP Address " + "=> " + str(ip) + " " + "Count "  + "=> " + str(hit))
                print " IP Address "+str(ip)+" was found "+str(hit)+" times"

            #occurance = dict(re.findall(myregex,l), re.findall(myregex2,l))
            #print "line is %s\n" %l
            print "IPs in file are: ",ip_list
            print "Actions in file are: ",action_list
            #print "Dict is: ",occurance
            for key, value in occurance.iteritems():
                print key, value


TotalAccessCount(afile)
