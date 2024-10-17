import numpy as np
from scipy.signal import hilbert
import statistics


class HilbClass:
        
    def HBSig(Signal):
        hilbTrans = hilbert(Signal)
        ampEnv = np.abs(hilbTrans)
        meanHil = statistics.mean(ampEnv)
        stdEnv = statistics.stdev(ampEnv)
        thold = meanHil + 3 * stdEnv
        medT = thold/2
        
        return ampEnv, thold,medT
    