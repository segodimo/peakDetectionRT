import time
from persistentTopology import Peak, get_persistent_homology

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

startidx = 0
Peak = Peak(startidx)
Peak.get_persistence(arrini)
res = get_persistent_homology(y)

print(res)


# num = 0
# while num < len(y):
#     res = get_persistent_homology(y[num])
#     print(y[num],res)
#     time.sleep(0.1)
#     num += 1
