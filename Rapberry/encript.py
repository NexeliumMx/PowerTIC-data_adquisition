def encript(value):
    f=open(r"Rapberry/sn.txt","r")
    key=str(hash(f.read()))[1:len(str(f.read()))]
    print(key)
    out=''
    for i in range(0,len(value)):
        out+=chr(ord(value[i])^ord(key[(i)%len(key)]))
    return out