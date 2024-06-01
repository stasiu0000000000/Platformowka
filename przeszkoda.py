import pygame as pg

from krawedz import Krawedz

class Przeszkoda(pg.sprite.Sprite):

    def __init__(self, plat, dane):
        super().__init__()

        self.plat = plat
        self.ekran = self.plat.ekran
        self.ekran_rect = self.plat.ekran_rect
        self.srodek_ekranu = self.plat.srodek_ekranu
        self.kolor = (230,230,230)
        self.x = dane[0]
        self.y = dane[1]
        
        self.rect = pg.Rect(0,0,dane[2],dane[3])
        self.rect.center = self.xy_na_center(self.x, self.y)
        size = (min(self.rect.right,self.srodek_ekranu[0]*2)-max(self.rect.left,0),min(self.rect.bottom,self.srodek_ekranu[1]*2)-max(self.rect.top,0))
        self.rect_draw = pg.Rect(0,0,size[0],size[1])
        self.rect_draw.center = self.rect.center
        if self.rect.left < 0:
            self.rect_draw.right = self.rect.right
        if self.rect.right > self.srodek_ekranu[0]*2:
            self.rect_draw.left = self.rect.left
        if self.rect.top < 0:
            self.rect_draw.bottom = self.rect.bottom
        if self.rect.bottom > self.srodek_ekranu[1]*2:
            self.rect_draw.top = self.rect.top

        self.stworz_krawedzie()

    def stworz_krawedzie(self):
        self.krawedzie = pg.sprite.Group()
        Krawedz(self.plat, self, self.rect.right, self.rect.centery, "right")
        Krawedz(self.plat, self, self.rect.left, self.rect.centery, "left")
        Krawedz(self.plat, self, self.rect.centerx, self.rect.top, "top")
        Krawedz(self.plat, self, self.rect.centerx, self.rect.bottom, "bottom")

    def update(self):
        self.update_pozycji()

    def update_pozycji(self):
        self.rect.center = self.xy_na_center(self.x, self.y)
        for k in self.krawedzie:
            k.update_pozycji()

    def blitme(self):
        self.ekran.fill(self.kolor, self.rect_draw)

    def znajdz_krawedz(self, strona):
        for k in self.krawedzie:
            if strona == k.strona:
                return k

    def xy_na_center(self, x, y):
        return self.srodek_ekranu[0]+x,self.srodek_ekranu[1]-y

    def center_na_xy(self, center):
        return center[0]-self.srodek_ekranu[0],self.srodek_ekranu[1]-center[1]
