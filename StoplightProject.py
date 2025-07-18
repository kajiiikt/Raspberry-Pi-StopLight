from gpiozero import Button, LED, PWMOutputDevice
from time import sleep
from LCD import LCD

lcd = LCD(2, 0x27, True)

red = LED(18)
yellow = LED(17)
green = LED(27) # Green LED is more dim look closely

button = Button(16)
buzzer = PWMOutputDevice(12)

pedestrian_request = [False]

def handle_button():
    print("Pedestrian pressed")
    pedestrian_request[0] = True
    
button.when_pressed = handle_button

def timer(seconds):
    for seconds in range(seconds, 0, -1):
            lcd.message(str(seconds), 1)
            sleep(1)

# The actual light sequence including conditional when button pressed
while True:
    if pedestrian_request[0]:
        print("Pedestrian crossing!")    
        red.on()
        yellow.off()
        green.off()
        lcd.message("Pedestrian Crossing!", 2)
        for i in range(5):
            buzzer.frequency = 1000
            buzzer.value = 0.5
            sleep(0.2)
            buzzer.off()
            sleep(0.8)
            
        timer(7)
            
        pedestrian_request[0] = False
        
        lcd.clear()
        
    print("Main sequence simulation")
    # Main sequence: Green Light    
    red.off()
    yellow.off()
    green.on()
    timer(7)
    lcd.clear()
    
    # Yellow Light
    red.off()
    yellow.on()
    green.off()
    timer(3)
    lcd.clear()
    
    # Red light
    red.on()
    yellow.off()
    green.off()
    timer(6)
    lcd.clear()
            
