import pandas as pd              
import matplotlib.pyplot as plt
from matplotlib import cm
import pandas as pd   

# Clases propias
from SignalClases import FiltSignal
from SignalClases import IndSW
from Hilbert import HilbClass
from ExtraClases import Extraclases
from Rectification import recClass
from SignalClases import saveData
from SignalClases import saveDataSR
from Wavelet import Wavelet
from SignalClases import saveWV
from SignalClases import saveWVOrg
from SignalClases import OrgSignal



numFol = 4                                                                                  # 4 carpetas diferentes 
totFiles = [8,4,8,8]                                                                        # Archivos totales de cada capeta CBX, NaCl, QUININA, TMA

numLabel = 8
srate = 10000

elcNames = ['HAD1', 'HADP2', 'HAD3', 'HADp4', 'HPD5', 'HPDp6','HPD7', 'HPDp8']


# for fold in range(numFol):
for fold in range(1,numFol):
    
    # for file in range(totFiles[fold]):
    for file in range(totFiles[fold]):
        
        filtSig,filtPath,fileName = FiltSignal.getData(fold,file)                               # Carga de data filtrada 
        
        for lb in range(numLabel):            
        # for lb in range(2,8):
            
            filtSiglb = (filtSig[lb, :]).copy() 
            dataPath = saveDataSR.getData(fold,file,lb)  
            df = pd.read_csv(dataPath)
            start = df["indFR star "].to_numpy()
            end = df["indFR end"].to_numpy()
            # start = df["indFR I"].to_numpy()
            # end = df["indFR F"].to_numpy()
           
            for fr in range(len(start)):
                signalWavelet = filtSiglb[(start[fr])-500:(end[fr])+500]               
                time,frex,mWarr = Wavelet.getWavelet(signalWavelet)
                fig, ax = plt.subplots(layout='constrained')
                CS = ax.contourf(time,frex,mWarr,cmap=cm.CMRmap)
                plt.gca().set_axis_off()
                pathIm = saveWV.getData(fold,file,lb,elcNames[lb],str(start[fr]),str(end[fr]))
                plt.close(fig)
                fig.savefig(pathIm)    