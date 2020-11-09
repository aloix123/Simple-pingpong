import pygame,sys,time # różne importy

from settings import Settings
from paletka import Paletka
from ball import Ball
from Scoreboard  import SScoreboard
from Sounds_or_music import sound_music
class Gra(Settings):
    def __init__(self):# różne klasy, zmienne itd
        pygame.init()

        self.screen_height = 700
        self.screen_widh = 1000
        self.opcje=Settings()
        self.screen = pygame.display.set_mode((self.screen_widh, self.screen_height))  # okno
        self.f=Paletka(self.screen)
        self.szary = (160, 160, 160)
        self.allmusic=sound_music()

        self.score=[0,0]

        self.ball = Ball(self.screen, self.f.gps1)




    def run_Gra(self):#sama gra
        while True:
            self.events()
            self.Tlo()
            self.events_pressed()
            pygame.display.flip()
            time.sleep(0.005)# speed
    def Tlo(self):# tło, kolor tła,rysunki o obiekty na nim umieszczone
        """tutaj powstaje tło ,kolorokna,i jego parametry"""




        self.screen.fill(self.szary)

        self.f.draw_paletka()
        self.ball.draw_ball()

        self.backend()


    def events(self):# funkcja odpowiadająca za wciśnięte kalwisze i ich reakcje na otoczenie
        for event in pygame.event.get():
            if event.type==pygame.QUIT:# czy chłop wcisnoł iksik w prawym górnym rogu ekranu
                sys.exit()# program się wyłącza
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_q or event.key==pygame.K_ESCAPE:# jeśli chłop wciśnie q lub escape
                    sys.exit()# wyłącz grę


    def events_pressed(self):# funkcja odpowiada za posuszanie się paletek po ekranie , tryb poruszania się to WS i up down
        if self.f.rect1.y>1:
            if pygame.key.get_pressed()[pygame.K_UP]:
                self.f.rect1.y-=self.opcje.paletka_speed
                self.f.gps1-=self.opcje.paletka_speed
        if self.f.rect1.y<600:
            if pygame.key.get_pressed()[pygame.K_DOWN]:
                self.f.rect1.y+=self.opcje.paletka_speed
                self.f.gps1 += self.opcje.paletka_speed
        if self.f.rect2.y>1:
            if pygame.key.get_pressed()[pygame.K_w]:
                self.f.rect2.y-=self.opcje.paletka_speed
                self.f.gps2 -= self.opcje.paletka_speed
        if self.f.rect2.y<600:
            if pygame.key.get_pressed()[pygame.K_s]:
                self.f.rect2.y+=self.opcje.paletka_speed
                self.f.gps2 += self.opcje.paletka_speed

    def backend(self):# ruch piłki
        self.ball.ball_run()
        self.listadesunia_deskalewa1()
        self.listadesunia_deskalewa2()
        self.ball_check()

        self.check_points()
        self.actual_points()
        self.scoreboard.show_score(self.screen)#liczba punktów

    def listadesunia_deskalewa1(self):#kolejna lista
        self.hag_lista = [i for i in range(-self.opcje.ball_size,self.opcje.deska_height+self.opcje.ball_size)]
        self.lista = list(map(lambda x: x + self.f.gps1, self.hag_lista))

    def listadesunia_deskalewa2(self):#lista
        self.hag_listas = [i for i in range(-self.opcje.ball_size,self.opcje.deska_height+self.opcje.ball_size)]
        self.listas = list(map(lambda x: x + self.f.gps2, self.hag_listas))
    def ball_check(self):
        """"""" ta funkcja odbija piłke od paletki"""""""
        if  self.ball.bal_rect.x==self.opcje.gps_height1-10 and  self.ball.bal_rect.y in self.lista:# jeśli piłka przed niebieską paletką i w liście
            self.ball.a=-self.ball.a # odbij

        if  self.ball.bal_rect.x==self.opcje.gps_height2+10 and  self.ball.bal_rect.y in self.listas:# jeśli piłka przed  czerwoną paletką i w liście

            self.ball.a=-self.ball.a #odbij w przeciwna stronę

    def check_points(self):
        if self.ball.bal_rect.x==0:
            self.allmusic.run_UFF()
            self.ball.bal_rect.y=350
            self.ball.bal_rect.x = 500
            self.ball.a = -1
            self.score[0]+=1





        if self.ball.bal_rect.x == 990:
            self.allmusic.run_UFF()
            self.ball.bal_rect.y = 350
            self.ball.bal_rect.x = 500
            self.ball.a=1
            self.score[1]+=1

    def actual_points(self):# aktualizuje liczbę punktów
        self.final_score=f'{self.score[0]}:{self.score[1]}'
        self.scoreboard = SScoreboard(self.final_score, self.szary)


if __name__=='__main__':# sprawdza czy się coś nie pierdoli z kodem
    d=Gra()
    d.run_Gra()