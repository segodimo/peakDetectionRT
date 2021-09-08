import time
from rt_z_scores import real_time_peak_detection


lag = 30
threshold = 4
influence = 0


arrini = [
        1.1,1,1,1.1,1,0.8,0.9,1,1.2,0.9,
        1,1,1.1,1.2,1,1.5,1,3,2,5,
        3,2,1,1,1,0.9,1,1,3, 2.6,
        4,3,3.2,2,1,1,0.8,4,4,2,
    ]

y = [
        1,1,1.1,1,0.9,1,1,1.1,1,0.9,
        1,1.1,1,1,0.9,1,1,1.1,1,1,
        1,1,1.1,0.9,1,1.1,1,1,0.9,1,
        1.1,1,1,1.1,1,0.8,0.9,1,1.2,0.9,
        1,1,1.1,1.2,1,1.5,1,3,2,5,
        3,2,1,1,1,0.9,1,1,3, 2.6,
        4,3,3.2,2,1,1,0.8,4,4,2,
        2.5,1,1,1
    ]


rtpd = real_time_peak_detection(arrini, lag, threshold, influence)

num = 0
while num < len(y):
    res = rtpd.thresholding_algo(y[num])
    print(y[num],res)
    time.sleep(0.1)
    num += 1
