import math
import numpy as np

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

def peakDetect(y, lag, threshold, influence):
    signals = [0]*len(y)
    filteredY = float_list(y)
    avgFilter = [0]*len(y)
    stdFilter = [0]*len(y)
    avgFilter[lag - 1] = mean(y[0:lag])
    stdFilter[lag - 1] = stdev(y[0:lag])
    for i in range(lag, len(y)):
        if abs(y[i] - avgFilter[i-1]) > threshold * stdFilter [i-1]:
            if y[i] > avgFilter[i-1]:
                signals[i] = 1
            else:
                signals[i] = -1

            filteredY[i] = influence * y[i] + (1 - influence) * filteredY[i-1]
            avgFilter[i] = mean(filteredY[(i-lag+1):i+1])
            stdFilter[i] = stdev(filteredY[(i-lag+1):i+1])
        else:
            signals[i] = 0
            filteredY[i] = y[i]
            avgFilter[i] = mean(filteredY[(i-lag+1):i+1])
            stdFilter[i] = stdev(filteredY[(i-lag+1):i+1])

    #return signals,avgFilter,stdFilter
    return signals[i]

class rtPeak:
    def __init__(self, lny, dt, base, m):
        self.y = []
        self.lny = lny #num impar VALIDAR!!!
        self.t = int(math.ceil(lny/2))-1
        self.dt = dt # dt < t VALIDAR!!!
        self.base = base
        self.m = m
        self.lag = 2
        self.threshold = 2800
        self.influence = 0

    def runPD(self, yrt):
        if len(self.y) < self.lny:
            self.y.append(yrt)
            return [yrt,self.base]
        if len(self.y) >= self.lny:
            self.y.append(yrt)
            self.y.pop(0)
            #------------------------
            pk = peakDetect(self.y,self.lag,self.threshold,self.influence)
            return [self.y[self.t],pk]
            #------------------------



        


