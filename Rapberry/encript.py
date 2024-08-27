def encript(value):
    f=open(r"Rapberry/sn.txt","r")
    key=str(hash(f.read()))[1:len(f.read)]
    print(key)
    out=''
    for i in range(0,len(value)):
        out+=str(int(value[i])^int(key[(i)%len(key)]))[0]
    return out