numberOfLines=1
f = open("http.log", "r")
for x in f :
    for index,word in enumerate(x.split()):
        if word == '200':
            print(x)
            print(x.split()[index-3])
            print(x.split()[index+1])
            numberOfLines+=1
    

print(numberOfLines)

f.close()