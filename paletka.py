import pygame

from settings import Settings

class Paletka(Settings):
    def __init__(self,screen):
        self.screen=screen
        super().__init__()
        self.rect1=pygame.Rect(self.gps_height1,self.gps1,self.deska_widh,self.deska_height)
        self.rect2 = pygame.Rect(self.gps_height2, self.gps2, self.deska_widh, self.deska_height)
    def draw_paletka(self):
        pygame.draw.rect(self.screen,self.desk1_color,self.rect1)
        pygame.draw.rect(self.screen,self.desk2_color,self.rect2)