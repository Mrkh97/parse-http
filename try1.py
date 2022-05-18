import datetime

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


for x in f:
    for index, word in enumerate(x.split()):
        if word == '200':
            # print(x)
            if(x.split()[index-3]) == '"GET':

                tarih = x.split()[index-5]
                date = datetime.datetime(1000*int(tarih[8])+100*int(tarih[9])
                                         + 10*int(tarih[10])+int(tarih[11]), returnMonthNumber(tarih[4]+tarih[5]
                                                                                               + tarih[6]), 10*int(tarih[1])+int(tarih[2]), 10*int(tarih[13])+int(tarih[14]), 10*int(tarih[16])+int(tarih[17]), 10*int(tarih[19])+int(tarih[20]))
                print(date)
                w.write("GET"+"\n")
                # print(x.split()[index-5])
                w.write(tarih+"\n")

                # print((10*int(tarih[1])+int(tarih[2])),returnMonthNumber(tarih[4]+tarih[5]
                # +tarih[6]),1000*int(tarih[8])+100*int(tarih[9])
                # +10*int(tarih[10])+int(tarih[11]),10*int(tarih[13])+int(tarih[14]),10*int(tarih[16])+int(tarih[17])
                # ,10*int(tarih[19])+int(tarih[20]))
                # print(x.split()[index+1])
                w.write(x.split()[index+1]+"\n")

                numberOfGet += 1
            if(x.split()[index-3]) == '"POST':
                tarih = x.split()[index-5]
                date = datetime.datetime(1000*int(tarih[8])+100*int(tarih[9])
                                         + 10*int(tarih[10])+int(tarih[11]), returnMonthNumber(tarih[4]+tarih[5]
                                                                                               + tarih[6]), 10*int(tarih[1])+int(tarih[2]), 10*int(tarih[13])+int(tarih[14]), 10*int(tarih[16])+int(tarih[17]), 10*int(tarih[19])+int(tarih[20]))
                print(date)
                w.write("POST"+"\n")
                # print(x.split()[index-5])
                w.write(x.split()[index-5]+"\n")
                # print(x.split()[index+1])
                w.write(x.split()[index+1]+"\n")

                numberOfPost += 1
            numberOfLines += 1


w.write('Total 200 requests={}\n'.format(numberOfLines))
w.write('GET={}\n'.format(numberOfGet))
w.write('POST={}\n'.format(numberOfPost))

print('Total 200 requests={}'.format(numberOfLines))
print('GET={}'.format(numberOfGet))
print('POST={}'.format(numberOfPost))


f.close()
w.close()
