
import statistics
from scipy.signal import find_peaks


class recClass:
        
    def recThold(signal):
        
        recTresh = statistics.mean(signal) + 2*statistics.stdev(signal)
               
        return recTresh
    
    def rectSignal(signalCut,recTr):
  
        peaks, _ = find_peaks(abs(signalCut), height=recTr)
        
        return  peaks