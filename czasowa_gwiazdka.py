import pygame as pg
import math as m

class CzasowaGwiazdka(pg.sprite.Sprite):

    def __init__(self, plat, dane):
        super().__init__()

        self.plat = plat
        self.ekran = self.plat.ekran
        self.ekran_rect = self.plat.ekran_rect
        self.srodek_ekranu = self.plat.srodek_ekranu
        self.fps = self.plat.fps
        self.kolor_kola = (255,255,0)
        self.typ_przedmiotu = "gwiazdka"
        self.size = (40,40)
        self.pozostaly_czas = dane[2]
        self.oryginal_x = self.x = dane[0]
        self.oryginal_y = self.y = dane[1]

        #od 0 (początek) do 1 (koniec)
        self.stan_animacji = 0
        self.czas_animacji = 1.5
        self.delta_sa = 1/self.fps/self.czas_animacji
        self.o_ile_podnies = 20

        self.koniec_animacji = False
        self.nie_zebrano = False
        self.czy_zebrany = False
        
        self.stworz_grafike()
        self.co_ile_sekund_obroc = 0.1

        self.error = 0
        self.stan_animacji_kola = 0
        self.czas_animacji_kola = self.pozostaly_czas
        self.punkty_na_klatki = 360/self.pozostaly_czas/self.fps
        self.stworz_punkty()
        
        self.index_grafiki = 0
        self.image = self.grafika[self.index_grafiki]
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()

        self.update_pozycji()

    def stworz_grafike(self):
        gwiazdka1 = pg.transform.scale(pg.image.load("grafika/gwiazdka/gwiazdka1.bmp"), self.size)
        gwiazdka1.set_colorkey((255,255,255))
        gwiazdka2 = pg.transform.scale(pg.image.load("grafika/gwiazdka/gwiazdka2.bmp"), self.size)
        gwiazdka2.set_colorkey((255,255,255))
        gwiazdka3 = pg.transform.scale(pg.image.load("grafika/gwiazdka/gwiazdka3.bmp"), self.size)
        gwiazdka3.set_colorkey((255,255,255))
        gwiazdka4 = pg.transform.scale(pg.image.load("grafika/gwiazdka/gwiazdka4.bmp"), self.size)
        gwiazdka4.set_colorkey((255,255,255))
        gwiazdka5 = pg.transform.scale(pg.image.load("grafika/gwiazdka/gwiazdka3.bmp"), self.size)
        gwiazdka5.set_colorkey((255,255,255))
        gwiazdka6 = pg.transform.scale(pg.image.load("grafika/gwiazdka/gwiazdka2.bmp"), self.size)
        gwiazdka6.set_colorkey((255,255,255))

        self.grafika = (gwiazdka1, gwiazdka2, gwiazdka3, gwiazdka4, gwiazdka5, gwiazdka6)

    def stworz_punkty(self):
        self.punkty = []
        for n in range(360):
            n = m.radians(n)-m.pi/2
            x = m.cos(n)*40+self.srodek_ekranu[0]+self.x
            y = m.sin(n)*40+self.srodek_ekranu[1]-self.y
            self.punkty.append((int(x),int(y)))

    def jezeli_kolizja_ja_gracz(self):
        if not self.czy_zebrany:
            self.oryginal_x = self.x
            self.oryginal_y = self.y
            self.plat.podnies_gwiazdke.play()
            self.plat.niezapisane_przedmioty = True
            self.czy_zebrany = True

    def animacja_zebrania(self):
        if self.stan_animacji >= 1:
            self.x = self.oryginal_x
            self.y = self.oryginal_y
            self.delta_sa = 0
            self.stan_animacji = 1
            self.koniec_animacji = True

        self.image.set_alpha((1-self.stan_animacji)*255)
        self.y += self.delta_sa * self.o_ile_podnies

        self.stan_animacji += self.delta_sa

    def idle_animacja(self):
        self.index_grafiki += 1/self.co_ile_sekund_obroc/self.fps
        self.index_grafiki = self.index_grafiki % len(self.grafika)
        self.image = self.grafika[int(self.index_grafiki)]
        
        if len(self.punkty) > 1:
            self.error += self.punkty_na_klatki
            while self.error >= 1:
                self.error -= 1
                del self.punkty[-1]
        elif not self.czy_zebrany:
            self.punkty.clear()
            self.nie_zebrano = True
            self.czy_zebrany = True

    def update(self):
        if self.rect.colliderect(self.plat.gracz):
            self.jezeli_kolizja_ja_gracz()

        self.idle_animacja()
                    
        if self.czy_zebrany and not self.koniec_animacji:
            self.animacja_zebrania()

        self.update_pozycji()

    def update_pozycji(self):
        self.rect.center = self.xy_na_center(self.x, self.y)

    def blitme(self):
        if not self.koniec_animacji:
            self.ekran.blit(self.image, self.rect)
            if not self.stan_animacji:
                if len(self.punkty) > 1:
                    pg.draw.lines(self.ekran, self.kolor_kola, False, self.punkty, 2)
                elif len(self.punkty) == 1:
                    try:
                        self.ekran.set_at(self.punkty[0], self.kolor_kola)
                    except:
                        print(self.punkty[0], self.kolor_kola)
                        self.plat.koniec()

    def xy_na_center(self, x, y):
        return self.srodek_ekranu[0]+x,self.srodek_ekranu[1]-y

    def center_na_xy(self, center):
        return center[0]-self.srodek_ekranu[0],self.srodek_ekranu[1]-center[1]
