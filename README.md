# Pico-clock-timer
A Pico based clock with a pomodoro timer. Includes a 3D printable case. Powered with USB. No network needed.

# A Raspberry Pi Pico based clock with a pomodoro timer including a 3D printable case and two control buttons for keyboard enthusiasts.
- Only for raspberry Pi Pico
- Uses TM1637.h screen
- 2x led and 2x 330-ohm resistors
- 2x Mechanical keyboard switches
- 3D printable case
- 4x screws (think M3 size) are needed to attach the bottom to the upper case
- Some super glue to attach the screen and leds to the case
- Wire (I used single core)

## Functionality
- On startup says "HIYA" as greeting
- Set time: Hours with left button, minutes with right button. When idling for 5 seconds, the clock starts running. If nothing is done, sets time to 00.00
- After setting the time left button starts Pomodoro timer with 25 - 5 x4 cycle and ends with a 30-minute break. When it´s working time, the red led shines and during pauses, the blue led shines. When the timer is ready, the led´s goes off. On clock mode, no leds are on.
- When pressing button on right during the Pomodoro cycle the time skips to pause timer (30 min) and second press exits the timer
- The clock keeps the time even during when the pomodoro timer is running
- Adjustable screen light brightness with the left button. When pressing button the blue led blinks. Cycles from dark to brighter and when maxed out, starts from dimmer again.

## Functionality TBD
- ~~When pressing buttons on right side skips only to next iteration of the timer~~
- ~~When left button pressed stops the timer and continues when pressing again~~
- ~~When both buttons pressed exits the timer~~

## PINS:

- Display: CLK=Pin (0), DIO=Pin(1), GND=GND, 5V=VBUS
- LEDs:  ledred = Pin (9), Cathode (-) = GND and ledblue = Pin (27), Cathode (-) = GND (don´t forget the resistor!)
- Buttons: Button1 = Pin (13), GND and button2 = Pin (18), GND


## Instructions:
- Print case (use supports, doesn´t consume time/resources, looks better)
- Attach first the leds in the case with superglue (after setting the screen in place, it might be a slightly tight over there)
- Solder everything as instructed in PINS section, check everything is working before assembly. 
- Attach the screen with superglue, bear in your mind that it´s done in the right direction (check the text on the board)
- Attach the Pico to the bottom of the case. I used some filament from the 3D printer and heated the other end to make it flat. Some superglue in the holes in the bottom of the case and the filament through the Pico board holes and into the case holes.

![Pico](https://user-images.githubusercontent.com/50976633/197330112-0730af83-3479-42e1-8b92-9064deb3e25b.jpg)

