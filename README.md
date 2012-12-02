pyusbalarm
==========

Monitor USB devices and trigger an action when any of them is unplugged. The action is defined by a Python function (payload).


## Licensing

BSD License

## Features

 - Check attached USB devices
 - Perform an action when any device is unplugged
 - Command line interface

## Example of use

You must have root priviliges to run this script (accessing usb info requires it)

    bluesman@diego-workstation:~/workspace/pyusbalarm$ sudo python alarm.py 
    * Exploring devices
    USB Laser Mouse
    24G Wireless Touchpad Keyboard
    ===================
    Monitoring USB devices... (Press CTRL+C for exit)
    Playing sound
    Playing sound
    ^CYou Pressed CTRL+C

## TODO

 - PyQT4 GUI
 - Implement something to configure alarms (read a config file or GUI)
 - Add new payloads