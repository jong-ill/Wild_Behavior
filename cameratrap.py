from picamera import PiCamera
from gpiozero import MotionSensor, LED

import time

camera = PiCamera()
camera.rotation=180

led = LED(16)
pir = MotionSensor(4)
motion_now = pir.motion_detected
print(motion_now)

#while True:
    #motion_now = pir.motion_detected
    #print(motion_now)
    

while True:
    motion_now = pir.motion_detected
    #if motion_now == False:
        #break
    if motion_now == True:
        timestart = time.time()
        timenow = time.time()

        camera.start_preview(alpha=200)
        led.on()
        while timenow<timestart+10:
            timenow = time.time()
        camera.stop_preview()
        led.off()
        motion_now = pir.motion_detected
