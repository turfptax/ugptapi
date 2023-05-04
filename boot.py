# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()

import network

# Declare wlan wifi LAN variable
wlan = network.WLAN(network.STA_IF)

# Reset Connection - Helps with wifi changes to reset
wlan.active(False)
wlan.active(True)

# Connect to SSID with Password
wlan.connect('OpenMuscle','3141592653')
while not wlan.isconnected():
    pass
print("connected ifconfig:",wlan.ifconfig())

# 



