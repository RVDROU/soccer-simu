'''Version avec la gestion du déplacement (jacobien) opérationnel'''


import pygame, math, os
import numpy as np
from threading import Thread, Lock
from time import sleep
from utils import *


class Robot(pygame.sprite.Sprite) :
    def __init__(self, color) :
        '''color : blue, green'''
        assert color in ['green', 'blue'] , 'Unknown color'
        self.__field = pygame.image.load(os.path.join('img', 'field.png'))
        self.__field = pygame.transform.scale(self.__field, WINDOW_SIZE)
        
        self.__motors = np.array([0,0,0], dtype=np.int16) # [m1, m2, m3]
        self.__time_step = 1/60
        self.__size = np.array([0,0], dtype=np.int16)     #radius wheel, platform radius
        self.__jac_inv = np.array([[0,0,0],
                            [0,0,0],
                            [0,0,0]])
   
        # Attributs publics
        self.pose = np.array([0,0,0])      # [x, y, theta]
        self.position = self.pose[:2]
        self.orientation = self.pose[2]     
        self.__lock = Lock()
        pygame.sprite.Sprite.__init__(self)
        self.color = color
        self.__init_sprite()
        self.name = '{0} robot'.format(self.color)          
        
    def __init_sprite(self) :
        ''' setup sprite '''
        pictures = {'green' : 'green_robot.png', 'blue' : 'blue_robot.png'}
        self.__default_img = pygame.image.load(os.path.join('img', pictures[self.color]))
        self.__default_img = pygame.transform.scale(self.__default_img, (2*self.__size[1]*SCALE, 2*self.__size[1]*SCALE))
        self.image = pygame.Surface.copy(self.__default_img)
        self.__display()
    
    
    def __absolute_speed(self) :
        '''Absolute speed of robot -> (vx, vy, w) : numpy array
        '''
        speed =  rot_matrix(-self.orientation) @ (kinematic_inv(self.__size[1]) @ (self.__size[0]*self.__motors))
        return speed
    
    def __display(self) :
        self.image = pygame.transform.rotate(self.__default_img, (self.pose[2]*360/(2*PI))+90)
        self.rect = self.image.get_rect()
        self.rect.center = (int(self.pose[0]*SCALE+FIELD_SIZE[0]/2+BORDER), int(-self.pose[1]*SCALE+FIELD_SIZE[1]/2+BORDER))
    
    def set_time_step(self, t) :
        self.__lock.acquire()
        self.__time_step = t
        self.__lock.release()    
    
    def set_size(self, size) :
        '''Size of robot / r : wheel radius, b : platform radius
        '''
        self.__lock.acquire()
        self.__size = np.array(size)
        self.__init_sprite()
        self.__lock.release()
            
    def get_size(self) :
        return self.__size
    
    
    def set_pos(self, pose) :
        '''initial position x, y , theta
        '''
        self.__lock.acquire()
        self.pose = np.array(pose)
        self.position = self.pose[:2]
        self.orientation = self.pose[2]
        self.__lock.release()
     
    
    def get_absolute_speed(self) :
        '''Absolute speed of robot-> (vx, vy, w) : tuple
        '''
        return tuple(self.__absolute_speed())

    def update(self) :
        self.move_robot()
        self.__display()      
        
        
    def move_robot(self) :
        '''Update absolute position'''
        speed = self.__absolute_speed()
        self.pose = self.pose + speed*self.__time_step
        self.position = self.pose[:2]
        self.pose[2] = self.pose[2] % (2*PI)
        self.orientation = self.pose[2]
              
    def speed_motors(self, m1, m2, m3) :
        '''Set speed of motors'''
        self.__lock.acquire()
        self.__motors = np.array([m1, m2, m3], dtype=np.float32)
        self.__lock.release()
        
    
    def __drive_speed(self, speed) :
        '''Define motor speed according to absolute linear speed of the robot
        speed : tuple (vx, vy, omega)
        return motor speed (tuple) according to the frame geometry
        '''
        vx, vy, omega = speed
        k = kinematic(self.__size[1])         
        w = tuple((1/self.__size[0])*(k @ (rot_matrix(self.orientation) @ np.array([vx,vy,omega]).T)))
        return w
    
    def goto(self, target, wait = True):
        if wait:
            while not self.goto(target, wait = False):
                sleep(0.05)
            self.speed_motors(0, 0, 0)
            return True        
        x, y, orientation = target
        #x = min(self.x_max, max(self.x_min, x))
        #y = min(self.y_max, max(self.y_min, y))
        error_x = x - self.pose[0]
        error_y = y - self.pose[1]
        error_orientation = angle_wrap(orientation - self.orientation)
        speed = (0.6*error_x, 0.6*error_y, 0.8*error_orientation)
        m1, m2, m3 = self.__drive_speed(speed)
        self.speed_motors(m1, m2, m3)
        return np.linalg.norm([error_x, error_y, error_orientation]) < 1
    
    def control(self, vx, vy, omega) :
        speed = (vx, vy, omega)
        m1, m2, m3 = self.__drive_speed(speed)
        self.speed_motors(m1, m2, m3)

