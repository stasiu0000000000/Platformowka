import pygame as pg

class Gracz(pg.sprite.Sprite):

    def __init__(self, plat, dane):
        super().__init__()

        self.plat = plat
        self.ekran = self.plat.ekran
        self.ekran_rect = self.plat.ekran_rect
        self.srodek_ekranu = self.plat.srodek_ekranu
        self.fps = self.plat.fps
        self.delta_t = 1/self.fps
        self.kolor = (50,50,255)
        self.speed = 200
        self.size_of_side = 26
        self.grupy_kolidujace = self.plat.grupy_kolidujace_z_graczem
        self.vel = pg.math.Vector2(0,0)
        self.pos = pg.math.Vector2(dane[0],dane[1])
        self.oryginalne_y = self.pos.y

        self.arrows = [0,0,0,0]

        self.grupy_kolidujace = self.plat.grupy_kolidujace_z_graczem

        self.stan_animacji = 0

        self.czas_animacji_przegranej = 1.5
        
        self.czas_animacji_wygranej = 3
        self.ile_skoczyc = 20

        self.image = pg.surface.Surface((self.size_of_side,self.size_of_side))
        self.rect = self.image.get_rect()
        self.blit_rect = pg.Rect(self.rect)

        self.update_pozycji()

    def update_e(self, e):
        keys = pg.key.get_pressed()
        if e.type == pg.KEYDOWN:
            if keys[pg.K_RIGHT] or keys[pg.K_d]:
                self.arrows[0] = 1
            if keys[pg.K_LEFT] or keys[pg.K_a]:
                self.arrows[1] = 1
            if keys[pg.K_UP] or keys[pg.K_w]:
                self.arrows[2] = 1
            if keys[pg.K_DOWN] or keys[pg.K_s]:
                self.arrows[3] = 1
        if e.type == pg.KEYUP:        
            if (not keys[pg.K_RIGHT]) and (not keys[pg.K_d]):
                self.arrows[0] = 0
            if (not keys[pg.K_LEFT]) and (not keys[pg.K_a]):
                self.arrows[1] = 0
            if (not keys[pg.K_UP]) and (not keys[pg.K_w]):
                self.arrows[2] = 0
            if (not keys[pg.K_DOWN]) and (not keys[pg.K_s]):
                self.arrows[3] = 0

    def update(self):
        if self.plat.stan == self.plat.wszystkie_stany[1]:
            self.oryginalne_y = self.pos.y
            self.ruch()
            self.blit_rect = pg.Rect(self.rect)
        if self.plat.stan == self.plat.wszystkie_stany[2]:
            self.animacja_przegrania()
        if self.plat.stan == self.plat.wszystkie_stany[3]:
            self.animacja_wygrania()

        self.update_pozycji()

    def ruch(self):
        self.strzalki = pg.math.Vector2(self.arrows[0]-self.arrows[1],self.arrows[2]-self.arrows[3])
        self.vel = self.strzalki*self.speed*self.delta_t
        self.pos += self.vel
        for g in self.grupy_kolidujace:
            self.kolizje(g)
    
    def kolizje(self, grupa):
        for p in grupa:
            if self.kolizja_z_p(p):
                przeszkoda = p
                typ, strona = self.ktora_strona(przeszkoda)
                if typ == "x":
                    if strona == "right":
                        self.pos.x = self.center_na_pos([przeszkoda.rect.right+self.rect.width/2,0])[0]
                    if strona == "left":
                        self.pos.x = self.center_na_pos([przeszkoda.rect.left-self.rect.width/2,0])[0]
                if typ == "y":
                    if strona == "top":
                        self.pos.y = self.center_na_pos([0,przeszkoda.rect.top-self.rect.height/2])[1]
                    if strona == "bottom":
                        self.pos.y = self.center_na_pos([0,przeszkoda.rect.bottom+self.rect.height/2])[1]

    def ktora_strona(self, przeszkoda):
        krawedzie = przeszkoda.krawedzie
        znajdz_krawedz = przeszkoda.znajdz_krawedz
        lista = self.kolizje_z_k(krawedzie)
        
        if len(lista) == 0:
            pos = self.pos_na_center(self.pos)
            
            to_left = pos[0]-znajdz_krawedz("left").rect.centerx
            to_right = znajdz_krawedz("right").rect.centerx-pos[0]
            to_top = pos[1]-znajdz_krawedz("top").rect.centery
            to_bottom = znajdz_krawedz("bottom").rect.centery-pos[1]

            min_distance = min(to_left,to_right,to_top,to_bottom)
            if min_distance == to_left:
                return ("x", "left")
            elif min_distance == to_right:
                return ("x", "right")
            elif min_distance == to_top:
                return ("y", "top")
            elif min_distance == to_bottom:
                return ("y", "bottom")

        elif len(lista) == 1:
            return (lista[0].typ, lista[0].strona)

        elif len(lista) == 2:
            if {"x","y"} == {lista[0].typ,lista[1].typ}:
                if lista[0].typ == "x":
                    krawedz_x, krawedz_y = lista
                else:
                    krawedz_y, krawedz_x = lista
                
                pos = self.pos_na_center(self.pos)
                if krawedz_x.strona == "right":
                    glebokosc_x = abs(pos[0]-self.rect.width/2 - krawedz_x.rect.right)
                if krawedz_x.strona == "left":
                    glebokosc_x = abs(pos[0]+self.rect.width/2 - krawedz_x.rect.left)

                if krawedz_y.strona == "top":
                    glebokosc_y = abs(pos[1]+self.rect.width/2 - krawedz_x.rect.top)
                if krawedz_y.strona == "bottom":
                    glebokosc_y = abs(pos[1]-self.rect.width/2 - krawedz_x.rect.bottom)

                if glebokosc_x < glebokosc_y:
                    return ("x", krawedz_x.strona)
                else:
                    return ("y", krawedz_y.strona)

            elif ("x","x") == (lista[0].typ,lista[1].typ):
                if lista[0].strona == "right":
                    krawedz_right, krawedz_left = lista
                else:
                    krawedz_left, krawedz_right = lista

                x = self.pos_na_center(self.pos)[0]
                glebokosc_right = przeszkoda.rect.right-(x-self.rect.width/2)
                glebokosc_left = (x+self.rect.width/2)-przeszkoda.rect.left

                if glebokosc_right < glebokosc_left:
                    return ("x", "right")
                else:
                    return ("x", "left")
            
            elif ("y","y") == (lista[0].typ,lista[1].typ):
                if lista[0].strona == "top":
                    krawedz_top = lista[0]
                else:
                    krawedz_bottom = lista[0]

                y = self.pos_na_center(self.pos)[1]
                glebokosc_top = przeszkoda.rect.top-(y+self.rect.width/2)
                glebokosc_bottom = (y-self.rect.width/2)-przeszkoda.rect.bottom

                if glebokosc_top > glebokosc_bottom:
                    return ("y", "top")
                else:
                    return ("y", "bottom")
        
        elif len(lista) == 3:
            x = y = 0
            for k in lista:
                if k.typ == "x":
                    x += 1
                elif k.typ == "y":
                    y += 1

            if x == 1:
                krawedz_x = None
                for k in lista:
                    if k.typ == "x":
                        krawedz_x = k
                czy_top = abs(self.pos_na_center(pg.math.Vector2(0,self.pos.y+self.rect.height/2))[1] - przeszkoda.rect.bottom) <= self.vel.y
                    
                czy_bottom = abs(przeszkoda.rect.top - self.pos_na_center(pg.math.Vector2(0,self.pos.y-self.rect.height/2))[1]) <= -self.vel.y
                    
                if (not czy_top) and (not czy_bottom):
                    return ("x", krawedz_x.strona)
                else:
                    glebokosc_top = (self.pos_na_center(self.pos)[1]-self.rect.height/2)-przeszkoda.rect.top
                    glebokosc_bottom = przeszkoda.rect.bottom-(self.pos_na_center(self.pos)[1]+self.rect.height/2)
                        
                    if glebokosc_top < glebokosc_bottom:
                        return ("y", "top")
                    else:
                        return ("y", "bottom")

            elif y == 1:
                krawedz_y = None
                for k in lista:
                    if k.typ == "y":
                        krawedz_y = k
                czy_right = abs(self.pos_na_center(pg.math.Vector2(self.pos.x+self.rect.width/2,0))[0] - przeszkoda.rect.left) <= self.vel.x
                    
                czy_left = abs(przeszkoda.rect.right - self.pos_na_center(pg.math.Vector2(self.pos.x-self.rect.width/2,0))[0]) <= -self.vel.x
              
                if (not czy_right) and (not czy_left):
                    return ("y", krawedz_y.strona)
                else:
                    glebokosc_right = (self.pos_na_center(self.pos)[0]+self.rect.width/2)-przeszkoda.rect.left
                    glebokosc_left = przeszkoda.rect.right-(self.pos_na_center(self.pos)[0]-self.rect.width/2)
                        
                    if glebokosc_right > glebokosc_left:
                        return ("x", "right")
                    else:
                        return ("x", "left")

        elif len(lista) == 4:
            glebokosc_right = self.pos_na_center(pg.math.Vector2(self.pos.x+self.rect.width/2,0))[0] - przeszkoda.rect.left
            glebokosc_left = przeszkoda.rect.right - self.pos_na_center(pg.math.Vector2(self.pos.x-self.rect.width/2,0))[0]
            glebokosc_top = przeszkoda.rect.bottom - self.pos_na_center(pg.math.Vector2(0,self.pos.y+self.rect.height/2))[1]
            glebokosc_bottom = self.pos_na_center(pg.math.Vector2(0,self.pos.y-self.rect.height/2))[1] - przeszkoda.rect.top
            max_glebokosc = max(glebokosc_right, glebokosc_left, glebokosc_top,glebokosc_bottom)
            if glebokosc_right == max_glebokosc:
                return ("x", "right")
            elif glebokosc_left == max_glebokosc:
                return ("x", "left")
            elif glebokosc_top == max_glebokosc:
                return ("y", "top")
            elif glebokosc_bottom == max_glebokosc:
                return ("y", "bottom")

    def kolizja_z_p(self, przeszkoda):
        try:
            czy_aktywny = przeszkoda.czy_aktywny
        except:
            czy_aktywny = True
        return self.kolizja_z_obiekt(przeszkoda) and czy_aktywny
 
    def kolizje_z_k(self, krawedzie):
        lista = []
        for k in krawedzie:
            if self.kolizja_z_obiekt(k):
                lista.append(k)
        return lista

    def kolizja_z_obiekt(self, obiekt):
        pos = self.pos_na_center(self.pos)
        rect = pg.Rect(0,0,self.rect.width,self.rect.height)
        rect.center = (pos)
        return obiekt.rect.colliderect(rect)

    def update_pozycji(self):
        self.rect.center = self.pos_na_center(self.pos)

    def animacja_przegrania(self):
        if self.stan_animacji-1/5 >= 1:
            self.stan_animacji = 0
            self.blit_rect = pg.Rect(self.rect)
            self.image = pg.transform.scale(self.image, self.rect.size)
            self.plat.zmien_stan(1)
            self.plat.start_poziomu()
            return

        self.blit_rect.width = self.blit_rect.height = self.size_of_side * (1-self.stan_animacji)
        self.image = pg.transform.scale(self.image, (max(self.blit_rect.width,0),max(self.blit_rect.height,0)))
        self.stan_animacji += 1/self.fps/self.czas_animacji_przegranej

    def animacja_wygrania(self):
        x = self.stan_animacji
        if self.stan_animacji < 1/3:
            self.pos.y = (-36*x**2 + 12*x)*self.ile_skoczyc + self.oryginalne_y
            self.update_pozycji()

        elif self.stan_animacji < 2/3:
            x -= 1/3
            self.pos.y = (-36*x**2 + 12*x)*self.ile_skoczyc + self.oryginalne_y

        elif self.stan_animacji < 1:
            self.image.set_alpha((1-(3*x-2))*255)

        else:
            self.stan_animacji = 0
            self.image.set_alpha(0)
            self.plat.zmien_stan(4)
            return

        self.stan_animacji += 1/self.fps/self.czas_animacji_wygranej

    def blitme(self):
        self.image.fill(self.kolor)
        self.ekran.blit(self.image,self.blit_rect)

    def pos_na_center(self, pos):
        return self.srodek_ekranu[0]+pos.x,self.srodek_ekranu[1]-pos.y

    def center_na_pos(self, center):
        return pg.math.Vector2(center[0]-self.srodek_ekranu[0],self.srodek_ekranu[1]-center[1])
