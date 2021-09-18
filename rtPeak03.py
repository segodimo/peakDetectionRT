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
    
def peakDetect(y,t,dt,base,thd):
    avgy = mean(y)
    stdy = stdev(y)
    lmx = avgy+stdy
    lmn = avgy-stdy
    th = (lmx * thd/10000)+lmx
    #lrms = rms*54.5
    #if y[t] >= (avgy+stdy):
    if y[t] >= th:
        pd1 = y[t]
    else:
        pd1 = base
    return pd1,avgy,lmx,lmn,th
    #return y[t], ysm[t], avgy, avgy+stdy
    # if y[t] >= 2900:
    #     if (y[t] - y[t-dt] > thd) and (y[t] - y[t+dt] > thd):
    #         return 5000 if y[t] >= 3700 else 4000
    #     else:
    #         pk = base
    #         return pk
    # else:
    #    return 2000
#----------------------------------------------
    
class rtPeak:
    def __init__(self, lny, dt, base, thd):
        self.y = []
        self.lny = lny #num impar VALIDAR!!!
        self.t = int(math.ceil(lny/2))-1
        self.dt = dt # dt < t VALIDAR!!!
        self.base = base
        self.thd = thd
        self.pk = base


    def runPD(self, yrt):
        if len(self.y) < self.lny+1:
            self.y.append(yrt)
            return [yrt,self.base]
        if len(self.y) >= self.lny+1:
            self.y.append(yrt)
            self.y.pop(0)
            #------------------------
            #ysm = [ ((self.y[i]+self.y[i+1])/2) for i in range(len(self.y)-1)]
            #------------------------
            pk = peakDetect(
                self.y,
                #ysm,
                self.t,
                self.dt,
                self.base,
                self.thd,
                )
            return (self.y[self.t],pk)
            #------------------------ 



        



