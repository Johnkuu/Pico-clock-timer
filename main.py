import miniclock
import led
import time

miniclock.clear_disp()
miniclock.set_time_manually()
miniclock.set_time()
#miniclock.set_time()
time.sleep(1)

miniclock.buttons()

while True:
    miniclock.clock()