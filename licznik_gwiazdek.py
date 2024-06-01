import pygame as pg

class LicznikGwiazdek(pg.sprite.Sprite):

    def __init__(self, plat, liczba_gwiazdek):
        super().__init__()

        self.plat = plat
        self.ekran = self.plat.ekran
        self.ekran_rect = self.plat.ekran_rect
        self.srodek_ekranu = self.plat.srodek_ekranu
        self.liczba_gwiazdek = liczba_gwiazdek
        self.stany_gwiazdek = [None for _ in range(self.liczba_gwiazdek)]
        self.x = -580
        self.y = 390

        self.rect = pg.Rect(0,0,1,1)

        self.stworz_grafike()

        self.update()

    def stworz_grafike(self):
        gz = pg.image.load("grafika/licznik_gwiazdek/g_zebrana.bmp")
        gz.set_colorkey((255,255,255))

        gdz = pg.image.load("grafika/licznik_gwiazdek/g_do_zebrania.bmp")
        gdz.set_colorkey((255,255,255))

        gs = pg.image.load("grafika/licznik_gwiazdek/g_skreslona.bmp")
        gs.set_colorkey((255,255,255))
        
        rect = pg.Rect(0,0,40,40)

        self.grafika = (gz,gdz,gs,rect)

    def update(self):
        for i, g in enumerate(self.plat.gwiazdki):
            self.stany_gwiazdek[i] = ((g.nie_zebrano+g.czy_zebrany)==0) + 2*g.nie_zebrano

        self.update_pozycji()

    def update_pozycji(self):
        self.rect.center = self.xy_na_center(self.x, self.y)

    def koniec_poziomu(self):
        for i in range(len(self.stany_gwiazdek)):
            if self.stany_gwiazdek[i] == 1:
                self.stany_gwiazdek[i] = 2

    def blitme(self):
        for i, stan in enumerate(sorted(self.stany_gwiazdek)):
            image = self.grafika[stan]
            rect = pg.Rect(self.rect.centerx+i*50,self.rect.centery,self.grafika[3].width,self.grafika[3].height)

            self.ekran.blit(image,rect)

    def xy_na_center(self, x, y):
        return self.srodek_ekranu[0]+x,self.srodek_ekranu[1]-y

    def center_na_xy(self, center):
        return center[0]-self.srodek_ekranu[0],self.srodek_ekranu[1]-center[1]
