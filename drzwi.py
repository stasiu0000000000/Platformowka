import pygame as pg

from krawedz import Krawedz

class Drzwi(pg.sprite.Sprite):

    def __init__(self, plat, dane):
        super().__init__()

        self.plat = plat
        self.ekran = self.plat.ekran
        self.ekran_rect = self.plat.ekran_rect
        self.srodek_ekranu = self.plat.srodek_ekranu
        self.fps = self.plat.fps
        self.kolor = dane[4]
        self.kolor_rgb = self.kolor_na_RGB(dane[4])
        self.kolor_ramki = (255-self.kolor_rgb[0],255-self.kolor_rgb[1],255-self.kolor_rgb[2])
        self.grubosc_ramki = 4
        self.x = dane[0]
        self.y = dane[1]
        self.size = (dane[2],dane[3])

        #od 0 (początek) do 1 (koniec)
        self.stan_animacji = 0
        self.czas_animacji = 1.5
       
        self.klucz = self.plat.znajdz_klucz(self.kolor)

        self.zamkniete = True
        self.otwierane = False
        self.otwarte = False

        self.image_zamek = pg.image.load("grafika/zamek_od_drzwi.bmp")
        self.image_zamek.set_colorkey((255,255,255))
        self.rect_zamek = self.image_zamek.get_rect()
        self.rect = pg.Rect(0,0,self.size[0],self.size[1])
        self.rect.center = self.xy_na_center(self.x, self.y)
        self.rect_animacja = pg.Rect(self.rect)

        self.update()
        self.rect_zamek.center = self.rect.center
        self.rect_animacja.center = self.rect.center

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

    def kolor_na_RGB(self, kolor):
        if kolor == "czerwony":
            return (255,0,0)
        if kolor == "zolty":
            return (255,255,0)
        if kolor == "zielony":
            return (0,255,0)
        if kolor == "cyan":
            return (0,255,255)
        if kolor == "niebieski":
            return (0,0,255)
        if kolor == "magenta":
            return (255,0,255)
        if kolor == "bialy":
            return (255,255,255)

    def stworz_krawedzie(self):
        self.krawedzie = pg.sprite.Group()
        Krawedz(self.plat, self, self.rect.right, self.rect.centery, "right")
        Krawedz(self.plat, self, self.rect.left, self.rect.centery, "left")
        Krawedz(self.plat, self, self.rect.centerx, self.rect.top, "top")
        Krawedz(self.plat, self, self.rect.centerx, self.rect.bottom, "bottom")

    def update(self):
        if self.klucz.czy_zebrany and not self.otwarte:
            if self.klucz.koniec_animacji:
                self.stan_animacji = 1
            self.zamkniete = False
            self.otwierane = True
            self.animacja_zamykania()

        self.update_pozycji()
        self.rect_zamek.center = self.rect.center
        self.rect_animacja.center = self.rect.center

    def animacja_zamykania(self):
        if self.stan_animacji >= 1:
            self.stan_animacji = 0
            self.otwierane = False
            self.otwarte = True
            self.rect = pg.Rect(0,0,1,1)
            self.x = -self.srodek_ekranu[0]-100
            self.y = self.srodek_ekranu[1]+100
            self.stworz_krawedzie()

        if self.klucz.koniec_animacji:
            self.stan_animacji = 1
        self.rect_animacja.height = self.size[1] * (1-self.stan_animacji)
        self.rect_animacja.width = self.size[0] * (1-self.stan_animacji)

        self.stan_animacji += 1/self.fps/self.czas_animacji

    def update_pozycji(self):
        self.rect.center = self.xy_na_center(self.x, self.y)

    def blitme(self):
        if self.zamkniete:
            rect = self.rect_draw
            self.ekran.fill(self.kolor_ramki, rect)
            pg.draw.rect(self.ekran, self.kolor_rgb, pg.Rect(rect.left+self.grubosc_ramki, rect.top+self.grubosc_ramki, rect.width-self.grubosc_ramki*2, rect.height-self.grubosc_ramki*2))
            self.ekran.blit(self.image_zamek, self.rect_zamek)

        elif self.otwierane:
            self.ekran.fill(self.kolor_ramki, self.rect_animacja)
            pg.draw.rect(self.ekran, self.kolor_rgb, pg.Rect(self.rect_animacja.left+self.grubosc_ramki, self.rect_animacja.top+self.grubosc_ramki, self.rect_animacja.width-self.grubosc_ramki*2, self.rect_animacja.height-self.grubosc_ramki*2))

        elif self.otwarte:
            self.ekran.fill(self.kolor_rgb, self.rect)

    def znajdz_krawedz(self, strona):
        for k in self.krawedzie:
            if strona == k.strona:
                return k

    def xy_na_center(self, x, y):
        return self.srodek_ekranu[0]+x,self.srodek_ekranu[1]-y

    def center_na_xy(self, center):
        return center[0]-self.srodek_ekranu[0],self.srodek_ekranu[1]-center[1]
