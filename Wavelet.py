import numpy as np 
from scipy.fft import fft, ifft
import math

class Wavelet:
    
    def __init__(self,srate) :
        self.srate = 10000  
    
    def getWavelet(data):
        min_freq = 0
        max_freq = 510
        num_freq = 510   #320 si se quiere resolución de una frecuencia 
        srate = 10000
        
        frex = np.linspace(min_freq,max_freq, num = num_freq)  
        timevec = np.arange(-0.1,0.1+1/srate,1/srate)  # Vector de 6001 pnt       
        halk = math.floor(len(timevec)/2)
        szD = len(data)  # Longitud de señal 
        pntC = szD + len(timevec)-1
        mWarr = np.zeros((num_freq,szD))
        dataFT = fft(data,pntC)
           
        for i in range(num_freq):
            cmw = np.exp(1j * 2 * np.pi * frex[i] * timevec) * np.exp(-4 * np.log(2) * timevec ** 2 / 0.009 ** 2)   # crando wavelet compleja 
            
            cmwX = fft(cmw,pntC)
            cmwX = cmwX/np.max(cmwX)
            
            conSW = ifft(dataFT * cmwX)
            conSW = conSW[halk:szD+halk]
            
            conSWpow = np.abs(conSW)**2
            
            mWarr[i,:] = conSWpow
            
        spmW = mWarr.shape
        time = np.arange(0,spmW[1],1)*1/10000
        
        return time,frex,mWarr

