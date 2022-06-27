'''Version avec la gestion du déplacement (jacobien) opérationnel'''


import pygame, os, sys
import numpy as np
from threading import Thread, Lock
from time import sleep
from utils import *

class Text(pygame.sprite.Sprite) :
    
    def __init__(self, pos = (int(0.7*WINDOW_SIZE[0]), 10)) :
        pygame.sprite.Sprite.__init__(self)
        pygame.font.init()
        self.text = ' '
        self.font = pygame.font.Font(None, 28)
        self.name = 'texte'
        self.rect = pygame.Rect(pos, (1, 1))
        self.update()
        
    def font(self, font) :
        self.font = font
        
    def update(self):
        color=pygame.Color('black')
        lines = self.text.splitlines()
        text_surfaces = [self.font.render(txt, True, color) for txt in lines]
        height = self.font.get_height()
        width = max(surface.get_width() for surface in text_surfaces)
        self.image = pygame.Surface((width, height * len(lines)), pygame.SRCALPHA)
        for i, surface in enumerate(text_surfaces) :
            self.image.blit(surface,(0, i*height))
        self.rect = self.image.get_rect(topleft = self.rect.topleft)
                                    
  
class Simulator() :

    def __init__(self, framePerSec) :
        pygame.init()
        self.__field = pygame.image.load(os.path.join('img', 'field.png'))
        self.__field = pygame.transform.scale(self.__field, WINDOW_SIZE)
        self.__fps = framePerSec
        self.__all_sprites = pygame.sprite.Group()
        self.__clock = pygame.time.Clock()
        self.__thread = Thread(target = self.loop)


    def is_running(self) :
        return self.__thread.is_alive()

    def fps(self,framePerSec) :
        '''Set frame per second'''
        self.__fps = framePerSec
           
    def get_thread(self) :
        return self.__thread
    
    def add(self, obj) :
        obj.set_time_step(1/self.__fps)
        self.__all_sprites.add(obj)
    
    def run(self) :
        self.__thread.start()
        
    def loop(self) :
        screen = pygame.display.set_mode(WINDOW_SIZE)
        screen.blit(self.__field, (0,0))
        infos = Text()
        self.__all_sprites.add(infos)
        flag = True
        while flag :
            for event in pygame.event.get() :
                if event.type == pygame.QUIT :
                    flag = False

            infos.text = ''
            for sprite in self.__all_sprites :
                if sprite.name in ['ball', 'blue robot', 'green robot'] :
                    infos.text = infos.text + '{0} : {1}, {2}\n'.format(sprite.name, int(sprite.position[0]), int(sprite.position[1]))
            self.__all_sprites.clear(screen, self.__field)
            self.__all_sprites.update()
            self.__all_sprites.draw(screen)
            pygame.display.flip()


        
    
    

