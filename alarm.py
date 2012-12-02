# encoding: utf-8

'''
Created on 12/09/2012

@author: dnmellen
'''

__author__ = "Diego Navarro Mellén"
__email__ = "dnmellen@gmail.com"
__version__ = 0.5

import usb
from usb.core import USBError
import time


### Some auxiliary functions ###
def _clean_str(s):
    '''
    Filter string to allow only alphanumeric chars and spaces
    
    @param s: string
    @return: string
    '''
    
    return ''.join([c for c in s if c.isalnum() or c in {' '}])


def _get_dev_string_info(device):
    '''
    Human readable device's info
    
    @return: string
    '''
    
    try:
        str_info = _clean_str(usb.util.get_string(device, 256, 2))
        str_info += ' ' + _clean_str(usb.util.get_string(device, 256, 3))
        return str_info
    except USBError:
        return str_info
    
    
def get_usb_devices():
    '''
    Get USB devices
    
    @return: list of tuples (dev_idVendor, dev_idProduct, dev_name)
    '''
    
    return [(device.idVendor, device.idProduct, _get_dev_string_info(device)) 
                for device in usb.core.find(find_all=True)
                    if device.idProduct > 2]
        
        
class USBAlarm(object):
    '''
    USB Alarm Class
    '''
    
    
    def __init__(self, devices=None, payload=None, check_interval=0.5):
        '''
        Constructor
        
        @param devices: list of tuples (dev_idVendor, dev_idProduct, dev_name)
        @param payload: function to call if any device is disconnected
        @param check_interval: number of secs to wait in each check
        '''
        
        self.devices = devices or []
        self.payload = payload
        self.check_interval = check_interval


    def is_any_disconnected(self):
        '''
        Check if any device has been disconnected.
        
        @return: True if found any device unplugged
        '''
        
        return not all([usb.core.find(idVendor=device[0], idProduct=device[1])
                        for device in self.devices])


    def run(self):
        '''
        Make sure every device is plugged in an infinite loop
        '''
        
        while True:
            if self.is_any_disconnected() and self.payload:
                self.payload()
            time.sleep(self.check_interval)


if __name__ == '__main__':
   
    # Catch signal CTRL+C to exit test
    import signal
    import sys

    def signal_handler(signal, frame):
        print 'You Pressed CTRL+C'
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)
 
    # Dummy test
    from payloads import play_sound
    print "* Exploring devices"
    devices = get_usb_devices()
    for d in devices:
        print d[2]
    print "==================="
    print "Monitoring USB devices... (Press CTRL+C for exit)"
#    a = USBAlarm(devices=devices, payload=dummy_payload)
    a = USBAlarm(devices=devices, payload=play_sound.payload)
    a.run()
