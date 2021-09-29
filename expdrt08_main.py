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


pkp1 = rtPeak(3,1,[2600, 3000, 3450],['m','j','u'])
pkp2 = rtPeak(3,1,[2600, 3000, 3450],[',','k','i'])
pkp3 = rtPeak(3,1,[2600, 3000, 3450],['.','l','o'])
pkp4 = rtPeak(3,1,[2600, 3000, 3450],[';','c','p'])




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
        pk1 = pkp1.runPdRt(p1)
        if pk1[0]: print(pk1)
        
        pk2 = pkp2.runPdRt(p2)
        if pk2[0]: print(pk2)
        
        pk3 = pkp3.runPdRt(p3)
        if pk3[0]: print(pk3)
        
        pk4 = pkp4.runPdRt(p4)
        if pk4[0]: print(pk4)
        
    if gc_dt >= gc_interval:
        gc.collect()
    
    time.sleep(tms/1000)



