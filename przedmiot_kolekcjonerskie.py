import pygame as pg

class PrzedmiotKolekcjonerski(pg.sprite.Sprite):

    def __init__(self, plat, x=0, y=0, typ_przedmiotu="moneta"):
        super().__init__()

        self.plat = plat
        self.ekran = self.plat.ekran
        self.ekran_rect = self.plat.ekran_rect
        self.srodek_ekranu = self.plat.srodek_ekranu
        self.fps = self.plat.fps
        self.typ_przedmiotu = typ_przedmiotu
        self.oryginal_x = self.x = x
        self.oryginal_y = self.y = x

        #od 0 (początek) do 1 (koniec)
        self.stan_animacji = 0
        self.czas_animacji = 1.5
        self.delta_sa = 1/self.fps/self.czas_animacji
        self.o_ile_podnies = 10

        self.koniec_animacji = False
        self.czy_zebrany = False

        self.stworz_grafike()
        
        self.image = self.grafika[0]
        self.rect = self.image.get_rect()

        self.update_pozycji()

    def stworz_grafike(self):
        grafika = []

        #image0 = pg.image.load("sciezka/obraz.bmp")
        #image0.set_colorkey((255,255,255))
        #grafika.append(image0)

        self.grafika = tuple(grafika)

    def jezeli_kolizja_ja_gracz(self):
        if not self.czy_zebrany:
            self.oryginal_x = self.x
            self.oryginal_y = self.y
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

    def update(self):
        if self.rect.colliderect(self.plat.gracz):
            self.jezeli_kolizja_ja_gracz()

        if self.czy_zebrany and not self.koniec_animacji:
            self.animacja_zebrania()

        self.update_pozycji()

    def update_pozycji(self):
        self.rect.center = self.xy_na_center(self.x, self.y)

    def blitme(self):
        self.ekran.blit(self.image, self.rect)

    def xy_na_center(self, x, y):
        return self.srodek_ekranu[0]+x,self.srodek_ekranu[1]-y

    def center_na_xy(self, center):
        return center[0]-self.srodek_ekranu[0],self.srodek_ekranu[1]-center[1]
