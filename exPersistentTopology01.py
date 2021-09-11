import time
from persistentTopology import Peak, get_persistent_homology

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
Peak.get_persistence(y)
res = get_persistent_homology(y)

num = 0
while num < len(res):
    print(res[num].born,res[num].died,res[num].left,res[num].right)
    time.sleep(0.1)
    num += 1
