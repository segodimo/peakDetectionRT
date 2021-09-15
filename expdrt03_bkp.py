import math

def float_list(list):
    floatList = [float(i) for i in list]
    return floatList

def mean(data):
    if iter(data) is data:
        data = list(data)
    return sum(data)/len(data)

def stdev(data, xbar=None):
    if iter(data) is data:
        data = list(data)
    if xbar is None:
        xbar = sum(data)/len(data)
    total = total2 = 0
    for x in data:
        total += (x - xbar)**2
        total2 += (x - xbar) 
    total -= total2**2/len(data)
    return math.sqrt(total/(len(data) - 1))

#----------------------------------------------
    
def peakDetect(y,t,dt,base,m):
    avgy = mean(y)
    stdy = stdev(y)
    if y[t] >= 2900:
        if abs(y[t] - avgy) > m * stdy:
            if y[t] > avgy:
                return 5000 if y[t] >= 3700 else 4000
            else:
                return 3000
        else:
            pk = base
            return pk
    else:
       return 2000

#----------------------------------------------
    
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



        



