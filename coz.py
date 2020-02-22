def sifrecoz(sa,sb):
    sifrelimesajdec=[]
    sifrelipasdec=[]
    cozulmus=[]
    comet=[]
    for xs in(sa):
        sifrelimesajdec.append(ord(xs))
    for ys in (sb):
        sifrelipasdec.append(ord(ys))
    print(sifrelimesajdec,sifrelipasdec)
    say=0
    ms=len(sifrelimesajdec)
    mp=len(sifrelipasdec)
    while say<ms:
        for ysa in range(0,mp):
            if(ysa==0):
                ysa=0
            if(say==ms):
                break
            print(say,ysa)
            cozulmus.append(sifrelimesajdec[say]-sifrelipasdec[ysa])
            say+=1
    print(cozulmus)
    for dte in(cozulmus):
        comet.append(chr(dte))
    print("".join(comet))
            
            
            
    
    
    
        
