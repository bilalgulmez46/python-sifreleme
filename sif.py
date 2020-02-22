def sifrele(a,b):
    mesajdec=[]
    sifredec=[]
    sifrelimdec=[]
    sifrelimet=[]
    for x in(a):
        mesajdec.append(ord(x))
    for y in(b):
        sifredec.append(ord(y))
    print(mesajdec,sifredec)
    say=0
    ms=len(mesajdec)
    mp=len(sifredec)
    while say<ms:
        for y in range(0,mp):
            if(y==mp):
                y=0
            if(say==ms):
                break
            print(say,y)
            sifrelimdec.append(mesajdec[say]+sifredec[y])
            say+=1
    print(sifrelimdec)
    for met in(sifrelimdec):
        sifrelimet.append(chr(met))
    print("".join(sifrelimet))
        
    
