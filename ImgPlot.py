import matplotlib.pyplot as plt

class Plot_Signals:
    
    def __init__(self,srate) :
        self.srate = 10000        
    
    # Método para graficar las 3 señales iniciales (Origina, filtrada SW, filtrada en banda especfíca)
    def Plot3Sig(timevec,indSW,numInd,label,orgSig,SWSig,filtSig):
        
        figOrg, axsOrg = plt.subplots(3, sharex=True)
        axsOrg[0].plot(timevec[indSW[numInd,0]:indSW[numInd,1]],orgSig[label,indSW[numInd,0]:indSW[numInd,1]])    # Señal Orginal
        axsOrg[0].set_title('Original Signal')
        axsOrg[1].plot(timevec[indSW[numInd,0]:indSW[numInd,1]],SWSig[label,indSW[numInd,0]:indSW[numInd,1]])  # Senal Slow Wave
        axsOrg[1].set_title('Slow Wave filtering Signal')
        axsOrg[2].plot(timevec[indSW[numInd,0]:indSW[numInd,1]],filtSig[label,indSW[numInd,0]:indSW[numInd,1]])   # Señal band pass 250-500 Hz
        axsOrg[2].set_title('Band Pass Signal (250 -500 Hz)')
        figOrg.text(0.5, 0.04, 'Time (s)', ha='center', va='center')
        figOrg.text(0.06, 0.5, 'Amplitude (V)', ha='center', va='center', rotation='vertical')
        # plt.close(figOrg)    # no muestra la figura y lo elimina 
        plt.show()
        
    # Método para graficar señal filtrada, threshold y 0.5*threshold
    def Plot_Thold(timevec,indSW,numInd,BPSig,ampEnv,tHold,medT):
        plt.plot(timevec[indSW[numInd,0]:indSW[numInd,1]],BPSig,'b', label='Bandpass] Signal')   # Plot de señal y tiempo en el que puede estar pasando FR (señal recortada)
        plt.plot(timevec[indSW[numInd,0]:indSW[numInd,1]],ampEnv[0:],'r--',label='Hilbert Envelope')
        plt.axhline(y=tHold, color='g', linestyle='-.', label='Threshold')
        plt.axhline(y=medT, color='y', linestyle='-.', label='0.5 * Threshold')
        plt.xlabel("Time (s)")
        plt.ylabel("Amplitude (V)")
        plt.title('Envelope of filter signal')
        plt.legend()
        plt.show()
                
    
    def recSigCross(d,timevec,indSW, indStar,indEnd,recSig,recTr):
        numInd = d
        timeCut = timevec[indSW[numInd,0]:indSW[numInd,1]]

        ## primer FR encontrada 
        for i in range(len(indStar)):
            plt.figure()
            plt.plot(timevec[indSW[numInd,0]:indSW[numInd,1]],recSig)
            plt.axhline(y=recTr, color='g', linestyle='-.', label='Threshold')
            
            plt.plot(timeCut[indStar[i]],recSig[indStar[i]],'ms',markersize=8, label = str(i+1) + ' event marked')                        # Punto inicial cruce FR
            plt.plot(timeCut[indEnd[i]],recSig[indEnd[i]],'ms',markersize=8)

            plt.xlabel("Time (s)")
            plt.ylabel("Amplitude (V)")
            plt.title('Original Signal and Event marked')
            plt.legend(prop = { "size": 8 } , loc ="lower right")

            plt.xlim([timeCut[indStar[i]]-0.001,timeCut[indEnd[i]]+0.001])

