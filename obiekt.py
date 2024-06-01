import pygame as pg

class Obiekt(pg.sprite.Sprite):

    def __init__(self, plat, x=0, y=0, kolor=(0,0,0)):
        super().__init__()

        self.plat = plat
        self.ekran = self.plat.ekran
        self.ekran_rect = self.plat.ekran_rect
        self.srodek_ekranu = self.plat.srodek_ekranu
        self.fps = self.plat.fps
        self.kolor = kolor
        self.x = x
        self.y = y

        self.image = pg.surface.Surface((30, 30))
        #self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()

        self.update_pozycji()

    def update_e(self, e):
        pass

    def update(self):
        self.update_pozycji()

    def update_pozycji(self):
        self.rect.center = self.xy_na_center(self.x, self.y)

    def blitme(self):
        self.image.fill(self.kolor)
        self.ekran.blit(self.image, self.rect)

    def xy_na_center(self, x, y):
        return self.srodek_ekranu[0]+x,self.srodek_ekranu[1]-y

    def center_na_xy(self, center):
        return center[0]-self.srodek_ekranu[0],self.srodek_ekranu[1]-center[1]
