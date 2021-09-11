import math

def peakDetect(y,t,dt,base):
    if y[t] > y[t-dt] and y[t] > y[t+dt]:
        pk = y[t]
        return pk
    else:
        pk = base
        return pk

class rtPeak:
    def __init__(self, lny, dt, base):
        self.y = []
        self.lny = lny #num impar VALIDAR!!!
        self.t = int(math.ceil(lny/2))-1
        self.dt = dt # dt < t VALIDAR!!!
        self.base = base

    def runPD(self, yrt):
        if len(self.y) < self.lny:
            self.y.append(yrt)
            return [yrt,0]
        if len(self.y) >= self.lny:
            self.y.append(yrt)
            self.y.pop(0)
            #------------------------
            pk = peakDetect(self.y,self.t,self.dt,self.base)
            return [yrt,pk]
            #------------------------



        
