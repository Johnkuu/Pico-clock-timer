import tm1637
from machine import Pin
import time
import led

from machine import RTC

display = tm1637.TM1637(clk=Pin(0), dio=Pin(1))
 
button1 = Pin(13, Pin.IN, Pin.PULL_UP)
button2 = Pin(18, Pin.IN, Pin.PULL_UP)

b = 1 #(brightness of the display)

display.brightness(b) #Set brightness between 1-7)

def set_time():
    rtc = RTC()
#    hour = 20
#    minute = 40
    #rtc.datetime((year, month, day, weekday, hour, minute, second, 0))
    rtc.datetime((2022, 10, 16, 7, hour, minute, 0, 0))

#Clear all
def clear_disp():
    display.show("HIYA")
    time.sleep(1)
    display.show("    ")
    
def clock():
    # get system time
    local_time = str(time.localtime())
    parts = local_time.split(', ')
    hour = int(parts[3])
    minute = int(parts[4])
    second = int(parts[5])

    # Toggle colon when displaying time
    if second % 2:
        # setup HH.MM for display and print it
        display.numbers(hour, minute)
    else:
        # setup HH MM for display and print it
        display.number_time(hour, minute)
    time.sleep(0.5)

#while True:
#    clock()

def pomodore():
    display.show("    ") #tyhjennä näyttö
    rounds = 3 #aseta kierrosten määrä +1
    hour = 25 #aseta kierron aika
    minute = 0 # aseta kierron aika.
    while rounds > 0:
        b1 = button1.value()
        if not b1:
            led.ledredoff()
            break
        led.ledredon()
        display.number_time(hour, minute) # näytä lähtöaika
        hour = 24 #aseta seuraava aika
        minute = 59
        time.sleep(1)
        while True: #aloita kierrosten sisäinen looppi
            b1 = button1.value()
            if hour == 0 and minute == 0: # jos kaikki on nollilla aloita looppi jossa tarkastetaan kierrosten määrä tai hypätään pois
                if rounds == 0:# jos kaikki on nollilla ja kierrokset on nollilla, hyppää loopista pois
                    led.ledredoff()
                    break
                else: #muuten ajan ollessa nollilla laita 5 minuutin tauko käyntiin ja vähennä kierros
                    led.ledblueon()
                    led.ledredoff()
                    rounds -= 1
                    hour = 5
                    minute = 0
                    display.number_time(hour, minute) #Näytä 5 minsaa
                    time.sleep(1)
                    hour = 4 #näytä 4:49
                    minute = 59
                    led.ledblueon()
                    while True:
                        if minute == 0 and hour == 0: #jos minuutti ja sekuntti 0 hyppää pois loopista
                            display.number_time(hour, minute)
                            time.sleep(1)
                            hour = 24 #aseta aika takaisin normaaliin
                            minute = 59
                            break
                        if minute == 0: # jos minuutti 0 vähennä tunti ja aloita minuutti alusta
                            display.number_time(hour, minute)
                            minute = 59
                            hour -= 1
                        if not b1:
                            break
                        else: #muuten näytä aika ja vähennä sekuntti
                            display.number_time(hour, minute)
                        time.sleep(1)
                        minute-= 1
            if minute == 0: #jos vain sekuntit ovat nollilla, vähennä minuutti
                display.number_time(hour, minute)
                minute = 59
                hour -= 1
            if not b1:
                led.ledredoff()
                break    
            else: #muuten vähennä vain sekunti normaalisti
            # setup HH MM for display and print it
                display.number_time(hour, minute)
            time.sleep(1)
            minute-= 1
        hour = 25
        minute = 0
        display.number_time(hour, minute)
#Asettaa taukoajastimen 30 min
        hour = 30
        minute = 0
        display.number_time(hour, minute)
        time.sleep(1)
        hour = 29
        minute = 59
        time.sleep(1)
    
        while True: #Viimeinen 30 minuuttia, jonka jälkeen loppuu 00:00 5 s tauko ja koko silmukka päättyy
            b1 = button1.value()
            led.ledblueon()
            if hour == 0 and minute == 0:
                display.number_time(hour, minute)
                time.sleep(5)
                led.ledblueoff()
                break
            if minute == 0: 
                display.number_time(hour, minute)
                minute = 59
                hour -= 1
            if not b1:
                led.ledblueoff()
                led.ledredoff()
                break    
            else:
            # setup HH MM for display and print it
                display.number_time(hour, minute)
            time.sleep(1)
            minute-= 1
        
def buttons():
    b = 1
    while True:
        b1 = button1.value()
        b2 = button2.value()
        if not b1:
            print("Button 1 pressed!")
            led.ledblueon()
            if b == 7:
                b = 1
                print(b)
            else:
                b += 1
                print(b)
            display.brightness(b) #Set brightness between 1-7)
            time.sleep(0.5)
        if not b2:
            print("Button 2 pressed!")
            pomodore()
        else:
            led.ledblueoff()
            led.ledredoff()
            clock()

def set_time_manually():
    global hour
    global minute
    hour = 0
    minute = 0
    rounds = 0
    while True:
        b1 = button1.value()
        b2 = button2.value()   
        if not b2:
            hour = hour + 1
            display.number_time(hour,minute)
            time.sleep(0.1)
            print(hour)
            rounds = 0
            if hour == 23:
                hour = -1  
        if not b1:
            minute = minute + 1
            display.number_time(hour,minute)
            time.sleep(0.1)
            print(minute)
            rounds = 0
            if minute == 59:
                minute = -1        
        else:
            time.sleep(0.1)
            rounds += 1
            print(rounds)
            if rounds == 50:
                rtc = RTC()
                #hour = 20
                #minute = 40
                #rtc.datetime((year, month, day, weekday, hour, minute, second, 0))
                rtc.datetime((2022, 10, 16, 7, hour, minute, 0, 0))
                break
