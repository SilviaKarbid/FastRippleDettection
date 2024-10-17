## Clases for threshold detection 


import numpy as np


class Extraclases:
    
    def __init__(self, envelope, thold, midThold):
        self.envelope = envelope
        self.thold = thold
        self.midThold = midThold
    
    def thresholdCrossing(self):
        pre = []
        post = []
        
        signal = self.envelope-self.thold 
        
        crossing = np.where(np.diff(np.sign(signal)))[0] 
    
        sgnCross = (np.sign(signal[crossing])).astype(int)
            
       
        for i in range(crossing.size-1):
            if ((sgnCross[i]== -1) and (sgnCross[i+1]== 1)):  # Detección de solo ondas cerradas 
                pre.append(crossing[i])
                post.append(crossing[i+1]+1)   # +1 ya que el signo +1 que se guarda es el signo anterior al cruce (1 1 -1 -1) -> en este caso se guarda el 1 para así cerrar la onda en el siguiente instante de muestreo 

        pre = np.array(pre)
        post = np.array(post)
        # print('pre inital threshold:',pre)
        # print('post inital threshold:',post)
        
        return pre,post
      
    
    def midThresCross(self):
        tempre = 0
        tempost= 0
        preMidT = []
        postMidT = []
        
        pre, post = self.thresholdCrossing()
        if len(pre) == 0:
            return preMidT,postMidT
        
        else:
            envMT = self.envelope - self.midThold
    
            for ind in range(pre.size):
                
                for i in range(pre[ind],1,-1):
                    if (np.sign(envMT[i+1]) - np.sign(envMT[i])) > 1 :
                        tempre = i
                        break
                    else:
                        tempre = 0 
                    
                    
                for i in range(post[ind], envMT.size,1):
                    if (np.sign(envMT[i]) - np.sign(envMT[i-1])) < -1 :
                        tempost = i
                        break
                    else:
                        tempost = 0
                        
                if tempre != 0 and tempost !=0:
                    preMidT.append(tempre)
                    postMidT.append(tempost)
                    
            preMidT = list(dict.fromkeys(preMidT))
            postMidT = list(dict.fromkeys(postMidT))
            
            preMidT = np.array(preMidT)
            postMidT = np.array(postMidT)
            
            # print('pre mid threshold:',preMidT)
            # print('post mid threshold:',postMidT)
            
            return preMidT, postMidT     
     
    def cross6Ms(self):
        
        preCross6 = []
        postCross6 = []
        
        preMidT,postMidT = self.midThresCross()
        if len(preMidT) == 0:
            return preCross6,postCross6
            
        else:            
            for i in range(preMidT.size):
                if postMidT[i]-preMidT[i] > 60:     ## 0.006 ms -> 60 muestras
                    preCross6.append(preMidT[i])
                    postCross6.append(postMidT[i])  
                    
                    # print('pre 6cross threshold:',preCross6)
                    # print('post 6cross threshold:',postCross6)
            return preCross6, postCross6
                

        
    def cross10ms(self):
               
        preCross, postCross = self.cross6Ms()
        
        if len(preCross) == 0:
           return preCross,postCross
       
        else:           
            # Listas para almacenar los nuevos arreglos filtrados
            nuevo_pre = [preCross[0]]  # Añadir el primer valor de pre
            nuevo_post = []

            # Iterar sobre los índices y comparar post[i] con pre[i+1]
            for i in range(len(preCross) - 1):
                if abs(preCross[i+1] - postCross[i]) >= 100:  # Comparar fin de evento actual con el inicio del siguiente
                    nuevo_post.append(postCross[i])  # Mantener post actual
                    nuevo_pre.append(preCross[i+1])  # Mantener pre del siguiente evento

            # Añadir el último valor de post, ya que no tiene más eventos que comparar
            nuevo_post.append(postCross[-1])

            # Convertir las listas en arrays de numpy
            nuevo_pre = np.array(nuevo_pre)
            nuevo_post = np.array(nuevo_post)
            
            return nuevo_pre, nuevo_post
        