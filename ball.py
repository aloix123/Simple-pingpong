import pygame

from settings import Settings



"""klasa , która tworzy piłeczkę , jej rozmiary krztałt i ruch"""
class Ball(Settings):# piłeczka
    def __init__(self, screen,f):
        super().__init__()
        self.bal_rect=pygame.Rect(self.ball_gps1,self.ball_gps2,self.ball_size,self.ball_size)# kwadracik
        self.screen=screen
        self.bal_color=(255,128,0)# kolor piłki
        self.a=1
        self.b=1
        self.f=f
    def draw_ball(self):#funkcja rysująca piłke na ekranie
        pygame.draw.rect(self.screen,self.bal_color,self.bal_rect)
    def ball_run(self):# trajektoria ruchu piłki
        self.bal_rect.x-=self.a
        self.bal_rect.y+=self.b
        if self.bal_rect.y==700:# tego nie tykaj to jest dobrze
            self.b=-1
        if self.bal_rect.y==0:
            self.b=1


