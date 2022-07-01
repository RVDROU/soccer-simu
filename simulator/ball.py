import pygame, math, os
import numpy as np
from threading import Thread, Lock
from time import sleep
from utils import *




class Ball(pygame.sprite.Sprite) :
    def __init__(self) :
        pygame.sprite.Sprite.__init__(self)
        self.pose = np.array([0,0,0])
        self.position = self.pose[:2]
        self.orientation = self.pose[2]
        self.__time_step = 1/60
        self.__default_img = pygame.image.load(os.path.join('img', 'ball.png'))
        self.__default_img = pygame.transform.scale(self.__default_img, (6*SCALE, 6*SCALE))
        self.image = pygame.Surface.copy(self.__default_img)
        self.rect = self.image.get_rect()
        self.rect.center = (int(self.pose[0]*SCALE), int(self.pose[1]*SCALE))
        self.name = 'ball'
        
    def set_time_step(self, t) :
        self.__time_step = t

        
    def update(self) :
        self.move_ball()
        self.image = pygame.transform.rotate(self.__default_img, self.pose[2]*360/(2*PI))
        self.rect = self.image.get_rect()
        self.rect.center = (int(self.pose[0]*SCALE+FIELD_SIZE[0]/2+BORDER), int(-self.pose[1]*SCALE+FIELD_SIZE[1]/2+BORDER))
        
    def goto(self, x, y) :
        self.pose[0] = x
        self.pose[1] = y
        self.position = self.pose[:2]
        
    def move_ball(self) :
        '''Update absolute position'''
        if pygame.mouse.get_pressed()[0] :
            self.pose[0], self.pose[1] = self.__position_in_abs_frame(pygame.mouse.get_pos())
            self.pose[2] =  (self.pose[2] + 0.05) % (2*PI)
            self.position = self.pose[:2]
            self.orientation = self.pose[2]        

    def __position_in_abs_frame(self, pos) :
        x, y = pos
        return (int((x-BORDER-FIELD_SIZE[0]/2)//SCALE) , int(-(y-BORDER-FIELD_SIZE[1]/2)//SCALE))




