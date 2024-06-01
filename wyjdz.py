import pygame as pg

class Wyjdz(pg.sprite.Sprite):

    def __init__(self, plat):
        super().__init__()

        self.plat = plat
        self.ekran = self.plat.ekran
        self.ekran_rect = self.plat.ekran_rect
        self.srodek_ekranu = self.plat.srodek_ekranu
        self.czy_kliknieto = False
        self.x = 75-self.srodek_ekranu[0]
        self.y = 75-self.srodek_ekranu[1]

        self.image = pg.transform.scale(pg.image.load("grafika/wyjdz.bmp"),(100,100))
        self.rect = self.image.get_rect()

        self.update_pozycji()

    def czy_dotyka_myszy(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            return True
        else:
            return False

    def update_e(self, e):
        if e.type == pg.MOUSEBUTTONDOWN:
            if e.button == 1:
                if self.czy_dotyka_myszy(e.pos):
                    self.czy_kliknieto = True

    def update(self):
        if self.czy_kliknieto:
            self.czy_kliknieto = False
            self.plat.zmien_stan(0)
        self.update_pozycji()

    def update_pozycji(self):
        self.rect.center = self.xy_na_center(self.x, self.y)

    def blitme(self):
        self.ekran.blit(self.image, self.rect)

    def xy_na_center(self, x, y):
        return self.srodek_ekranu[0]+x,self.srodek_ekranu[1]-y

    def center_na_xy(self, center):
        return center[0]-self.srodek_ekranu[0],self.srodek_ekranu[1]-center[1]
