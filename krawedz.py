import pygame as pg

class Krawedz(pg.sprite.Sprite):

    def __init__(self, plat, przeszkoda, x, y, strona):
        super().__init__()

        self.plat = plat
        self.ekran = self.plat.ekran
        self.ekran_rect = self.plat.ekran_rect
        self.srodek_ekranu = self.plat.srodek_ekranu
        self.strona = strona
        self.przeszkoda = przeszkoda
        self.przeszkoda.krawedzie.add(self)

        if strona == "right" or strona == "left":
            self.typ = "x"
            self.rect = pg.Rect(0,0,1,przeszkoda.rect.height)
        if strona == "top" or strona == "bottom":
            self.typ = "y"
            self.rect = pg.Rect(0,0,przeszkoda.rect.width,1)

        self.rect.center = (x,y)
        self.x, self.y = self.center_na_xy(self.rect.center)

    def update_pozycji(self):
        self.rect.center = self.xy_na_center(self.x, self.y)

    def xy_na_center(self, x, y):
        return self.srodek_ekranu[0]+x,self.srodek_ekranu[1]-y

    def center_na_xy(self, center):
        return center[0]-self.srodek_ekranu[0],self.srodek_ekranu[1]-center[1]
