import math
import time

def mean(data):
    if iter(data) is data:
        data = list(data)
    return sum(data)/len(data)


def peakDetectRt(y,dt,thld,tml,tmm,tmh,kys):
    if y >= thld[1] and y < thld[2]:
        tmm += 1
        return (None,[tml,tmm,tmh])
    elif y >= thld[1] and y >= thld[2]:
        tmh += 1
        return (None,[tml,tmm,tmh])
    elif y < thld[0]:
        tml += 1
        return (None,[tml,tmm,tmh])
    else:
        ver = [tmm,tmh,tml]
        if (tmm > 0 or tmh > 0) and tmm > tmh:
            return (kys[1],ver)
        elif (tmm > 0 or tmh > 0) and tmh > tmm:
            return (kys[2],ver)
        elif tml > 0:
            return (kys[0],ver)
        else:
            return (None,[0,0,0])
    
    
class rtPeak:
    
    def __init__(self,lny,dt,thld,kys):
        self.y = []
        self.lny = lny #num impar VALIDAR!!!
        self.t = int(math.ceil(lny/2))-1
        self.dt = dt # dt < t VALIDAR!!!
        self.thld = thld
        self.tml = self.tmm = self.tmh = 0
        self.kys = kys


    def runPdRt(self, y):
        pk = peakDetectRt(y, self.dt, self.thld, self.tml, self.tmm, self.tmh, self.kys)
        if pk[0]:
            self.tml = self.tmm = self.tmh = 0
            return pk
        else:
            self.tml = pk[1][0]
            self.tmm = pk[1][1]
            self.tmh = pk[1][2]
            return pk










w