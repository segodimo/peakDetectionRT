import time
import mpu6050
import micropython
from constants import *
from machine import Pin, ADC
from rtPeak05 import rtPeak

tms=50

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

thld = [2600, 3000, 3450]

pkp1 = rtPeak(3,1,thld)
    
while True:
    now = time.ticks_ms()
    write_dt = time.ticks_diff(now, lastsent)
    read_dt = time.ticks_diff(now, lastread)
    gc_dt = time.ticks_diff(now, lastgc)

    #time.sleep_ms(max(0, 1-read_dt))
    
    if flag_reset_gyro:
        mpu.filter.reset_gyro()
        flag_reset_gyro = False

    ga = mpu.read_position()
    
    p1 = pot1.read()
    p2 = pot2.read()
    p3 = pot3.read()
    p4 = pot4.read()
    lastread = now

    if write_dt >= write_interval:
        lastsent = time.ticks_ms()
        #print(p1,p2,p3,p4,ga)
        #print(p1)
        pk = pkp1.runPdRt(p1)
        if pk[0]: print(pk)


    if gc_dt >= gc_interval:
        gc.collect()
    
    time.sleep(tms/1000)



