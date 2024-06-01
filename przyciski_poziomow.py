import pygame as pg

class PPoziomow(pg.sprite.Sprite):

    def __init__(self, plat, id_po, x, y, klasa_poziomu):
        super().__init__()

        self.plat = plat
        self.ekran = self.plat.ekran
        self.ekran_rect = self.plat.ekran_rect
        self.srodek_ekranu = self.plat.srodek_ekranu
        self.czy_kliknieto = False
        self.x = x
        self.y = y
        self.klasa_poziomu = klasa_poziomu
        self.id = id_po

        self.czy_dostepny = not self.id
        self.czy_skonczony = False

        self.grafika = (pg.image.load("grafika/przycisk_level/przycisk_level_zamkniety.bmp"),pg.image.load("grafika/przycisk_level/przycisk_level_otwarty.bmp"))
        self.image = self.grafika[self.czy_dostepny]
        self.rect = self.image.get_rect()

        self.rect.center = self.xy_na_center(self.x, self.y)
        self.przygotuj_tekst()

    def przygotuj_tekst(self):
        self.image_tekst = pg.font.SysFont("comicsansms", 70).render(str(self.id+1), False, (200,200,200), (0,0,0))
        self.image_tekst.set_colorkey((0,0,0))
        self.rect_tekst = self.image_tekst.get_rect(center=self.rect.center)

    def czy_dotyka_myszy(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            return True
        else:
            return False

    def update_e(self, e):
        if e.type == pg.MOUSEBUTTONDOWN:
            if e.button == 1:
                if self.czy_dotyka_myszy(e.pos):
                    self.kliknieto()

    def kliknieto(self):
        self.czy_kliknieto = True
        if self.czy_dostepny:
            self.czy_kliknieto = False
            self.start_poziom()

    def start_poziom(self):
        self.plat.actual_level = self
        self.plat.level_klasa = self.klasa_poziomu
        self.plat.level = self.id+1
        self.plat.reset_poziomu(self.klasa_poziomu(self.plat))

    def update(self):
        if not self.czy_dostepny and self.id != -1:
            self.czy_dostepny = self.plat.znajdz_przycisk_poziom(self.id-1).czy_skonczony
        self.image = self.grafika[self.czy_dostepny]
        self.update_pozycji()

    def update_pozycji(self):
        self.rect.center = self.xy_na_center(self.x, self.y)

    def blitme(self):
        self.ekran.blit(self.image, self.rect)
        self.ekran.blit(self.image_tekst, self.rect_tekst)

    def xy_na_center(self, x, y):
        return self.srodek_ekranu[0]+x,self.srodek_ekranu[1]-y

    def center_na_xy(self, center):
        return center[0]-self.srodek_ekranu[0],self.srodek_ekranu[1]-center[1]
