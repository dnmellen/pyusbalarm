pyusbalarm
==========

Monitor USB devices and trigger an action when any of them is unplugged. The action is defined by a Python function (payload).

This program is still under development and by this time it only provides a very limited functionality.

## Licensing

BSD License

## Requirements

List of required Python modules

 - pyusb
 - pygame

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

The example included in *alarm.py* first explores the attached USB devices. 
Then the program enters into an infinite loop to check if any device has been unplugged, if so, the payload 
will be called and the loop will continue checking all devices again after the payload execution.
CTRL+C must be pressed to finish the program.

## TODO

 - PyQT4 GUI
 - Implement something to configure alarms (read a config file or GUI)
 - Add new payloads