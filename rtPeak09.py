import math
import time

def mean(data):
    if iter(data) is data:
        data = list(data)
    return sum(data)/len(data)


def peakDetectRt(y,dt,thld,tml,tmm,tmh,kys,tthm):
    if y > thld[1]:
        tmm += 1
        return (None,[tml,tmm,tmh])
    elif y < thld[0]:
        tml += 1
        return (None,[tml,tmm,tmh])
    else:
        ver = [tmm,tmh,tml]
        if tmm > 0 and tmm < tthm:
            return (kys[1],ver)
        elif tmm > 0 and tmm > tthm:
            return (kys[2],ver)
        elif tml > 0:
            return (kys[0],ver)
        else:
            return (None,[0,0,0])
    
    
class rtPeak:
    
    def __init__(self,lny,dt,thld,kys,tthm):
        self.yl = []
        self.lny = 2
        self.t = int(math.ceil(lny/2))-1
        self.dt = dt # dt < t VALIDAR!!!
        self.thld = thld
        self.tml = self.tmm = self.tmh = 0
        self.kys = kys
        self.tthm = tthm


    def runPdRt(self, y):
        if len(self.yl) < self.lny:
            self.yl.append(y)
            return (None,[0,0,0])
        if len(self.yl) >= self.lny:
            self.yl.append(y)
            self.yl.pop(0)
            ys = mean(self.yl)
            
            pk = peakDetectRt(ys, self.dt, self.thld, self.tml, self.tmm, self.tmh, self.kys,self.tthm)
            if pk[0]:
                self.tml = self.tmm = self.tmh = 0
                return pk
            else:
                self.tml = pk[1][0]
                self.tmm = pk[1][1]
                self.tmh = pk[1][2]
                return pk










