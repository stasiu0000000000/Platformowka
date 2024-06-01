import pygame as pg

class TekstyWygranej(pg.sprite.Sprite):

    def __init__(self, plat):
        super().__init__()

        self.plat = plat
        self.ekran = self.plat.ekran
        self.ekran_rect = self.plat.ekran_rect
        self.srodek_ekranu = self.plat.srodek_ekranu
        self.x = self.plat.okno_wygranej.x
        self.y = self.plat.okno_wygranej.y

    def przygotuj_teksty(self):
        self.teksty = []
        self.teksty.append(przygotuj_tekst(f"LEVEL : {self.plat.level}"))
        self.teksty.append(przygotuj_tekst(f"CZAS : {self.plat.stoper_gry}"))

    def update(self):
        self.teksty[0][1].center = (self.srodek_ekranu[0]+self.x+120,self.srodek_ekranu[1]-self.y-60)
        self.teksty[1][1].center = (self.srodek_ekranu[0]+self.x+110,self.srodek_ekranu[1]-self.y+60)

    def blitme(self):
        for tekst in self.teksty:
            self.ekran.blit(tekst[0], tekst[1])

def przygotuj_tekst(tekst):
    image_tekst = pg.font.SysFont(None, 40).render(tekst, False, (200,200,200), (0,0,0))
    image_tekst.set_colorkey((0,0,0))
    rect_tekst = image_tekst.get_rect()

    return image_tekst, rect_tekst
