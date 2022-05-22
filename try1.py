import datetime
import json
import operator
import string
import hashlib

from sqlalchemy import null

numberOfLines = 0
numberOfGet = 0
numberOfPost = 0
f = open("http.log", "r")
w = open("result.txt", "w")

def returnMonthNumber(arg):
    switcher = {
        "Jan": 1,
        "Feb": 2,
        "Mar": 3,
        "Apr": 4,
        "May": 5,
        "Jun": 6,
        "Jul": 7,
        "Aug": 8,
        "Sep": 9,
        "Oct": 10,
        "Nov": 11,
        "Dec": 12
    }
    return switcher.get(arg)

myDict=[]

for x in f:
    for index, word in enumerate(x.split()):
        if word == '200':
            # print(x)
            if(x.split()[index-3]) == '"GET':

                tarih = x.split()[index-5]
                buyukluk = x.split()[index+1]
                year = 1000*int(tarih[8])+100*int(tarih[9]) + 10*int(tarih[10])+int(tarih[11])
                month = returnMonthNumber(tarih[4] + tarih[5] + tarih[6])
                day = 10*int(tarih[1])+int(tarih[2])
                hour = 10*int(tarih[13])+int(tarih[14])
                minute = 10*int(tarih[16])+int(tarih[17])
                second = 10*int(tarih[19])+int(tarih[20])
                date = int(datetime.datetime(year, month, day, hour, minute, second).timestamp())
                myDict.append({'time':date,'type':'GET','size':int(buyukluk)})
                numberOfGet += 1
            if(x.split()[index-3]) == '"POST':
                tarih = x.split()[index-5]
                buyukluk = x.split()[index+1]
                year = 1000*int(tarih[8])+100*int(tarih[9]) + 10*int(tarih[10])+int(tarih[11])
                month = returnMonthNumber(tarih[4] + tarih[5] + tarih[6])
                day = 10*int(tarih[1])+int(tarih[2])
                hour = 10*int(tarih[13])+int(tarih[14])
                minute = 10*int(tarih[16])+int(tarih[17])
                second = 10*int(tarih[19])+int(tarih[20])
                date = int(datetime.datetime(year, month, day, hour, minute, second).timestamp())# print(date)
                myDict.append({'time':date,'type':'POST','size':int(buyukluk)})
                numberOfPost += 1
            numberOfLines += 1

sortedDict = sorted(myDict, key=lambda x: x['time'])

totalSize = 0

for i in sortedDict:
    totalSize+=i['size']

duplicateItems = []



for count,item in enumerate(sortedDict):
    if sortedDict[count-1]['time']==sortedDict[count]['time']:
        if sortedDict[count-1]['type']==sortedDict[count]['type']:
            # duplicateItems.append(sortedDict[count])
            sortedDict[count-1]['size'] = sortedDict[count-1]['size'] + sortedDict[count]['size']
            del(sortedDict[count])
    
for count,item in enumerate(sortedDict):
    if sortedDict[count-1]['time']==sortedDict[count]['time']:
        if sortedDict[count-1]['type']==sortedDict[count]['type']:
            # duplicateItems.append(sortedDict[count])
            sortedDict[count-1]['size'] = sortedDict[count-1]['size'] + sortedDict[count]['size']
            del(sortedDict[count])

for count,item in enumerate(sortedDict):
    if sortedDict[count-1]['time']==sortedDict[count]['time']:
        if sortedDict[count-1]['type']==sortedDict[count]['type']:
            # duplicateItems.append(sortedDict[count])
            sortedDict[count-1]['size'] = sortedDict[count-1]['size'] + sortedDict[count]['size']
            del(sortedDict[count])

for count,item in enumerate(sortedDict):
    if sortedDict[count-1]['time']==sortedDict[count]['time']:
        if sortedDict[count-1]['type']==sortedDict[count]['type']:
            # duplicateItems.append(sortedDict[count])
            sortedDict[count-1]['size'] = sortedDict[count-1]['size'] + sortedDict[count]['size']
            del(sortedDict[count])

for count,item in enumerate(sortedDict):
    if sortedDict[count-1]['time']==sortedDict[count]['time']:
        if sortedDict[count-1]['type']==sortedDict[count]['type']:
            # duplicateItems.append(sortedDict[count])
            sortedDict[count-1]['size'] = sortedDict[count-1]['size'] + sortedDict[count]['size']
            del(sortedDict[count])

for count,item in enumerate(sortedDict):
    if sortedDict[count-1]['time']==sortedDict[count]['time']:
        if sortedDict[count-1]['type']==sortedDict[count]['type']:
            # duplicateItems.append(sortedDict[count])
            sortedDict[count-1]['size'] = sortedDict[count-1]['size'] + sortedDict[count]['size']
            del(sortedDict[count])

for count,item in enumerate(sortedDict):
    if sortedDict[count-1]['time']==sortedDict[count]['time']:
        if sortedDict[count-1]['type']==sortedDict[count]['type']:
            # duplicateItems.append(sortedDict[count])
            sortedDict[count-1]['size'] = sortedDict[count-1]['size'] + sortedDict[count]['size']
            del(sortedDict[count])

for count,item in enumerate(sortedDict):
    if sortedDict[count-1]['time']==sortedDict[count]['time']:
        if sortedDict[count-1]['type']==sortedDict[count]['type']:
            # duplicateItems.append(sortedDict[count])
            sortedDict[count-1]['size'] = sortedDict[count-1]['size'] + sortedDict[count]['size']
            del(sortedDict[count])


for count,item in enumerate(sortedDict):
    if sortedDict[count-1]['time']==sortedDict[count]['time']:
        if sortedDict[count-1]['type']==sortedDict[count]['type']:
            duplicateItems.append(sortedDict[count])
            # sortedDict[count-1]['size'] = sortedDict[count-1]['size'] + sortedDict[count]['size']
            # del(sortedDict[count])


count = 1

while count < len(sortedDict):
    if sortedDict[count-1]['time']==sortedDict[count]['time']:
        if sortedDict[count-1]['type']==sortedDict[count]['type']:
            duplicateItems.append(sortedDict[count])
    count+=1

# print(sortedDict[15000]['time'])

totalSizeAfter = 0

for i in sortedDict:
    totalSizeAfter+=i['size']


w.write('Total 200 requests={}\n'.format(numberOfLines))
w.write('GET={}\n'.format(numberOfGet))
w.write('POST={}\n'.format(numberOfPost))

print('Total 200 requests={}'.format(numberOfLines))
print('GET={}'.format(numberOfGet))
print('POST={}'.format(numberOfPost))
# print(duplicateItems)
print(totalSize)
print(totalSizeAfter)
print(len(sortedDict))
# for item in sortedDict:
#     print(item)

# stringOfNewList = str(newlist)
# for item in newlist:
#     w.write(str(item['time'])+'\n')
# print(newlist)
f.close()
w.close()

# print(datetime.datetime.now().timestamp())



