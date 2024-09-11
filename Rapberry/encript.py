def encript(value):
    f=open(r"vals/sn.txt","r")
    key=str(hash(str(f.read()).strip('\n')))
    
    out=''
    for i in range(0,len(value)):
        out+=chr(ord(value[i])^ord(key[(i)%len(key)]))
    return out
