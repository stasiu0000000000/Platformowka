import pygame as pg
from random import random

class LicznikMonet(pg.sprite.Sprite):

    def __init__(self, plat, wszystkie_monety):
        super().__init__()

        self.plat = plat
        self.ekran = self.plat.ekran
        self.ekran_rect = self.plat.ekran_rect
        self.srodek_ekranu = self.plat.srodek_ekranu
        self.fps = self.plat.fps
        self.x = -500
        self.y = 300

        self.zebrane_monety = 0
        self.wszystkie_monety = wszystkie_monety
        self.czy_dzialac = (self.wszystkie_monety != 0)

        if self.czy_dzialac:
            self.przygotuj_tekst()

            self.image = pg.image.load("grafika/licznik_monet.bmp")
            self.image.set_colorkey((0,0,0))
            self.image.set_alpha(200)
            self.rect = self.image.get_rect(center=self.xy_na_center(self.x, self.y))

    def przygotuj_tekst(self):
        liczby_grafika = []

        for i in range(10):
            c = f"{i}/{self.wszystkie_monety}"

            image_tekst = pg.font.SysFont("courier", 40).render(c, False, (0,0,0), (255,255,255))
            image_tekst.set_colorkey((255,255,255))
            image_tekst.set_alpha(200)
            rect_tekst = image_tekst.get_rect()
            liczby_grafika.append((image_tekst, rect_tekst))

        self.liczby_grafika = tuple(liczby_grafika)

    def update(self):
        if self.czy_dzialac:
            self.zebrane_monety = 0
            for m in self.plat.monety:
                self.zebrane_monety += m.czy_zebrany

            self.napis = str(self.zebrane_monety)
            if len(self.napis) < 1:
                self.napis = "0" + self.napis

            self.update_pozycji()

    def update_pozycji(self):
        self.rect.center = self.xy_na_center(self.x, self.y)

    def blitme(self):
        if self.czy_dzialac:
            self.ekran.blit(self.image, self.rect)

            for i, liczba in enumerate(str(self.zebrane_monety)[::-1]):
                x = self.rect.centerx + 50 - i * 20
                y = self.rect.centery+5
                image = self.liczby_grafika[int(liczba)][0]
                rect = self.liczby_grafika[int(liczba)][1]
                rect = pg.Rect(0,0,rect.width,rect.height)
                rect.center = (x,y)
                self.ekran.blit(image, rect)

    def xy_na_center(self, x, y):
        return self.srodek_ekranu[0]+x,self.srodek_ekranu[1]-y

    def center_na_xy(self, center):
        return center[0]-self.srodek_ekranu[0],self.srodek_ekranu[1]-center[1]
