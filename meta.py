import pygame as pg

class Meta(pg.sprite.Sprite):

    def __init__(self, plat, dane):
        super().__init__()

        self.plat = plat
        self.ekran = self.plat.ekran
        self.ekran_rect = self.plat.ekran_rect
        self.srodek_ekranu = self.plat.srodek_ekranu
        self.fps = self.plat.fps
        self.kolor = (0,180,0)
        self.x = dane[0]
        self.y = dane[1]

        self.rect = pg.Rect(0,0,dane[2],dane[3])

        self.update_pozycji()

    def update(self):
        self.update_pozycji()

    def update_pozycji(self):
        self.rect.center = self.xy_na_center(self.x, self.y)

    def blitme(self):
        self.ekran.fill(self.kolor, self.rect)

    def xy_na_center(self, x, y):
        return self.srodek_ekranu[0]+x,self.srodek_ekranu[1]-y

    def center_na_xy(self, center):
        return center[0]-self.srodek_ekranu[0],self.srodek_ekranu[1]-center[1]
