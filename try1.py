numberOfLines=0
numberOfGet=0
numberOfPost=0
f = open("http.log", "r")
for x in f :
    for index,word in enumerate(x.split()):
        if word == '200':
            print(x)
            if(x.split()[index-3])=='"GET':
                print(x.split()[index-5])
                print(x.split()[index+1])
                
                numberOfGet+=1
            if(x.split()[index-3])=='"POST':
                print(x.split()[index-5])
                print(x.split()[index+1])
                
                numberOfPost+=1
            numberOfLines+=1
    

print('Total 200 requests={}'.format(numberOfLines))
print('GET={}'.format(numberOfGet))
print('POST={}'.format(numberOfPost))

f.close()