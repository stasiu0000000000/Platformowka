import pygame as pg

class Moneta(pg.sprite.Sprite):

    def __init__(self, plat, dane):
        super().__init__()

        self.plat = plat
        self.ekran = self.plat.ekran
        self.ekran_rect = self.plat.ekran_rect
        self.srodek_ekranu = self.plat.srodek_ekranu
        self.fps = self.plat.fps
        self.typ_przedmiotu = "moneta"
        self.size = (25,25)
        self.oryginal_x = self.x = dane[0]
        self.oryginal_y = self.y = dane[1]

        #od 0 (początek) do 1 (koniec)
        self.stan_animacji = 0
        self.czas_animacji = 1.5
        self.delta_sa = 1/self.fps/self.czas_animacji
        self.o_ile_podnies = 10

        self.koniec_animacji = dane[2]
        self.czy_zebrany = dane[2]

        self.stworz_grafike()
        self.co_ile_sekund_obroc = 1/6
        
        self.index_grafiki = 0
        self.image = self.grafika[self.index_grafiki]
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()

        self.update_pozycji()

    def stworz_grafike(self):
        moneta1 = pg.transform.scale(pg.image.load("grafika/moneta/moneta1.bmp"), self.size)
        moneta1.set_colorkey((255,255,255))
        moneta2 = pg.transform.scale(pg.image.load("grafika/moneta/moneta2.bmp"), self.size)
        moneta2.set_colorkey((255,255,255))
        moneta3 = pg.transform.scale(pg.image.load("grafika/moneta/moneta3.bmp"), self.size)
        moneta3.set_colorkey((255,255,255))
        moneta4 = pg.transform.scale(pg.image.load("grafika/moneta/moneta4.bmp"), self.size)
        moneta4.set_colorkey((255,255,255))
        moneta5 = pg.transform.scale(pg.image.load("grafika/moneta/moneta5.bmp"), self.size)
        moneta5.set_colorkey((255,255,255))

        self.grafika = (moneta1, moneta2, moneta3, moneta4, moneta5)

    def jezeli_kolizja_ja_gracz(self):
        if not self.czy_zebrany:
            self.oryginal_x = self.x
            self.oryginal_y = self.y
            self.plat.podnies_monete.play()
            self.plat.niezapisane_przedmioty = True
            self.czy_zebrany = True

    def animacja_zebrania(self):
        if self.stan_animacji >= 1:
            self.x = self.oryginal_x
            self.y = self.oryginal_y
            self.delta_sa = 0
            self.stan_animacji = 1
            self.koniec_animacji = True
            return

        self.image.set_alpha((1-self.stan_animacji)*255)
        self.y += self.delta_sa * self.o_ile_podnies

        self.stan_animacji += self.delta_sa

    def idle_animacja(self):
        self.index_grafiki += 1/self.co_ile_sekund_obroc/self.fps
        self.index_grafiki = self.index_grafiki % len(self.grafika)
        self.image = self.grafika[int(self.index_grafiki)]

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

    def xy_na_center(self, x, y):
        return self.srodek_ekranu[0]+x,self.srodek_ekranu[1]-y

    def center_na_xy(self, center):
        return center[0]-self.srodek_ekranu[0],self.srodek_ekranu[1]-center[1]
