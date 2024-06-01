import pygame as pg

class Przycisk(pg.sprite.Sprite):

    def __init__(self, plat, x, y, tekst, kolor, dzialanie, arg=None):
        super().__init__()

        self.plat = plat
        self.ekran = self.plat.ekran
        self.ekran_rect = self.plat.ekran_rect
        self.srodek_ekranu = self.plat.srodek_ekranu
        self.kolor = kolor
        self.dzialanie = dzialanie
        self.arg = arg
        self.x = x
        self.y = y
        self.czy_klikniety = False
        self.tekst = tekst

        self.rect = pg.Rect(0,0,200,50)

        self.przygotuj_tekst()

        self.update()

    def przygotuj_tekst(self):
        self.image_tekst = pg.font.SysFont(None, 45).render(self.tekst, True, (255,255,255), self.kolor)
        self.rect_tekst = self.image_tekst.get_rect()

    def czy_dotyka_myszy(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            return True
        else:
            return False

    def update_e(self, e):
        if e.type == pg.MOUSEBUTTONDOWN:
            if e.button == 1:
                if self.czy_dotyka_myszy(e.pos):
                    self.czy_klikniety = True

    def update(self):
        if self.czy_klikniety:
            self.czy_klikniety = False
            if self.tekst == "RESET":
                self.plat.reset_poziomu(self.plat.poziom)
            else:
                if self.arg != None:
                    self.dzialanie(self.arg)
                else:
                    self.dzialanie()
        self.update_pozycji()
        self.rect_tekst.center = self.rect.center

    def update_pozycji(self):
        self.rect.center = self.xy_na_center(self.x, self.y)

    def blitme(self):
        self.ekran.fill(self.kolor, self.rect)
        self.ekran.blit(self.image_tekst, self.rect_tekst)

    def xy_na_center(self, x, y):
        return self.srodek_ekranu[0]+x,self.srodek_ekranu[1]-y

    def center_na_xy(self, center):
        return center[0]-self.srodek_ekranu[0],self.srodek_ekranu[1]-center[1]
