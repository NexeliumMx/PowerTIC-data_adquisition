def encript(value):
    f=open(r"Rapberry/sn.txt","r")
    key=str(hash(str(f.read())))
    
    out=''
    for i in range(0,len(value)):
        out+=chr(ord(value[i])^ord(key[(i)%len(key)]))
    return out
