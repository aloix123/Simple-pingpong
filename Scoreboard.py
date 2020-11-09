
import pygame.font

"""""klasa , która tworzy licznik punktów"""""

class SScoreboard():
    def __init__(self,redpoint,szary):
        self.text_color=(0,255,0)# kolor czcionki numerków punktujących
        self.font=pygame.font.SysFont(None,48)
        self.redpoint = redpoint
        self.szary=szary
        self.prep_score()
    def prep_score(self):
        self.redpoint=str(self.redpoint)
        self.score_image=self.font.render(self.redpoint,True,self.text_color,self.szary)
        self.score_rect=self.score_image.get_rect()
        self.score_rect=(470,20)
    def show_score(self,screen):
        self.screen=screen
        self.screen.blit(self.score_image,self.score_rect)