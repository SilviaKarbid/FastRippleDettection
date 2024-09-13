


class save:
        
    # def saveList(lst, d, trueStart, fileNm, label, labelInd, indSW, filtPath, trueEnd,lapse):
    #    for ind in range(len(trueStart)):
    #        listTemp = [fileNm, [labelInd,label],[indSW[d,0],indSW[d,1]],[trueStart[ind],trueEnd[ind]],lapse[ind],filtPath]
    #        lst.append(listTemp)
           
    def saveList(lst, d, trueStart, fileNm, label, labelInd, indSW, trueEnd,lapse):
       for ind in range(len(trueStart)):
           listTemp = [fileNm, labelInd,label,indSW[d,0],indSW[d,1],trueStart[ind],trueEnd[ind],lapse[ind]]
           lst.append(listTemp)
        
       return lst
