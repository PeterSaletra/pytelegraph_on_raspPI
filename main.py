from RPLCD.i2c import CharLCD
from gpiozero import Button, LED
from timeit import default_timer as timer
import time
from libs.binTree import *

lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=16, rows=2, dotsize=8)
button = Button(5)
led = LED(6)

code =  ''
start =  0
end = 0
gstart = 0

def starttime():
    global start
    start =  time.time()
    led.on()

def endtime():
    global end
    global code
    global gstart
    end = time.time()
    led.off()
    if end - start >= 0.5:
        code += '-'
    elif end - start < 0.5:
        code += '.'
    print(code)
    gstart = time.time()

def setup():
    a = 'A'
    lcd.write_string(a)
    lcd.clear()
    lcd.write_string('Welcom to Morse Code')
    time.sleep(3)
    lcd.clear()
    lcd.write_string('Press to start')
    button.wait_for_press()
    led.on()
    time.sleep(1)
    led.off()
    lcd.clear()


def run():
    global gstart
    global code
    posx = 0
    posy = 0
    node = makeMorseTree()
    while True:
        if not button.is_pressed:
            gend = time.time()
            if gend - gstart > 2 and code:
                letter = findLetter(node, code, 0)
                print(letter)
                if letter:
                    code = ''
                    lcd.cursor_pos = (posy, posx)
                    lcd.write_string(letter)
                    posx += 1
                    if posx == 16:
                        posx = 0
                        posy += 1
                    if posy == 2:
                        posy = 0
                gstart = gend
            elif gend - gstart >= 7:
                lcd.clear()
        
        button.when_pressed = starttime
        button.when_released = endtime


setup()
run()
