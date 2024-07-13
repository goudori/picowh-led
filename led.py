from machine import Pin

import time

led = Pin("LED", Pin.OUT)

# Lチカを実行する
while True:
    led.on()
    print("LED点灯")
    
    time.sleep(1)
    
    led.off()
    print("LED消灯")
    
    time.sleep(1)


# BOOTSELボタンを押してLED(1=ON, 0=OFF)
# while True:
#     if rp2.bootsel_button() == 1:
#         led.on()
#         print("LED点灯")
#         
#     elif rp2.bootsel_button() == 0:
#         led.off()
#         print("LED消灯")
#         
#     else:
#         print("エラー発生")
#         

        