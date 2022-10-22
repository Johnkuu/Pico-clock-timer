from machine import Pin
import time

ledred = Pin(9, Pin.OUT)
ledblue = Pin(27, Pin.OUT)

def ledblueon():
    ledblue.on()

def ledblueoff():
    ledblue.off()

def ledredon():
    ledred.on()

def ledredoff():
    ledred.off()