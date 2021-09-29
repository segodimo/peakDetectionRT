import math
import time

def mean(data):
    if iter(data) is data:
        data = list(data)
    return sum(data)/len(data)

def peakDetect(y,t,dt,thld,tml,tmm,tmh):
    if y[t] >= thld[1] and y[t] < thld[2]:
        tmm += 1
        return (None,[tml,tmm,tmh])
    elif y[t] >= thld[1] and y[t] >= thld[2]:
        tmh += 1
        return (None,[tml,tmm,tmh])
    elif y[t] < thld[0]:
        tml += 1
        return (None,[tml,tmm,tmh])
    else:
        ver = [tmm,tmh,tml]
        if (tmm > 0 or tmh > 0) and tmm > tmh:
            return ("J",ver)
        elif (tmm > 0 or tmh > 0) and tmh > tmm:
            return ("U",ver)
        elif tml > 0:
            return ("M",ver)
        else:
            return (None,[0,0,0])
    
    
class rtPeak:
    def __init__(self,lny,dt,thld):
        self.y = []
        self.lny = lny #num impar VALIDAR!!!
        self.t = int(math.ceil(lny/2))-1
        self.dt = dt # dt < t VALIDAR!!!
        self.thld = thld
        self.tml = self.tmm = self.tmh = 0
    def runPD(self, yrt):
        if len(self.y) < self.lny:
            self.y.append(yrt)
            return (None,None) 
        if len(self.y) >= self.lny:
            self.y.append(yrt)
            self.y.pop(0)
            #------------------------
            pk = peakDetect(self.y, self.t, self.dt, self.thld, self.tml, self.tmm, self.tmh)
            if pk[0]:
                self.tml = self.tmm = self.tmh = 0
                return pk
            else:
                self.tml = pk[1][0]
                self.tmm = pk[1][1]
                self.tmh = pk[1][2]
                return pk

            # if self.y[self.t] >= self.thld[1] and self.y[self.t] < self.thld[2]: self.tmm += 1
            # elif self.y[self.t] >= self.thld[1] and self.y[self.t] >= self.thld[2]: self.tmh += 1
            # elif self.y[self.t] < self.thld[0]: self.tml += 1
            # else:
            #     ver = (self.tmm,self.tmh,self.tml)
            #     if (self.tmm > 0 or self.tmh > 0) and self.tmm > self.tmh: res = ("J",ver)
            #     elif (self.tmm > 0 or self.tmh > 0) and self.tmh > self.tmm: res = ("U",ver)
            #     elif self.tml > 0: res = ("M",ver)
            #     else: res = None 
            #     self.tml = self.tmm = self.tmh = 0
            #     return res
            #------------------------







