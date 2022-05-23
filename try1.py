import datetime
import json
import operator
from os import remove
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

getRequests=[]
postRequests=[]

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
                getRequests.append((date,'GET',int(buyukluk)))
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
                postRequests.append((date,'POST',int(buyukluk)))
                numberOfPost += 1
            numberOfLines += 1

# sortedGet = sorted(getRequests, key=lambda x: x[0])
# sortedPost = sorted(postRequests, key=lambda x: x[0])

Gets = {}
Posts = {}

seenGet = set()
dupesGet = []

for x in getRequests:
    if x[0] in seenGet:
        dupesGet.append(x)
    else:
        seenGet.add(x[0])
        # seenGet.add(x)

seenPost = set()
dupesPost = []

for x in postRequests:
    if x[0] in seenPost:
        dupesPost.append(x)
    else:
        seenPost.add(x[0])
        # seenPost.add(x)

for x in seenGet:
    Gets[x]=[]

for x in seenGet:
    for y in getRequests:
        if y[0] == x:
            Gets[x].append(y[2])

for x in seenPost:
    Posts[x]=[]

for x in seenPost:
    for y in postRequests:
        if y[0] == x:
            Posts[x].append(y[2])

w.write('Total 200 requests={}\n'.format(numberOfLines))
w.write('GET={}\n'.format(numberOfGet))
w.write('POST={}\n'.format(numberOfPost))
for x in dupesGet:
    w.write(str(x)+'\n')

print('Total 200 requests={}'.format(numberOfLines))
print('GET={}'.format(numberOfGet))
print('POST={}'.format(numberOfPost))
print(len(dupesGet))
print(len(dupesPost))
print(len(seenPost))
print(len(seenGet))


# for x in dupesGet:
#     print(x)

for x in Gets:
    print(sum(Gets[x]))

print(len(Gets))
print(len(Posts))

f.close()
w.close()




