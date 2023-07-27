
from machine import Pin
import network
import esp
import gc
import time

print()
print()

esp.osdebug(None)
gc.collect()

# ssid = 'rad_wifi'
# password = 'polito_rad'
# 
# station = network.WLAN(network.STA_IF)
# 
# station.active(True)
# 
# print("Trying to connect to " + ssid + "...")
led_pin = Pin(2, Pin.OUT)
led_pin.value(0)
# 
# station.connect(ssid, password)
# 
# while not station.isconnected():
#   led_pin.value(led_pin.value() ^ 1)
#   time.sleep(0.1)
# 
# print('Connection successful')
# print(station.ifconfig())
