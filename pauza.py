import pygame as pg

class Pauza(pg.sprite.Sprite):

    def __init__(self, plat):
        super().__init__()

        self.plat = plat
        self.ekran = self.plat.ekran
        self.ekran_rect = self.plat.ekran_rect
        self.srodek_ekranu = self.plat.srodek_ekranu
        self.x = -(self.srodek_ekranu[0]-20)
        self.y = -(self.srodek_ekranu[1]-20)
        self.czy_klikniety = False

        self.image_pauza = pg.image.load("grafika/pauza.bmp")
        self.image_pauza.set_colorkey((0,0,0))
        self.image_pauza.set_alpha(100)
        self.rect_pauza = self.image_pauza.get_rect()

        self.image_prostokat = pg.transform.scale(pg.image.load("grafika/prostokat1x1.bmp"),self.ekran_rect.size)
        self.image_prostokat.set_alpha(150)
        self.rect_prostokat = self.image_prostokat.get_rect()

        self.update_pozycji()

    def czy_dotyka_myszy(self, mouse_pos):
        if self.rect_pauza.collidepoint(mouse_pos):
            return True
        else:
            return False

    def update_e(self, e):
        if e.type == pg.MOUSEBUTTONDOWN:
            if e.button == 1:
                if self.czy_dotyka_myszy(e.pos):
                    self.czy_klikniety = True

        if e.type == pg.KEYDOWN and e.key == pg.K_SPACE:
            self.czy_klikniety = True

    def update(self):
        if self.czy_klikniety:
            self.czy_klikniety = False
            self.plat.zmien_stan(5)
        self.update_pozycji()

    def update_pozycji(self):
        self.rect_pauza.center = self.xy_na_center(self.x, self.y)

    def blitme(self):
        self.ekran.blit(self.image_pauza, self.rect_pauza)
        if self.plat.stan == self.plat.wszystkie_stany[5]:
            self.ekran.blit(self.image_prostokat, self.rect_prostokat)

    def xy_na_center(self, x, y):
        return self.srodek_ekranu[0]+x,self.srodek_ekranu[1]-y

    def center_na_xy(self, center):
        return center[0]-self.srodek_ekranu[0],self.srodek_ekranu[1]-center[1]
