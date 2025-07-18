# Raspberry-Pi-StopLight
Real time working stoplight with timers, working physical button, and a buzzer for audible preference. 
Raspberry Pi Stoplight & Pedestrian System with LCD


**Overview**
Real time working stoplight with timers, working physical button, and a buzzer for audible preference. 
Hardware: 
- Raspberry Pi 5
- 3x GPIO LEDs (Green, Yellow, Red)
- GPIO Button
- GPIO Passive Buzzer
- 4x 220 ohm resistors
- Jumper cables
	The simulation mimics real-life traffic control systems that include multiple modules to highlight user interaction rather than just automation. Small but useful project to help beginners understand state machines, delays, and the importance of event driven programming. 
**Features**
- Traffic light with GPIO LEDs
- Physical Pedestrian Walk Button
- LCD display for message/timer
- Passive Buzzer as warning
- Timed light sequence and interaction



**Challenges & Fixes**
Challenges:
I2C LCD and Gpiozero Errors:
- Struggled to get I2C and Gpiozero(buttons/buzzer) to work together in a virtual environment or even in the same script
	System Integration:
- Manage timing, button inputs, and display output which required clean logic and efficient sequencing
	Fixes I Made:
	Custom LCD Class:
- Ditched installing RPLCD and imported raw smbus class directly into the project folder to control LCD with other modules in the same environment.
	Working Physical System
- With trial and error but most importantly problem solving skills all modules, all code, and logic were working together that achieved a fully functional demo for traffic flow. 

**Code Snippet:**
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
Media Link
didaiddjaia


