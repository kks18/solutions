from collections import Counter

filepath='apache.log'
mydict = {}
ip_list = []
#functiondefns

def createDict(line):
    ipmsg = line.split('\n')[0].split('- -')
    ip = ipmsg[0]
    ip_list.append(ip);
    action = (ipmsg[1].split('"')[1]).split('"')[0]
    if ip not in mydict.keys():
        mydict[ip] = action
    elif ip in mydict.keys():
        mydict[ip] = mydict[ip]+','+action
    #ip = ip.append(ip)
def getIPCounter():
    return Counter(ip_list)
def countKeys():
    for key, value in mydict.iteritems():
        #print (key, value)
        if ',' in value:
            print(key, len(value.split(',')))
            #continue
        else:
            print(key, 1)
        #continue


for line in open(filepath, 'r+'):
    createDict(line)

ipcount = getIPCounter()
dict_count = countKeys()
#print mydict
#print "ipcount is:", ipcount
#print "dict_count is", dict_count
#mydict_len = len(mydict)
#print "Total IPs found in log file are:", ipcount
#print "Here are the IPs found in log file\n", ip_list

#print "mydict_len", mydict_len
