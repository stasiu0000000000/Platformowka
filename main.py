import pygame as pg
import sys as s

from przycisk_gry import Przycisk

from okno_wygranej import OknoWygranej
from teksty_wygranej import TekstyWygranej

from pauza import Pauza

from przyciski_poziomow import PPoziomow

from wyjdz import Wyjdz

from gracz import Gracz
from przeszkoda import Przeszkoda
from zla_sciana import ZlaSciana
from wrog import Wrog
from dzialko import Dzialko
from moneta import Moneta
from licznik_monet import LicznikMonet
from gwiazdka import Gwiazdka
from czasowa_gwiazdka import CzasowaGwiazdka
from licznik_gwiazdek import LicznikGwiazdek
from klucz import Klucz
from drzwi import Drzwi
from meta import Meta
from teleporter import Teleporter
from polaczenie_teleportow import PolaczenieTeleportow
from strzelec import Strzelec
from stoper import Stoper

import skonczone_poziomy as p
from poziomy import Poziom11

class Platformowka():

    def start(self):
        pg.init()
        pg.mixer.init()

        self.zegar = pg.time.Clock()
        self.fps = 60
        self.delta_time = 1/self.fps

        self.level = 1
        self.stoper_gry = 0

        self.mute = False

        self.mouse = pg.mouse.get_pos()

        self.gracz_xy = None

        self.wszystkie_stany = ("menu", "game time", "animacja przegrania", "animacja wygrania", "ekran wygrania", "pauza", "", "wybierz poziom")
        self.zmien_stan(0)

        self.init()

        self.while_function()

    def init(self):
        self.init_dzwiekow()
        self.init_grup()
        self.init_ekranu()
        self.init_obiektow()

    def init_dzwiekow(self):
        self.smierc_gracza = pg.mixer.Sound("dzwieki/smierc_gracza.wav")
        self.smierc_gracza.set_volume(1/5*(not self.mute))

        self.podnies_monete = pg.mixer.Sound("dzwieki/podnies_monete.wav")
        self.podnies_monete.set_volume(3/4*(not self.mute))

        self.podnies_gwiazdke = pg.mixer.Sound("dzwieki/podnies_gwiazdke.wav")
        self.podnies_gwiazdke.set_volume(1/10*(not self.mute))

        self.podnies_klucz = pg.mixer.Sound("dzwieki/podnies_klucz.wav")
        self.podnies_klucz.set_volume(1/10*(not self.mute))

        self.wejscie_w_meta = pg.mixer.Sound("dzwieki/wejscie_w_meta.wav")
        self.wejscie_w_meta.set_volume(1/20*(not self.mute))

        self.teleportuj_sie = pg.mixer.Sound("dzwieki/teleportuj_sie.wav")
        self.teleportuj_sie.set_volume(1/10*(not self.mute))

    def init_grup(self):
        self.przyciski_menu = pg.sprite.Group()
        self.przyciski_wygranej = pg.sprite.Group()
        self.przyciski_przegranej = pg.sprite.Group()
        self.przyciski_pauzy = pg.sprite.Group()
        self.przyciski_poziomow = pg.sprite.Group()

        self.przeszkody = pg.sprite.Group()
        self.drzwi = pg.sprite.Group()
        self.klucze = pg.sprite.Group()
        self.monety = pg.sprite.Group()
        self.gwiazdki = pg.sprite.Group()
        self.teleportery = pg.sprite.Group()
        self.polaczenia_teleportow = []
        self.zle_sciany = pg.sprite.Group()
        self.wrogowie = pg.sprite.Group()
        self.dzialka = pg.sprite.Group()
        self.strzelcy = pg.sprite.Group()
        self.pociski = pg.sprite.Group()

        self.grupy_w_game_time = (self.przeszkody,self.drzwi,self.klucze,self.monety,self.gwiazdki,self.teleportery,self.zle_sciany,self.wrogowie,self.dzialka,self.strzelcy,self.pociski)
        self.grupy_kolidujace_z_graczem = (self.przeszkody, self.drzwi)
        self.grupy_z_animacjami = (self.drzwi, self.monety, self.gwiazdki, self.klucze)
        self.grupy_wrogie  = (self.wrogowie, self.strzelcy, self.pociski, self.zle_sciany)
        self.grupy_przedmiotow_kolekcjonerskich = (self.klucze, self.monety, self.gwiazdki)

    def init_ekranu(self):
        self.ekran = pg.display.set_mode((1200, 800))
        pg.display.set_caption("Platformówka")
        self.ekran_rect = self.ekran.get_rect()
        self.srodek_ekranu = self.ekran_rect.center

    def init_obiektow(self):
        self.zrob_przyciski_poziomow()

        self.zrob_przyciski_menu()

        self.okno_wygranej = OknoWygranej(self)
        self.teksty_wygranej = TekstyWygranej(self)
        self.zrob_przyciski_wygrania()

        self.pauza = Pauza(self)
        self.zrob_przyciski_pauzy()

        self.stoper = Stoper(self)

        self.wyjdz = Wyjdz(self)

    def zrob_przyciski_menu(self):
        self.przyciski_menu.add(Przycisk(self, 0, 105, "PLAY", (0,255,0), self.znajdz_przycisk_poziom(0).start_poziom))
        self.przyciski_menu.add(Przycisk(self, 0, 35, "LEVELS", (0,0,255), self.zmien_stan, 7))
        self.przyciski_menu.add(Przycisk(self, 0, -105, "QUIT", (255,0,0), self.koniec))

    def zrob_przyciski_wygrania(self):
        self.przyciski_wygranej.add(Przycisk(self, -90, 105, "NEXT LEVEL", (0,255,0), self.nastepny_poziom))
        self.przyciski_wygranej.add(Przycisk(self, -90, 35, "RESET", (255,0,0),  self.reset_poziomu, self.level))
        self.przyciski_wygranej.add(Przycisk(self, -90, -35, "LEVELS", (0,0,255), self.zmien_stan, 7))
        self.przyciski_wygranej.add(Przycisk(self, -90, -105, "MAIN", (150,150,150), self.zmien_stan, 0))

    def zrob_przyciski_przegrania(self):
        self.przyciski_przegranej.add(Przycisk(self, -90, 100, "RESET", (255,0,0), self.reset_poziomu, self.level))
        self.przyciski_przegranej.add(Przycisk(self, -90, 0, "LEVELS", (0,0,255), self.zmien_stan, 7))
        self.przyciski_przegranej.add(Przycisk(self, -90, -100, "MAIN", (150,150,150), self.zmien_stan, 0))

    def zrob_przyciski_pauzy(self):
        self.przyciski_pauzy.add(Przycisk(self, 0, 105, "RESUME", (0,255,0), self.zmien_stan, 1))
        self.przyciski_pauzy.add(Przycisk(self, 0, 35, "RESET", (200,0,0),self.reset_poziomu, self.level))
        self.przyciski_pauzy.add(Przycisk(self, 0, -35, "LEVELS", (0,0,255), self.zmien_stan, 7))
        self.przyciski_pauzy.add(Przycisk(self, 0, -105, "MAIN", (150,150,150), self.zmien_stan, 0))

    def zrob_przyciski_poziomow(self):
        id_po = 0
        self.przyciski_poziomow.add(PPoziomow(self,id_po,-3/4*self.srodek_ekranu[0],1/2*self.srodek_ekranu[1],p.Poziom1))
        id_po += 1
        self.przyciski_poziomow.add(PPoziomow(self,id_po,-1/4*self.srodek_ekranu[0],1/2*self.srodek_ekranu[1],p.Poziom2))
        id_po += 1
        self.przyciski_poziomow.add(PPoziomow(self,id_po,1/4*self.srodek_ekranu[0],1/2*self.srodek_ekranu[1],p.Poziom3))
        id_po += 1
        self.przyciski_poziomow.add(PPoziomow(self,id_po,3/4*self.srodek_ekranu[0],1/2*self.srodek_ekranu[1],p.Poziom4))
        id_po += 1
        self.przyciski_poziomow.add(PPoziomow(self,id_po,-3/4*self.srodek_ekranu[0],0,p.Poziom5))
        id_po += 1
        self.przyciski_poziomow.add(PPoziomow(self,id_po,-1/4*self.srodek_ekranu[0],0,p.Poziom6))
        id_po += 1
        self.przyciski_poziomow.add(PPoziomow(self,id_po,1/4*self.srodek_ekranu[0],0,p.Poziom7))
        id_po += 1
        self.przyciski_poziomow.add(PPoziomow(self,id_po,3/4*self.srodek_ekranu[0],0,p.Poziom8))
        id_po += 1
        self.przyciski_poziomow.add(PPoziomow(self,id_po,-3/4*self.srodek_ekranu[0],-1/2*self.srodek_ekranu[1],p.Poziom9))
        id_po += 1
        self.przyciski_poziomow.add(PPoziomow(self,id_po,-1/4*self.srodek_ekranu[0],-1/2*self.srodek_ekranu[1],p.Poziom10))
        id_po += 1
        self.przyciski_poziomow.add(PPoziomow(self,id_po,1/4*self.srodek_ekranu[0],-1/2*self.srodek_ekranu[1],Poziom11))
        id_po += 1
        self.przyciski_poziomow.add(PPoziomow(self,id_po,3/4*self.srodek_ekranu[0],-1/2*self.srodek_ekranu[1],p.Poziom12))

        self.przyciski_poziomow.add(PPoziomow(self,-1,self.srodek_ekranu[0]+100,0,p.PoziomYouWin))

    def zaladuj_gre(self, poziom):
        for grupa in self.grupy_w_game_time:
            grupa.empty()
        self.polaczenia_teleportow = []

        self.zaladuj_poziom(poziom)

        self.licznik_gwiazdek = LicznikGwiazdek(self, len(self.gwiazdki))
        self.licznik_monet = LicznikMonet(self, len(self.monety))

    def kontynuj_gre(self):
        for grupa in self.grupy_w_game_time:
            grupa.empty()

        self.zaladuj_poziom(self.poziom, self.gracz_xy)

    def zaladuj_poziom(self, poziom, gracz_xy=None):
        self.poziom = poziom

        if gracz_xy == None:
            self.gracz = Gracz(self, self.poziom.get_kordynaty_gracza())
        else:
            self.gracz = Gracz(self, gracz_xy)

        self.meta = Meta(self, self.poziom.meta_dane)

        for dane in self.poziom.przeszkody_dane:
            self.przeszkody.add(Przeszkoda(self, dane))

        for dane in self.poziom.zle_sciany_dane:
            self.zle_sciany.add(ZlaSciana(self, dane))

        for dane in self.poziom.wrogowie_dane:
            self.wrogowie.add(Wrog(self, dane))

        for dane in self.poziom.dzialka_dane:
            self.dzialka.add(Dzialko(self, dane))

        for dane in self.poziom.strzelcy_dane:
            self.strzelcy.add(Strzelec(self, dane))

        for i, dane in enumerate(self.poziom.monety_dane):
            self.monety.add(Moneta(self, dane+(False,)))

        for i, dane in enumerate(self.poziom.gwiazdki_dane):
            self.gwiazdki.add(Gwiazdka(self, dane+(False,)))

        for dane in self.poziom.teleportery_dane:
            if dane[0][0]<dane[1][0]:
                t1 = Teleporter(self,dane[0],"a",dane[2])
                t2 = Teleporter(self,dane[1],"b",dane[2])
            else:
                t1 = Teleporter(self,dane[1],"a",dane[2])
                t2 = Teleporter(self,dane[0],"b",dane[2])

            self.teleportery.add(t1)
            self.teleportery.add(t2)
            self.polaczenia_teleportow.append(PolaczenieTeleportow(self,t1,t2,dane[3]))

        for i, klucz_drzwi in enumerate(self.poziom.klucze_drzwi_dane):
            self.klucze.add(Klucz(self, klucz_drzwi[0]+(False,)))
            for dane in klucz_drzwi[1]:
                self.drzwi.add(Drzwi(self, dane))

    def while_function(self):
        while True:
            self.sprawdzanie_zdarzen()
            self.update()
            self.aktualizacja_ekranu()
            self.zegar.tick(self.fps)

    def sprawdzanie_zdarzen(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                self.koniec()

            self.update_e(e)

    def koniec(self):
        pg.quit()
        s.exit()

    def update_e(self, e):
        if self.stan == self.wszystkie_stany[0]:
            for pm in self.przyciski_menu:
                pm.update_e(e)

        if self.stan == self.wszystkie_stany[1]:
            if e.type == pg.KEYDOWN:
                if e.key == pg.K_r:
                    self.reset_poziomu(self.poziom)

            for grupa in self.grupy_w_game_time:
                for obiekt in grupa:
                    try:
                        obiekt.update_e(e)
                    except:
                        pass

            self.gracz.update_e(e)
            self.pauza.update_e(e)

        if self.stan == self.wszystkie_stany[4]:
            for pw in self.przyciski_wygranej:
                    pw.update_e(e)

        if self.stan == self.wszystkie_stany[5]:
            for pp in self.przyciski_pauzy:
                pp.update_e(e)

        if self.stan == self.wszystkie_stany[7]:
            self.wyjdz.update_e(e)
            for po in self.przyciski_poziomow:
                po.update_e(e)

    def update(self):
        if self.stan == self.wszystkie_stany[0]:
            for pm in self.przyciski_menu:
                pm.update()

        if self.stan == self.wszystkie_stany[1]:
            self.stoper_gry += self.delta_time
            self.stoper.update()

            self.pauza.update()

            for pt in self.polaczenia_teleportow:
                pt.update()
            for grupa in self.grupy_w_game_time:
                for obiekt in grupa:
                    obiekt.update()

            self.licznik_monet.update()
            self.licznik_gwiazdek.update()


            self.meta.update()
            self.gracz.update()

            if self.czy_przegrana():
                self.przegrana()
            if self.czy_wygrana():
                self.wygrana()

        if self.stan == self.wszystkie_stany[2] or self.stan == self.wszystkie_stany[3]:
            self.gracz.update()
            for grupa in self.grupy_z_animacjami:
                for obiekt in grupa:
                    if obiekt.stan_animacji > 0:
                        obiekt.update()

        if self.stan == self.wszystkie_stany[4]:
            self.okno_wygranej.update()
            for pw in self.przyciski_wygranej:
                pw.update()
            self.teksty_wygranej.update()

        if self.stan == self.wszystkie_stany[5]:
            for pp in self.przyciski_pauzy:
                pp.update()

        if self.stan == self.wszystkie_stany[7]:
            self.wyjdz.update()
            for po in self.przyciski_poziomow:
                po.update()

    def czy_przegrana(self):
        for grupa in self.grupy_wrogie:
            if pg.sprite.spritecollideany(self.gracz, grupa):
                return True
        return False

    def przegrana(self):
        self.smierc_gracza.play()
        self.stoper_gry = int(self.stoper_gry*100)/100
        self.stoper_gry = 0
        self.zmien_stan(2)

    def czy_wygrana(self):
        pass
        return pg.sprite.collide_rect(self.gracz, self.meta)

    def wygrana(self):
        self.actual_level.czy_skonczony = True
        self.wejscie_w_meta.play()
        self.stoper_gry = int(self.stoper_gry*100)/100
        self.teksty_wygranej.przygotuj_teksty()
        self.stoper_gry = 0
        self.licznik_gwiazdek.koniec_poziomu()
        self.zmien_stan(3)

    def reset_poziomu(self, poziom):
        self.stoper_gry = 0
        self.zaladuj_gre(poziom)
        self.zmien_stan(1)

    def start_poziomu(self):
        pass
        self.kontynuj_gre()

    def nastepny_poziom(self):
        p = self.znajdz_przycisk_poziom(self.level)
        if p != None:
            p.start_poziom()
        else:
            self.znajdz_przycisk_poziom(-1).start_poziom()

    def zmien_stan(self, stan):
        pass
        self.stan = self.wszystkie_stany[stan]

    def aktualizacja_ekranu(self):
        self.ekran.fill((0,0,0))
        if self.stan == self.wszystkie_stany[0]:
            self.ekran.fill((200, 200, 200))

            for pm in self.przyciski_menu:
                pm.blitme()

        if self.stan == self.wszystkie_stany[1] or self.stan == self.wszystkie_stany[2] or self.stan == self.wszystkie_stany[3]:
            self.ekran.fill((30, 30, 30))

            self.meta.blitme()

            for grupa in self.grupy_w_game_time:
                for obiekt in grupa:
                    obiekt.blitme()

            self.gracz.blitme()

            self.licznik_monet.blitme()
            self.licznik_gwiazdek.blitme()

            self.stoper.blitme()

            self.pauza.blitme()

        if self.stan == self.wszystkie_stany[4]:
            self.ekran.fill((30, 30, 30))

            self.meta.blitme()

            for grupa in self.grupy_w_game_time:
                for obiekt in grupa:
                    obiekt.blitme()

            self.gracz.blitme()

            self.licznik_monet.blitme()
            self.licznik_gwiazdek.blitme()

            self.stoper.blitme()

            self.okno_wygranej.blitme()
            for pw in self.przyciski_wygranej:
                    pw.blitme()
            self.teksty_wygranej.blitme()

        if self.stan == self.wszystkie_stany[5]:
            self.ekran.fill((30, 30, 30))

            self.meta.blitme()

            for grupa in self.grupy_w_game_time:
                for obiekt in grupa:
                    obiekt.blitme()

            self.gracz.blitme()

            self.licznik_monet.blitme()
            self.licznik_gwiazdek.blitme()

            self.stoper.blitme()

            self.pauza.blitme()

            for pp in self.przyciski_pauzy:
                pp.blitme()

        if self.stan == self.wszystkie_stany[6]:
            self.ekran.fill((127,127,127))

            self.wyjdz.blitme()

        if self.stan == self.wszystkie_stany[7]:
            self.ekran.fill((50,50,50))

            self.wyjdz.blitme()

            for po in self.przyciski_poziomow:
                po.blitme()

        pg.display.flip()

    def get_pos_myszy_na_xy(self):
        pass
        return self.center_na_xy(pg.mouse.get_pos())

    def xy_na_center(self, x, y):
        pass
        return self.srodek_ekranu[0]+x,self.srodek_ekranu[1]-y

    def center_na_xy(self, center):
        pass
        return center[0]-self.srodek_ekranu[0],self.srodek_ekranu[1]-center[1]

    def znajdz_klucz(self, kolor):
        for k in self.klucze:
            if k.kolor == kolor:
                return k

    def znajdz_przycisk_poziom(self, id):
        for po in self.przyciski_poziomow:
            if po.id == id:
                return po

if __name__ == "__main__":
    plat = Platformowka()
    plat.start()
