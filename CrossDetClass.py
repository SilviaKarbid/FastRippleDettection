
class crossDetector:
    
    def crossDet(AmpEnv,thold):     # Amplitud de fragmento de signal
        i = 0
        indPreT = []
        indPosT = []
        for i in range(0,len(AmpEnv)):
            if i==0 and AmpEnv[i] >= thold:
                indPreT.append(i)
            
            if i > 0 and AmpEnv[i] >= thold and AmpEnv[i-1] < thold: 
                indPreT.append(i)
                
            if AmpEnv[i] >= thold and AmpEnv[i-1] < thold: 
                indPreT.append(i)
                
            if i > 0 and AmpEnv[i] <= thold and AmpEnv[i-1] > thold:
                indPosT.append(i)
                       
            if i == len(AmpEnv)-1 and AmpEnv[i] > thold and AmpEnv[i-1] > thold:
                indPosT.append(i)
                
        indPreT = sorted(list(set(indPreT)))
                                                                                                                                 
        return indPreT,indPosT
    
    def detDur(preCross,postCross,ampEnv,medT):
        starInd = []
        endInd = []
        
        preCross.reverse()
        for i in range(len(preCross)):
            for b in range(preCross[i],-1,-1):          # se recorre la lista hacia la izquierda
                if ampEnv[b] <= medT:
                    starInd.append(b) 
                    break
                if ampEnv[b] == ampEnv[0]:
                    starInd.append(b)

        for i in range(len(postCross)):                      
            for c in range(postCross[i],len(ampEnv)):
                if ampEnv[c]<= medT:
                    endInd.append(c)
                    break
                if ampEnv[c] == ampEnv[len(ampEnv)-1]:  #Recorre el arreglo hacía la derecha y si se llega a un extremo pero sin cruce de threshold se toma ese extremo 
                    endInd.append(c)
                    break
        
        starIndSR = sorted(list(set(starInd)))    #Elimina elementos repetidos en las listas
        endIndSR = sorted(list(set(endInd)))

        return starIndSR,endIndSR
    
    def retOrg(starIndSR,endIndSR, indSW,numInd):
        starOrg = [x + indSW[numInd,0] for x in starIndSR]  # Regresando indices a puntos en la señal original 
        print(starOrg)

        endOrg = [x + indSW[numInd,0] for x in endIndSR]
        print(endOrg)
        
        return starOrg,endOrg
    
    def finCross(indStar, recSig,indEnd,recTr,indSW,d):
        trueStart = []
        trueEnd = []

        for i in range(len(indStar)):   
            crsStart, crsEnd = crossDetector.crossDet(recSig[indStar[i]:indEnd[i]],recTr)
            
            if len(crsStart) >= 6 and len(crsEnd) >= 6:
                trueStart.append(indStar[i] + indSW[d,0])
                trueEnd.append(indEnd[i] + indSW[d,0])
                
        return trueStart,trueEnd