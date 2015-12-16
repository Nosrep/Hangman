#! /usr/bin/env python

import os, sys
import pygame
from pygame.locals import *

def load_image(name, colorkey=None):
    fullname = os.path.join('data', 'images')
    fullname = os.path.join(fullname, name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', fullname
        raise SystemExit, message
    image = image.convert_alpha()
    
    return image#, image.get_rect()

##def load_music(name):
##    fullname = os.path.join('data','sound')
##    fullname = os.path.join(fullname,name)
##    try:
##        pygame.mixer.music.load(name)
##    except pygame.error,message:
##        print 'cannot load music',fullname
##        raise SystemExit,message
    
