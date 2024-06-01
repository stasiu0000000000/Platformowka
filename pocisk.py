import pygame as pg
import math as m

class Pocisk(pg.sprite.Sprite):

    def __init__(self, plat, dzialko):
        super().__init__()

        self.plat = plat
        self.ekran = self.plat.ekran
        self.ekran_rect = self.plat.ekran_rect
        self.srodek_ekranu = self.plat.srodek_ekranu
        self.fps = self.plat.fps
        self.speed = 300
        self.speed_vector = self.normalize_vector(pg.math.Vector2(self.plat.gracz.pos.x-dzialko.x,self.plat.gracz.pos.y-dzialko.y)) * self.speed / self.fps

        self.x = dzialko.x
        self.y = dzialko.y

        self.rect = pg.Rect(0,0,10,10)

        self.update_pozycji()

    def normalize_vector(self, vector):
        try:
            vector = vector.normalize()
        except ValueError:
            vector = pg.math.Vector2(1,0)
        return vector

    def update(self):
        self.x, self.y = (self.x+self.speed_vector.x,self.y+self.speed_vector.y)

        if pg.sprite.spritecollideany(self, self.plat.przeszkody):
            self.kill()

        self.update_pozycji()

    def update_pozycji(self):
        self.rect.center = self.xy_na_center(self.x, self.y)

    def blitme(self):
        self.ekran.fill((255,0,0), self.rect)

    def xy_na_center(self, x, y):
        return self.srodek_ekranu[0]+x,self.srodek_ekranu[1]-y

    def center_na_xy(self, center):
        return center[0]-self.srodek_ekranu[0],self.srodek_ekranu[1]-center[1]
