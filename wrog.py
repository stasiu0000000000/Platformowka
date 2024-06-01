import pygame as pg

class Wrog(pg.sprite.Sprite):

    def __init__(self, plat, dane):
        super().__init__()

        self.plat = plat
        self.ekran = self.plat.ekran
        self.ekran_rect = self.plat.ekran_rect
        self.srodek_ekranu = self.plat.srodek_ekranu
        self.fps = self.plat.fps
        self.delta_t = 1/self.fps
        self.grupy_kolidujace = self.plat.grupy_kolidujace_z_graczem
        self.speed = 130
        self.x = dane[0]
        self.y = dane[1]
        self.kolor = (255,0,0)

        self.dir = 0

        self.rect = pg.Rect(0,0,35,35)

        self.update_pozycji()

    def update(self):
        self.ruch()

        self.update_pozycji()

    def update_pozycji(self):
        self.rect.center = self.xy_na_center(self.x, self.y)

    def ruch(self):
        me_to_player = pg.math.Vector2(self.plat.gracz.pos-(self.x,self.y)).normalize()
        self.vel = me_to_player*self.speed*self.delta_t
        self.x += self.vel.x
        self.y += self.vel.y
        for g in self.grupy_kolidujace:
            self.kolizje(g)

    def kolizje(self, grupa):
        for p in grupa:
            if self.kolizja_z_p(p):
                przeszkoda = p
                typ, strona = self.ktora_strona(przeszkoda)
                if typ == "x":
                    if strona == "right":
                        self.x = self.center_na_xy([przeszkoda.rect.right+self.rect.width/2,0])[0]
                    if strona == "left":
                        self.x = self.center_na_xy([przeszkoda.rect.left-self.rect.width/2,0])[0]
                if typ == "y":
                    if strona == "top":
                        self.y = self.center_na_xy([0,przeszkoda.rect.top-self.rect.height/2])[1]
                    if strona == "bottom":
                        self.y = self.center_na_xy([0,przeszkoda.rect.bottom+self.rect.height/2])[1]

    def ktora_strona(self, przeszkoda):
        krawedzie = przeszkoda.krawedzie
        znajdz_krawedz = przeszkoda.znajdz_krawedz
        lista = self.kolizje_z_k(krawedzie)
        
        if len(lista) == 0:
            pos = self.xy_na_center(self.x,self.y)
            
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
            if set(("x","y")) == set((lista[0].typ,lista[1].typ)):
                if lista[0].typ == "x":
                    krawedz_x, krawedz_y = lista
                else:
                    krawedz_y, krawedz_x = lista
                
                pos = self.xy_na_center(self.x,self.y)
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

            elif set(("x","x")) == set((lista[0].typ,lista[1].typ)):
                if lista[0].strona == "right":
                    krawedz_right, krawedz_left = lista
                else:
                    krawedz_left, krawedz_right = lista

                x = self.xy_na_center(self.x,self.y)[0]
                glebokosc_right = przeszkoda.rect.right-(x-self.rect.width/2)
                glebokosc_left = (x+self.rect.width/2)-przeszkoda.rect.left

                if glebokosc_right < glebokosc_left:
                    return ("x", "right")
                else:
                    return ("x", "left")
            
            elif set(("y","y")) == set((lista[0].typ,lista[1].typ)):
                if lista[0].strona == "top":
                    krawedz_top = lista[0]
                else:
                    krawedz_bottom = lista[0]

                y = self.xy_na_center(self.x,self.y)[1]
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
                czy_top = abs(self.xy_na_center(pg.math.Vector2(0,self.y+self.rect.height/2))[1] - przeszkoda.rect.bottom) <= self.vel.y
                    
                czy_bottom = abs(przeszkoda.rect.top - self.xy_na_center(pg.math.Vector2(0,self.y-self.rect.height/2))[1]) <= -self.vel.y
                    
                if (not czy_top) and (not czy_bottom):
                    return ("x", krawedz_x.strona)
                else:
                    glebokosc_top = (self.xy_na_center(0,self.y)[1]-self.rect.height/2)-przeszkoda.rect.top
                    glebokosc_bottom = przeszkoda.rect.bottom-(self.xy_na_center(0,self.y)[1]+self.rect.height/2)
                        
                    if glebokosc_top < glebokosc_bottom:
                        return ("y", "top")
                    else:
                        return ("y", "bottom")

            elif y == 1:
                krawedz_y = None
                for k in lista:
                    if k.typ == "y":
                        krawedz_y = k
                czy_right = abs(self.xy_na_center(self.x+self.rect.width/2,0)[0] - przeszkoda.rect.left) <= self.vel.x
                    
                czy_left = abs(przeszkoda.rect.right - self.xy_na_center(pg.math.Vector2(self.x-self.rect.width/2,0))[0]) <= -self.vel.x

                print(czy_right, czy_left)
                    
                if (not czy_right) and (not czy_left):
                    return ("y", krawedz_y.strona)
                else:
                    glebokosc_right = (self.xy_na_center(self.x,0)[0]+self.rect.width/2)-przeszkoda.rect.left
                    glebokosc_left = przeszkoda.rect.right-(self.xy_na_center(self.x,0)[0]-self.rect.width/2)
                        
                    if glebokosc_right > glebokosc_left:
                        return ("x", "right")
                    else:
                        return ("x", "left")

        elif len(lista) == 4:
            glebokosc_right = self.xy_na_center(pg.math.Vector2(self.x+self.rect.width/2,0))[0] - przeszkoda.rect.left
            glebokosc_left = przeszkoda.rect.right - self.xy_na_center(pg.math.Vector2(self.x-self.rect.width/2,0))[0]
            glebokosc_top = przeszkoda.rect.bottom - self.xy_na_center(pg.math.Vector2(0,self.y+self.rect.height/2))[1]
            glebokosc_bottom = self.xy_na_center(pg.math.Vector2(0,self.y-self.rect.height/2))[1] - przeszkoda.rect.top
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
        x, y = self.xy_na_center(self.x, self.y)
        rect = pg.Rect(x-self.rect.width/2,y-self.rect.height/2,self.rect.width,self.rect.height)
        return obiekt.rect.colliderect(rect)

    def blitme(self):
        self.ekran.fill(self.kolor, self.rect)

    def xy_na_center(self, x, y):
        return self.srodek_ekranu[0]+x,self.srodek_ekranu[1]-y

    def center_na_xy(self, center):
        return center[0]-self.srodek_ekranu[0],self.srodek_ekranu[1]-center[1]
