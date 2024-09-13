
import statistics


class recClass:
        
    def recClassThre(Signal):
        recSig = abs(Signal)
        recTr = 2*statistics.stdev(recSig)
        
        return recSig,recTr
    