import time
import math
import mpu6050
import micropython
from constants import *
from machine import Pin, ADC
from rtPeak05 import rtPeak

tms=20

micropython.alloc_emergency_exception_buf(100)

def isr(pin):
    print("Interrupt!")

mpu = mpu6050.MPU()

pot1 = ADC(Pin(34))
pot2 = ADC(Pin(35))
pot3 = ADC(Pin(32))
pot4 = ADC(Pin(33))
pot5 = ADC(Pin(39))

pot1.atten(ADC.ATTN_11DB)
pot2.atten(ADC.ATTN_11DB)
pot3.atten(ADC.ATTN_11DB)
pot4.atten(ADC.ATTN_11DB)
pot5.atten(ADC.ATTN_11DB)

lastgc = lastsent = lastread = time.ticks_ms()

write_interval = 10
gc_interval = 1000
flag_reset_gyro = False


def mean(data):
    if iter(data) is data:
        data = list(data)
    return sum(data)/len(data)

def clThdLM(pot,tms,tclth):
    tmc = tclth*(1000/tms)
    arr = []
    for i in range(tmc):
        p = pot.read()
        #print(p)
        arr.append(p)
        time.sleep(tms/1000)
    print(min(arr),max(arr))
    return (min(arr),max(arr),3450)

def tdu(nom):
  print('Calibrate %s...' % nom)
  for i in range(3):
    print('%s...' % (3-i))
    time.sleep(1000/1000)
  print('start...')

def clClik(pot,tms,clsamp,ths,nom):
  tdu(nom)
  cn = []
  cnt = 0

  while len(cn) < clsamp:
    p = pot.read()
    if p > ths[1]:
      cnt += 1
    else:
      if cnt > 0:
        print(cnt)
        cn.append(cnt)
        cnt = 0
    time.sleep(tms/1000)

  print('stop')
  print('Mean = %s' % (int(math.ceil(mean(cn)))))
  return int(math.ceil(mean(cn)))

def clClikMMHH(pot,tms,clsamp,ths,noms):
  res = []
  res.append(clClik(pot1,tms,clsamp,clths1,noms[0]))
  res.append(clClik(pot1,tms,clsamp,clths1,noms[1]))
  return res


     
tclth = 3
# clths1 = clThdLM(pot1,tms,tclth)
# clths2 = clThdLM(pot2,tms,tclth)
# clths3 = clThdLM(pot3,tms,tclth)
# clths4 = clThdLM(pot4,tms,tclth)

clths1 = [2796,2899,3450]
clths2 = [2738,2896,3450]
clths3 = [2762,2907,3450]
clths4 = [2694,2794,3450]

clsamp = 30
clck1 = clClikMMHH(pot1,tms,clsamp,clths1,['MM1','HH1'])

# pkp1 = rtPeak(3,1,clths1,['m','j','u'],clck1)
# pkp2 = rtPeak(3,1,clths2,[',','k','i'],clck2)
# pkp3 = rtPeak(3,1,clths3,['.','l','o'],clck3)
# pkp4 = rtPeak(3,1,clths4,[';','c','p'],clck4)

# while True:
#   p1 = pot1.read()
#   print(p1)
#   time.sleep(tms/1000)


# while True:
#     now = time.ticks_ms()
#     write_dt = time.ticks_diff(now, lastsent)
#     read_dt = time.ticks_diff(now, lastread)
#     gc_dt = time.ticks_diff(now, lastgc)
# 
#     #time.sleep_ms(max(0, 1-read_dt))
#     
#     if flag_reset_gyro:
#         mpu.filter.reset_gyro()
#         flag_reset_gyro = False
# 
#     ga = mpu.read_position()
#     
#     p1 = pot1.read()
#     p2 = pot2.read()
#     p3 = pot3.read()
#     p4 = pot4.read()
#     lastread = now
# 
#     if write_dt >= write_interval:
#         lastsent = time.ticks_ms()
#         #print(p1,p2,p3,p4,ga)
#         #print(p1)
#         pk1 = pkp1.runPdRt(p1)
#         if pk1[0]: print(pk1)
#         
#         pk2 = pkp2.runPdRt(p2)
#         if pk2[0]: print(pk2)
#         
#         pk3 = pkp3.runPdRt(p3)
#         if pk3[0]: print(pk3)
#         
#         pk4 = pkp4.runPdRt(p4)
#         if pk4[0]: print(pk4)
#         
#     if gc_dt >= gc_interval:
#         gc.collect()
#     
#     time.sleep(tms/1000)






