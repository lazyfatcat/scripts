#!/bash/bin/python

import csv
import os

def getCountryCode():
    countryCodesList=[]
    i = 0
    for line in open("country_code.csv"):
        i = i + 1
        if(i <= 1):#skip line 0 & line 1
            continue
        
        a,b,c,d,e= line.split(",")
        countryCodesList.append(d)
    #print a,b,c,d,e
    codes = list(set(countryCodesList))
    return sorted(codes)
    
def readRawData():
    res = []
    for line in open("MobileRegister.csv"):
        a = line.split(",")
        res.append(a)
    return res
        #print a

def classifyByCountryCode():
    ccodes = getCountryCode()
    data = readRawData()
    if not os.path.exists('result'):
        os.mkdir('result')
    filePath = 'result/a.csv'
    writer = csv.writer(file(filePath, 'wb'))
    filterList = []
    for code in ccodes:
        e = [i for i in data if i[4].startswith(code)]
        filterList = filterList + e
        for item in e:
            temp = list(item)
            temp.append(code)
            writer.writerow(tuple(temp))
    #leftData = [i for i in data if i not in filterList]
    #print leftData

data = classifyByCountryCode()
#print data
#e = [i for i in data if i[4].startswith('1')]
#writer = csv.writer(file('your.csv', 'wb'))
#for item in e:
#    writer.writerow(item)
