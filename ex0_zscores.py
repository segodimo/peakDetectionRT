import time
from rt_z_scores import real_time_peak_detection


lag = 30
threshold = 25
influence = 0


arrini = [
        10.1,10,1,10.1,10,00.8,00.9,10,10.2,00.9,
        1,10,10.1,10.2,10,10.5,10,3,20,5,
        3,20,1,10,1,00.9,10,1,30, 20.6,
        4,30,30.2,20,1,10,00.8,40,4,20,
    ]

y = [
        1,10,10.1,10,00.9,10,1,10.1,10,00.9,
        1,10.1,10,1,00.9,10,1,10.1,10,1,
        1,10,10.1,00.9,10,10.1,10,1,00.9,10,
        10.1,10,1,10.1,10,00.8,00.9,10,10.2,00.9,
        1,10,10.1,10.2,10,10.5,10,3,20,5,
        3,20,1,10,1,00.9,10,1,30, 20.6,
        4,30,30.2,20,1,10,00.8,40,4,20,
        20.5,10,1,1
    ]

rtpd = real_time_peak_detection(arrini, lag, threshold, influence)

num = 0
while num < len(y):
    res = rtpd.thresholding_algo(y[num])
    print(y[num],res)
    time.sleep(0.1)
    num += 1
