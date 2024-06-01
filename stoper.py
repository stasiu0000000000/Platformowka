import pygame as pg

class Stoper(pg.sprite.Sprite):

    def __init__(self, plat):
        super().__init__()

        self.plat = plat
        self.ekran = self.plat.ekran
        self.ekran_rect = self.plat.ekran_rect
        self.kolor = (255,255,255)

        self.przygotuj_tekst()
        self.czas_na_napis()

    def przygotuj_tekst(self):
        znaki_image_rect = []

        for i in range(12):
            if i < 10:
                c = str(i)
            elif i == 10:
                c = ":"
            elif i == 11:
                c = "."

            image_tekst = pg.font.SysFont("courier", 45).render(c, False, self.kolor, (0,0,0))
            image_tekst.set_colorkey((0,0,0))
            rect_tekst = image_tekst.get_rect()

            znaki_image_rect.append((image_tekst, rect_tekst))

        self.znaki_image_rect = tuple(znaki_image_rect)

    def update(self):
        self.czas_na_napis()

    def czas_na_napis(self):
        self.czas = str(int(self.plat.stoper_gry*100)/100)
        czas_split = self.czas.split(".")

        minuty = str(int(czas_split[0])//60)
        sekundy = str(int(czas_split[0])%60)
        setne_sekundy = czas_split[1]
        if len(minuty) < 2:
            minuty = "0" + minuty
        if len(sekundy) < 2:
            sekundy = "0" + sekundy
        if len(setne_sekundy) < 2:
            setne_sekundy = "0" + setne_sekundy

        self.indexy = [minuty[0],minuty[1],10,sekundy[0],sekundy[1],11,setne_sekundy[0],setne_sekundy[1]]

    def znak_na_index(self, znak):
        if type(znak) == int:
            znak = int(znak)
            return znak
        else:
            if znak == ":":
                return 10
            if znak == ".":
                return 11

    def index_na_znak(self, index):
        if index == 10:
            return ":"
        elif index == 11:
            return "."
        else:
            return str(index)

    def blitme(self):
        for i, index in enumerate(self.indexy):
            index = int(index)
            rect = self.znaki_image_rect[index][1]
            self.ekran.blit(self.znaki_image_rect[index][0], pg.Rect(self.ekran_rect.width+(i-9)*20,0,rect.width,rect.height))


