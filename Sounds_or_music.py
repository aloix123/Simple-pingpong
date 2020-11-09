import time,pygame.mixer

"""""klasa , gdzie jest przechowywana muzyczka na starcie """""
class sound_music:
    def __init__(self):
        pygame.mixer.init()


        self.f = pygame.mixer.Sound('UFF.wav')



        time.sleep(1)
    def run_UFF(self):
        self.f.play()
        time.sleep(1)