class tDetClass:
    
    def timeLen(starOrg,endOrg,timevec):
        finStart = []
        finEnd = []
        lapse = []
        

        for i in range(len(endOrg)):
            # print(timevec[endOrg[i]],timevec[starOrg[i]])
            
            if timevec[endOrg[i]]-timevec[starOrg[i]] > 0.006:
                finStart.append(starOrg[i])
                finEnd.append(endOrg[i])
                lapse.append(timevec[endOrg[i]]-timevec[starOrg[i]])
                
         
        return finStart,finEnd, lapse       
            
    def time10Len(finStart,finEnd,timevec):
        lapse = []
        lapStar = []
        lapEnd = []
        ind = 0

        lapStar.append(finStart[ind])

        for ind in range(len(finStart)):
            if len(finStart) > 1 and ind < len(finStart)-1:
                if(timevec[finStart[ind+1]]-timevec[finEnd[ind]]) > 0.01:
                    lapStar.append(finStart[ind+1])
                    lapEnd.append(finEnd[ind])
        
        lapEnd.append(finEnd[-1])
                
        for t in range(len(lapEnd)):
            dur = timevec[lapEnd[t]]-timevec[lapStar[t]]
            lapse.append(round(dur,3))
            
        return lapStar,lapEnd,lapse
    
