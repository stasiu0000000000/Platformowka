import pygame as pg

from wrog import Wrog
from dzialko import Dzialko

class Strzelec(Wrog):

    def __init__(self, pwg, dane):
        self.dzialko = Dzialko(pwg, dane)
        
        super().__init__(pwg, dane)
        
        self.kolor = (200,0,0)

    def update(self):
        self.ruch()
        self.dzialko.update()
        self.update_pozycji()

    def update_pozycji(self):
        self.dzialko.x = self.x
        self.dzialko.y = self.y
        self.rect.center = self.xy_na_center(self.x, self.y)

    def blitme(self):
        self.dzialko.blitme()
        self.ekran.fill(self.kolor, self.rect)
