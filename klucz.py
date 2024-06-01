import pygame as pg

class Klucz(pg.sprite.Sprite):

    def __init__(self, plat, dane):
        super().__init__()

        self.plat = plat
        self.ekran = self.plat.ekran
        self.ekran_rect = self.plat.ekran_rect
        self.srodek_ekranu = self.plat.srodek_ekranu
        self.fps = self.plat.fps
        self.kolor = dane[2]
        self.typ_przedmiotu = f"{self.kolor} klucz"
        self.oryginal_x = self.x = dane[0]
        self.oryginal_y = self.y = dane[1]

        #od 0 (początek) do 1 (koniec)
        self.stan_animacji = 0
        self.czas_animacji = 1.5
        self.delta_sa = 1/self.fps/self.czas_animacji
        self.o_ile_podnies = 10

        self.koniec_animacji = dane[3]
        self.czy_zebrany = dane[3]
        
        self.image = pg.image.load(f"grafika/klucze/{self.kolor}_klucz.bmp")
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()

        self.update_pozycji()

    def restart_poziomu(self, dane):
        if self.czy_powinno_odradzac:
            self.x = self.oryginalne_x
            self.y = self.oryginalne_y

            self.update_pozycji()
        else:
            self.koniec_animacji = True
            self.czy_zebrany = True

    def jezeli_kolizja_ja_gracz(self):
        if not self.czy_zebrany:
            self.oryginal_x = self.x
            self.oryginal_y = self.y
            self.plat.podnies_klucz.play()
            self.plat.niezapisane_przedmioty = True
            self.czy_zebrany = True

    def animacja_przegrania(self):
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
            self.animacja_przegrania()

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
