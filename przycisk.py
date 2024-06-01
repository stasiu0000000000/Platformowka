import pygame as pg

class Przycisk(pg.sprite.Sprite):

    def __init__(self, plat, x=0, y=0, kolor=(0,0,0)):
        super().__init__()

        self.plat = plat
        self.ekran = self.plat.ekran
        self.ekran_rect = self.plat.ekran_rect
        self.srodek_ekranu = self.plat.srodek_ekranu
        self.fps = self.plat.fps
        self.kolor = kolor
        self.czy_kliknieto = False
        self.x = x
        self.y = y

        self.image = pg.surface.Surface((30, 30))
        #self.image.set_colorkey((255,255,255))
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
                    self.kliknieto(self.center_na_xy(e.pos))

        if e.type == pg.MOUSEBUTTONUP:
            if e.button == 1:
                if self.czy_kliknieto:
                    self.puszczono(self.center_na_xy(e.pos))

    def kliknieto(self, mouse_pos):
        self.czy_kliknieto = True
        print("kliknieto")

    def puszczono(self, mouse_pos):
        self.czy_kliknieto = False
        print("puszczono")

    def czy_kliknieto_rowna_1(self, mouse_pos):
        pass

    def czy_kliknieto_rowna_0(self, mouse_pos):
        pass

    def update(self):
        mouse_pos = self.center_na_xy(pg.mouse.get_pos())
        if self.czy_kliknieto:
            self.czy_kliknieto_rowna_1(mouse_pos)
        else:
            self.czy_kliknieto_rowna_0(mouse_pos)

        self.update_pozycji()

    def update_pozycji(self):
        self.rect.center = self.xy_na_center(self.x, self.y)

    def blitme(self):
        self.image.fill(self.kolor)
        self.ekran.blit(self.image, self.rect)

    def xy_na_center(self, x, y):
        return self.srodek_ekranu[0]+x,self.srodek_ekranu[1]-y

    def center_na_xy(self, center):
        return center[0]-self.srodek_ekranu[0],self.srodek_ekranu[1]-center[1]
