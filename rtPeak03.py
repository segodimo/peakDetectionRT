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
    
def peakDetect(y,ysm,t,dt,base,threshold):
    avgy = mean(ysm)
    stdy = stdev(ysm)
    if y[t] >= (avgy+stdy) and (avgy+stdy) > 2840:
        pd1 = y[t]
    else:
        pd1 = base
    return (avgy+stdy),pd1,avgy
    #return y[t], ysm[t], avgy, avgy+stdy
    # if y[t] >= 2900:
    #     if (y[t] - y[t-dt] > threshold) and (y[t] - y[t+dt] > threshold):
    #         return 5000 if y[t] >= 3700 else 4000
    #     else:
    #         pk = base
    #         return pk
    # else:
    #    return 2000

def smooth(y):
    # ysm = []
    ysm = [ ((y[i]+y[i+1])/2) for i in range(len(y)-1)]
    # for i in range(len(y)-1):
    #     my = (y[i]+y[i+1])/2
    #     ysm.append(my)
    return ysm
#----------------------------------------------
    
class rtPeak:
    def __init__(self, lny, dt, base, threshold):
        self.y = []
        self.lny = lny #num impar VALIDAR!!!
        self.t = int(math.ceil(lny/2))-1
        self.dt = dt # dt < t VALIDAR!!!
        self.base = base
        self.threshold = threshold

    def runPD(self, yrt):
        if len(self.y) < self.lny+1:
            self.y.append(yrt)
            return [yrt,self.base]
        if len(self.y) >= self.lny+1:
            self.y.append(yrt)
            self.y.pop(0)
            #------------------------
            ysm = smooth(self.y)
            #------------------------
            pk = peakDetect(self.y,ysm,self.t,self.dt,self.base,self.threshold)
            return (self.y[self.t],pk)
            #------------------------



        



