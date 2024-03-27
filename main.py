from RPLCD.i2c import CharLCD
from gpiozero import Button, LED
from timeit import default_timer as timer
import time
from libs.binTree import *

lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=16, rows=2, dotsize=8)
button = Button(5)
led = LED(6)

word = ''
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
    print(f"Actuall code: {code}")
    gstart = time.time()


def blink():
    for i in range(12):
        led.toggle()
        time.sleep(0.05)
    led.off()


def setup():
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
    global word
    posx = 0
    posy = 0
    node = makeMorseTree()
    while True:
        if not button.is_pressed:
            gend = time.time()
            if gend - gstart > 2 and code:
                led.on()
                letter = findLetter(node, code, 0)
                if letter:
                    lcd.cursor_pos = (posy, posx)
                    lcd.write_string(letter)
                    word += letter
                    print(f"Actuall code: {letter}")
                    posx += 1
                    if posx == 16:
                        posx = 0
                        posy += 1
                    if posy == 2:
                        posy = 0
                else:
                    lcd.clear()
                    lcd.cursor_pos = (0, 0)
                    lcd.write_string("Wrong morse code")
                    time.sleep(2)
                    lcd.clear()
                    lcd.write_string(word)
                code = ''
                gstart = gend
                time.sleep(0.5)
                led.off()
            elif gend - gstart >= 7 and word:
                lcd.clear()
                blink()
                code = ''
                word = ''
                posx = 0
                posy = 0
                led.off()
        
        button.when_pressed = starttime
        button.when_released = endtime


setup()
run()
