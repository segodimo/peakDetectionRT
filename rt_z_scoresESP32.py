import statistics_indepfunc as msf

def float_list(list):
    floatList = [float(i) for i in list]
    return floatList

class real_time_peak_detection():
    def __init__(self, array, lag, threshold, influence):
        self.y = list(array)
        self.length = len(self.y)
        self.lag = lag
        self.threshold = threshold
        self.influence = influence
        self.signals = [0] * len(self.y)
        self.filteredY = float_list(self.y)
        self.avgFilter = [0] * len(self.y)
        self.stdFilter = [0] * len(self.y)
        self.avgFilter[self.lag - 1] = msf.mean(self.y[0:self.lag])
        self.stdFilter[self.lag - 1] = msf.stdev(self.y[0:self.lag])

    def thresholding_algo(self, new_value):
        self.y.append(new_value)
        i = len(self.y) - 1
        self.length = len(self.y)
        if i < self.lag:
            return 0
        elif i == self.lag:
            self.signals = [0] * len(self.y)
            self.filteredY = float_list(self.y)
            self.avgFilter = [0] * len(self.y)
            self.stdFilter = [0] * len(self.y)
            self.avgFilter[self.lag - 1] = msf.mean(self.y[0:self.lag])
            self.stdFilter[self.lag - 1] = msf.stdev(self.y[0:self.lag])
            return 0

        self.signals += [0]
        self.filteredY += [0]
        self.avgFilter += [0]
        self.stdFilter += [0]

        if abs(self.y[i] - self.avgFilter[i - 1]) > self.threshold * self.stdFilter[i - 1]:
            if self.y[i] > self.avgFilter[i - 1]:
                self.signals[i] = 1
            else:
                self.signals[i] = -1

            self.filteredY[i] = self.influence * self.y[i] + (1 - self.influence) * self.filteredY[i - 1]
            self.avgFilter[i] = msf.mean(self.filteredY[(i - self.lag):i])
            self.stdFilter[i] = msf.stdev(self.filteredY[(i - self.lag):i])
        else:
            self.signals[i] = 0
            self.filteredY[i] = self.y[i]
            self.avgFilter[i] = msf.mean(self.filteredY[(i - self.lag):i])
            self.stdFilter[i] = msf.stdev(self.filteredY[(i - self.lag):i])

        return self.signals[i]
