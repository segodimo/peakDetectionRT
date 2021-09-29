import math
import time

def mean(data):
    if iter(data) is data:
        data = list(data)
    return sum(data)/len(data)

def printKey(key):
    print(key)
    time.sleep(500/1000)

def peakDetect(y,t,dt,thm,thh,tt,tp):
    if y[t] >= thm and y[t] < thh and (y[t+dt] < thh):
        printKey("J")
        return 1
    elif y[t] >= thm and y[t] >= thh and (y[t+dt] >= thh):
        printKey("U")
        return 2
    else:
        return 0
    

class rtPeak:
    def __init__(self, lny, dt, thm, thh, tm):
        self.y = []
        self.tt = []
        self.lny = lny #num impar VALIDAR!!!
        self.t = int(math.ceil(lny/2))-1
        self.dt = dt # dt < t VALIDAR!!!
        self.thm = thm
        self.thh = thh
        self.tm = tm

    def runPD(self, yrt, tp, tm):
        if len(self.y) < self.lny:
            self.y.append(yrt)
            self.tt.append(tp)
            return 0
        if len(self.y) >= self.lny:
            self.y.append(yrt)
            self.tt.append(tp)
            self.y.pop(0)
            self.tt.pop(0)
            #------------------------
            pk = peakDetect(self.y,self.t,self.dt,self.thm,self.thh,self.tt,tm)
            return pk
            #------------------------