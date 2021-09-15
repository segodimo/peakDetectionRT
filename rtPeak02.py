import math

def mean(data):
    if iter(data) is data:
        data = list(data)
    return sum(data)/len(data)

def peakDetect(y,t,dt,base,m):
    #ll = y[t] - y[t-dt]
    #rr = y[t] - y[t+dt]
    #print(ll,rr)
    if (y[t] - y[t-dt] > m) and (y[t] - y[t+dt] > m):
        if mean(y) < 3000:
            pk = 3500
            return pk
        else:
            pk = base
            return pk
    else:
        pk = base
        return pk

class rtPeak:
    def __init__(self, lny, dt, base, m):
        self.y = []
        self.lny = lny #num impar VALIDAR!!!
        self.t = int(math.ceil(lny/2))-1
        self.dt = dt # dt < t VALIDAR!!!
        self.base = base
        self.m = m

    def runPD(self, yrt):
        if len(self.y) < self.lny:
            self.y.append(yrt)
            return [yrt,self.base]
        if len(self.y) >= self.lny:
            self.y.append(yrt)
            self.y.pop(0)
            #------------------------
            pk = peakDetect(self.y,self.t,self.dt,self.base,self.m)
            return [self.y[self.t],pk]
            #------------------------



        


