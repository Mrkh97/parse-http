i=1
f = open("http.log", "r")
for x in f :
    for word in x.split():
        if word == '200':
            print(x)
            i+=1
    

print(i)