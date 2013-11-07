#!/bash/bin/python

import os
import csv
def readRawData():
    res = []
    for line in open("appid.txt"):
        a = line.split("\n")
        res.append(a[0])
    return res

def readOneCVS(cvsFile):
    res = []
    #print cvsFile
    i = 0
    for line in open(cvsFile):
        i = i + 1
        if(i <= 1):#skip line 0 & line 1
            continue
        line = line.strip('\n')
        a = line.split(",")
        #print a
        res.append(a)
    return res

def oneDayData(d, qqiData):
    c1 = 0
    c2 = 0
    for a in qqiData:
        c1 += int(a[1])
        c2 += int(a[2])

    return (d, c1, c2)

def classifyALL():
    QQiAppID = readRawData()
    qqiData = []
    qqData = []
    qqiResult = []
    qqResult = []
    for filename in os.listdir('raw'):
        print filename
        pname = filename.split('.')
        print pname
        dataList = readOneCVS('raw/' + filename)
        #print dataList
        qqiData = [i for i in dataList if i[0] in QQiAppID]
        qqData = [i for i in dataList if i[0] not in QQiAppID]
        #print qqiData
        #print qqData

        #print "c1 " + str(c1)
        #print "c2 " + str(c2)
        qqiResult.append(oneDayData(pname[0],qqiData))
        qqResult.append(oneDayData(pname[0], qqData))
        #print result
    writeResult('qqi.csv', qqiResult)
        #print qqData
    writeResult('qq.csv', qqResult)

def writeResult(result_csv, dataList):
    if not os.path.exists('result'):
        os.mkdir('result')
    filePath = 'result/' + result_csv
    writer = csv.writer(file(filePath, 'wb'))
    for e in dataList:
        writer.writerow(e)


#print filename

classifyALL()
#a = readRawData()
#print a