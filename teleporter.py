import pygame as pg

class Teleporter(pg.sprite.Sprite):

    def __init__(self, plat, dane, rodzaj, kolor):
        super().__init__()

        self.plat = plat
        self.ekran = self.plat.ekran
        self.ekran_rect = self.plat.ekran_rect
        self.srodek_ekranu = self.plat.srodek_ekranu
        self.fps = self.plat.fps
        self.rodzaj = rodzaj
        self.kolor = kolor
        self.ile_do_naladowania = 0
        self.x = dane[0]
        self.y = dane[1]

        self.image = pg.image.load(f"grafika/teleporter/{self.kolor}_teleporter.bmp")
        if rodzaj == "b":
            self.image = pg.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()

        self.update_pozycji()

    def update(self):
        if self.ile_do_naladowania:
            self.image.set_alpha((1-self.ile_do_naladowania)*255*3/5)
        else:
            self.image.set_alpha(255)

        self.update_pozycji()

    def update_pozycji(self):
        self.rect.center = self.xy_na_center(self.x, self.y)

    def czy_teleportacja(self):
        if pg.sprite.collide_rect(self, self.plat.gracz):
            return True
        else:
            return False
    
    def blitme(self):
        self.ekran.blit(self.image, self.rect)

    def xy_na_center(self, x, y):
        return self.srodek_ekranu[0]+x,self.srodek_ekranu[1]-y

    def center_na_xy(self, center):
        return center[0]-self.srodek_ekranu[0],self.srodek_ekranu[1]-center[1]
