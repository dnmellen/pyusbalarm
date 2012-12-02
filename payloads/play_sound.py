'''
Created on 13/09/2012

@author: dnmellen
'''

import pygame
import os.path

def payload():
    '''
    Play a sound file
    '''
    
    pygame.mixer.init()
    sound = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), 
        'audios/ALARM.wav'))
    audio_chn = sound.play()
    print "Playing sound"
    while audio_chn.get_busy():
        pygame.time.delay(100)