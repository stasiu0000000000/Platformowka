import pygame as pg

from pocisk import Pocisk

class Dzialko(pg.sprite.Sprite):

    def __init__(self, plat, dane):
        super().__init__()

        self.plat = plat
        self.ekran = self.plat.ekran
        self.ekran_rect = self.plat.ekran_rect
        self.srodek_ekranu = self.plat.srodek_ekranu
        self.fps = self.plat.fps
        self.kolor = (200,100,50)
        self.co_ile_strzal = 1
        self.stoper = 0
        self.x = dane[0]
        self.y = dane[1]
        
        self.promien = 15

        self.rect = pg.Rect(0,0,1,1)

        self.update_pozycji()

    def update(self):
        self.stoper += 1/self.fps
        if self.stoper >= self.co_ile_strzal:
            self.stoper -= self.co_ile_strzal
            self.strzal()

        self.update_pozycji()

    def update_pozycji(self):
        self.rect.center = self.xy_na_center(self.x, self.y)

    def strzal(self):
        self.plat.pociski.add(Pocisk(self.plat, self))

    def blitme(self):
        pg.draw.circle(self.ekran, self.kolor, self.rect.center, self.promien)

    def xy_na_center(self, x, y):
        return self.srodek_ekranu[0]+x,self.srodek_ekranu[1]-y

    def center_na_xy(self, center):
        return center[0]-self.srodek_ekranu[0],self.srodek_ekranu[1]-center[1]
