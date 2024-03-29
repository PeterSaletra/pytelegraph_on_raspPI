from RPLCD.i2c import CharLCD
from gpiozero import Button, LED
from libs.binTree import makeMorseTree, findLetter
from libs.httpClient import HTTPClient
import time

lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=16, rows=2, dotsize=8)
button = Button(5)
led = LED(6)

client  = HTTPClient("localhost", 8000)
word = ''
code =  ''
start =  0
end = 0
gstart = 0


def starttime():
    '''
    Starts to count time how long button was presssed
    '''

    global start

    start =  time.time()
    led.on()


def endtime():
    '''
    Stops time and based on time determinates whether it was long or short signal.
    '''

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


def reset():
    '''
    Resets LCD Screen if you entered whole word and sends it to the server or 
    writes it to the file.
    '''

    global code
    global word
    
    if client.checkConnection():
        client.sendWord(word)
    else:
        with open("messages.txt", "+a") as file:
            file.write(word)

    lcd.clear()
    blink()

    code = ''
    word = ''

def printLetter(letter: str, posy: int, posx: int):
    '''
    Prints letter on the LCD Screen and adds letter to whole word.

    :param str letter: letter which was tranaslated form morse code into str
    :param int posy: position on y axis of 16x2 LCD Screen
    :param int posx: position on x axis of 16x2 LCD Screen
    '''
    
    global word
    
    lcd.cursor_pos = (posy, posx)
    lcd.write_string(letter)
    word += letter
    print(f"Actuall code: {letter}")


def wrongMorseCode():
    '''
    Let you now if you inputed wrong morse code comibination.
    '''
    
    lcd.clear()
    lcd.cursor_pos = (0, 0)
    lcd.write_string("Wrong morse code")
    time.sleep(2)
    lcd.clear()
    lcd.write_string(word)


def blink():
    '''
    Custom led blink mode.
    '''
    
    for i in range(12):
        led.toggle()
        time.sleep(0.05)
    led.off()


def setup():
    '''
    Setups LCD Screen and tells user when to start entering morse code 
    '''

    lcd.clear()
    lcd.write_string('Welcome to Morse Code')
    time.sleep(3)
    lcd.clear()
    lcd.write_string('Press to start')
    button.wait_for_press()
    led.on()
    time.sleep(1)
    led.off()
    lcd.clear()


def run():
    '''
    Run whole code and determinates whether user entered letter or whole word
    '''

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
                    printLetter(letter, posy, posx)
                    posx += 1
                    if posx == 16:
                        posx = 0
                        posy += 1
                    if posy == 2:
                        posy = 0
                else:
                    wrongMorseCode()
                code = ''
                gstart = gend
                time.sleep(0.5)
                led.off()
            elif gend - gstart >= 7 and word:
                reset()
                posx = 0
                posy = 0
        
        button.when_pressed = starttime
        button.when_released = endtime

if __name__ == "__main__":
    setup()
    run()
