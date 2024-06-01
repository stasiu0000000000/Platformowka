class Poziom1:

	def __init__(self, plat):
		self.plat = plat
		self.srodek_ekranu = self.plat.srodek_ekranu

		self.gracz_dane = (0,0)
		self.meta_dane = (0,0,1,1)
		
		self.przeszkody_dane = self.klucze_drzwi_dane = self.monety_dane = self.gwiazdki_dane = self.teleportery_dane = self.zle_sciany_dane = self.wrogowie_dane = self.dzialka_dane = self.strzelcy_dane = ()

		self.gracz_dane = (-300,0)

		self.meta_dane = (450, 0, 200, 700)

		self.przeszkody_dane = (
		 	(-self.srodek_ekranu[0]+25,0,50,self.srodek_ekranu[1]*2),
			(self.srodek_ekranu[0]-25,0,50,self.srodek_ekranu[1]*2),
		   	(0,self.srodek_ekranu[1]-25,self.srodek_ekranu[0]*2,50),
		   	(0,-self.srodek_ekranu[1]+25,self.srodek_ekranu[0]*2,50))

	def get_kordynaty_gracza(self):
		return self.gracz_dane

class Poziom2:

	def __init__(self, plat):
		self.plat = plat
		self.srodek_ekranu = self.plat.srodek_ekranu

		self.gracz_dane = (0,0)
		self.meta_dane = (0,0,1,1)
		
		self.przeszkody_dane = self.klucze_drzwi_dane = self.monety_dane = self.gwiazdki_dane = self.teleportery_dane = self.zle_sciany_dane = self.wrogowie_dane = self.dzialka_dane = self.strzelcy_dane = ()

		self.przeszkody_dane = (
		 	(-self.srodek_ekranu[0]+25,0,50,self.srodek_ekranu[1]*2),
			(self.srodek_ekranu[0]-25,0,50,self.srodek_ekranu[1]*2),
		   	(0,self.srodek_ekranu[1]-25,self.srodek_ekranu[0]*2,50),
		   	(0,-self.srodek_ekranu[1]+25,self.srodek_ekranu[0]*2,50),
		   	(-200,-87,50,625),(0,87,50,625),(200,-87,50,625))

		self.gracz_dane = (-438,0)

		self.meta_dane = (450, 0, 200, 700)

		self.przeszkody_dane = (
		 	(-575,0,50,800),(575,0,50,800),
		   	(0,375,1200,50),(0,-375,1200,50),
		   	(-300,-87,50,625),
		   	(-100,87,50,625),
		   	(100,-87,50,625))

	def get_kordynaty_gracza(self):
		return self.gracz_dane

class Poziom3:

	def __init__(self, plat):
		self.plat = plat
		self.srodek_ekranu = self.plat.srodek_ekranu

		self.gracz_dane = (0,0)
		self.meta_dane = (0,0,1,1)
		
		self.przeszkody_dane = self.klucze_drzwi_dane = self.monety_dane = self.gwiazdki_dane = self.teleportery_dane = self.zle_sciany_dane = self.wrogowie_dane = self.dzialka_dane = self.strzelcy_dane = ()

		self.przeszkody_dane = (
		 	(-self.srodek_ekranu[0]+25,0,50,self.srodek_ekranu[1]*2),
			(self.srodek_ekranu[0]-25,0,50,self.srodek_ekranu[1]*2),
		   	(0,self.srodek_ekranu[1]-25,self.srodek_ekranu[0]*2,50),
		   	(0,-self.srodek_ekranu[1]+25,self.srodek_ekranu[0]*2,50))

		self.gracz_dane = (-438,0)

		self.meta_dane = (450, 0, 200, 700)

		self.przeszkody_dane = (
		 	(-575,0,50,800),(575,0,50,800),
		   	(0,375,1200,50),(0,-375,1200,50),)

		self.zle_sciany_dane = (
		   	(-300,-62,50,575),
		   	(-100,63,50,575),
		   	(100,-62,50,575))

	def get_kordynaty_gracza(self):
		return self.gracz_dane

class Poziom4:

	def __init__(self, plat):
		self.plat = plat
		self.srodek_ekranu = self.plat.srodek_ekranu

		self.gracz_dane = (0,0)
		self.meta_dane = (0,0,1,1)
		
		self.przeszkody_dane = self.klucze_drzwi_dane = self.monety_dane = self.gwiazdki_dane = self.teleportery_dane = self.zle_sciany_dane = self.wrogowie_dane = self.dzialka_dane = self.strzelcy_dane = ()

		self.gracz_dane = (-300,0)

		self.meta_dane = (450, 0, 200, 700)

		self.przeszkody_dane = (
		 	(-self.srodek_ekranu[0]+25,0,50,self.srodek_ekranu[1]*2),
			(self.srodek_ekranu[0]-25,0,50,self.srodek_ekranu[1]*2),
		   	(0,self.srodek_ekranu[1]-25,self.srodek_ekranu[0]*2,50),
		   	(0,-self.srodek_ekranu[1]+25,self.srodek_ekranu[0]*2,50),
		   	(0,0,100,100))
		
		self.wrogowie_dane = ((300,100),(300,-100),)

	def get_kordynaty_gracza(self):
		return self.gracz_dane

class Poziom5:

	def __init__(self, plat):
		self.plat = plat
		self.srodek_ekranu = self.plat.srodek_ekranu

		self.gracz_dane = (0,0)
		self.meta_dane = (0,0,1,1)

		self.przeszkody_dane = self.klucze_drzwi_dane = self.monety_dane = self.gwiazdki_dane = self.teleportery_dane = self.zle_sciany_dane = self.wrogowie_dane = self.dzialka_dane = self.strzelcy_dane = ()

		self.gracz_dane = (-300,0)

		self.meta_dane = (450, 0, 200, 700)

		self.przeszkody_dane = (
		 	(-self.srodek_ekranu[0]+25,0,50,self.srodek_ekranu[1]*2),
			(self.srodek_ekranu[0]-25,0,50,self.srodek_ekranu[1]*2),
		   	(0,self.srodek_ekranu[1]-25,self.srodek_ekranu[0]*2,50),
		   	(0,-self.srodek_ekranu[1]+25,self.srodek_ekranu[0]*2,50))

		self.dzialka_dane = ((200,250),(200,-250),(200,0))

	def get_kordynaty_gracza(self):
		return self.gracz_dane

class Poziom6:

	def __init__(self, plat):
		self.plat = plat
		self.srodek_ekranu = self.plat.srodek_ekranu

		self.gracz_dane = (0,0)
		self.meta_dane = (0,0,1,1)

		self.przeszkody_dane = self.klucze_drzwi_dane = self.monety_dane = self.gwiazdki_dane = self.teleportery_dane = self.zle_sciany_dane = self.wrogowie_dane = self.dzialka_dane = self.strzelcy_dane = ()

		self.gracz_dane = (-400,0)

		self.meta_dane = (450, 0, 200, 700)

		self.przeszkody_dane = (
		 	(-self.srodek_ekranu[0]+25,0,50,self.srodek_ekranu[1]*2),
			(self.srodek_ekranu[0]-25,0,50,self.srodek_ekranu[1]*2),
		   	(0,self.srodek_ekranu[1]-25,self.srodek_ekranu[0]*2,50),
		   	(0,-self.srodek_ekranu[1]+25,self.srodek_ekranu[0]*2,50),
		   	(-200,63,50,575),(0,-63,50,575),(200,63,50,575))

		self.klucze_drzwi_dane = (
			 ((-300,300,"czerwony"),
			 ((-200,-287,50,125,"czerwony"),)),

			 ((-100,-300,"zolty"),
			 ((0,287,50,125,"zolty"),)),

			 ((100,300,"zielony"),
			 ((200,-287,50,125,"zielony"),)))

	def get_kordynaty_gracza(self):
		return self.gracz_dane

class Poziom7:

	def __init__(self, plat):
		self.plat = plat
		self.srodek_ekranu = self.plat.srodek_ekranu

		self.gracz_dane = (0,0)
		self.meta_dane = (0,0,1,1)

		self.przeszkody_dane = self.klucze_drzwi_dane = self.monety_dane = self.gwiazdki_dane = self.teleportery_dane = self.zle_sciany_dane = self.wrogowie_dane = self.dzialka_dane = self.strzelcy_dane = ()

		self.gracz_dane = (-450,-250)

		self.meta_dane = (475, -275, 150, 150)

		self.przeszkody_dane = (
		 	(-self.srodek_ekranu[0]+25,0,50,self.srodek_ekranu[1]*2),
			(self.srodek_ekranu[0]-25,0,50,self.srodek_ekranu[1]*2),
		   	(0,self.srodek_ekranu[1]-25,self.srodek_ekranu[0]*2,50),
		   	(0,-self.srodek_ekranu[1]+25,self.srodek_ekranu[0]*2,50),
			(-350,225,400,400),(350,225,400,500),(0,-125,450,450))

		self.teleportery_dane = (((-350,-250),(-75,200),"cyan",3),((75,200),(350,-250),"czerwony",3))

	def get_kordynaty_gracza(self):
		return self.gracz_dane

class Poziom8:

	def __init__(self, plat):
		self.plat = plat
		self.srodek_ekranu = self.plat.srodek_ekranu

		self.gracz_dane = (0,0)
		self.meta_dane = (0,0,1,1)

		self.przeszkody_dane = self.klucze_drzwi_dane = self.monety_dane = self.gwiazdki_dane = self.teleportery_dane = self.zle_sciany_dane = self.wrogowie_dane = self.dzialka_dane = self.strzelcy_dane = ()

		self.gracz_dane = (-500,300)

		self.meta_dane = (125, 0, 200, 700)

		self.przeszkody_dane = (
		 	(-self.srodek_ekranu[0]+25,0,50,self.srodek_ekranu[1]*2),
			(self.srodek_ekranu[0]-25,0,50,self.srodek_ekranu[1]*2),
		   	(0,self.srodek_ekranu[1]-25,self.srodek_ekranu[0]*2,50),
		   	(0,-self.srodek_ekranu[1]+25,self.srodek_ekranu[0]*2,50),
		   	(0,0,50,self.srodek_ekranu[1]*2))

		self.zle_sciany_dane = ((450, 0, 200, 700),)

		self.teleportery_dane = (((-100,-300),(300,0),"cyan", 3),)

		self.strzelcy_dane = ((-300,350),(-300,-350))

	def get_kordynaty_gracza(self):
		return self.gracz_dane

class Poziom9:

	def __init__(self, plat):
		self.plat = plat
		self.srodek_ekranu = self.plat.srodek_ekranu

		self.gracz_dane = (0, 0)
		self.meta_dane = (0, 0, 1, 1)

		self.przeszkody_dane = self.klucze_drzwi_dane = self.monety_dane = self.gwiazdki_dane = self.teleportery_dane = self.zle_sciany_dane = self.wrogowie_dane = self.dzialka_dane = self.strzelcy_dane = ()

		self.gracz_dane = (-300, 0)

		self.meta_dane = (450, 0, 200, 700)

		self.przeszkody_dane = (
			(-self.srodek_ekranu[0] + 25, 0, 50, self.srodek_ekranu[1] * 2),
			(self.srodek_ekranu[0] - 25, 0, 50, self.srodek_ekranu[1] * 2),
			(0, self.srodek_ekranu[1] - 25, self.srodek_ekranu[0] * 2, 50),
			(0, -self.srodek_ekranu[1] + 25, self.srodek_ekranu[0] * 2, 50))

	def get_kordynaty_gracza(self):
		return self.gracz_dane

class Poziom10:

	def __init__(self, plat):
		self.plat = plat
		self.srodek_ekranu = self.plat.srodek_ekranu

		self.gracz_dane = (0, 0)
		self.meta_dane = (0, 0, 1, 1)

		self.przeszkody_dane = self.klucze_drzwi_dane = self.monety_dane = self.gwiazdki_dane = self.teleportery_dane = self.zle_sciany_dane = self.wrogowie_dane = self.dzialka_dane = self.strzelcy_dane = ()

		self.gracz_dane = (-300, 0)

		self.meta_dane = (450, 0, 200, 700)

		self.przeszkody_dane = (
			(-self.srodek_ekranu[0] + 25, 0, 50, self.srodek_ekranu[1] * 2),
			(self.srodek_ekranu[0] - 25, 0, 50, self.srodek_ekranu[1] * 2),
			(0, self.srodek_ekranu[1] - 25, self.srodek_ekranu[0] * 2, 50),
			(0, -self.srodek_ekranu[1] + 25, self.srodek_ekranu[0] * 2, 50))

	def get_kordynaty_gracza(self):
		return self.gracz_dane

class Poziom11:

	def __init__(self, plat):
		self.plat = plat
		self.srodek_ekranu = self.plat.srodek_ekranu

		self.gracz_dane = (0, 0)
		self.meta_dane = (0, 0, 1, 1)

		self.przeszkody_dane = self.klucze_drzwi_dane = self.monety_dane = self.gwiazdki_dane = self.teleportery_dane = self.zle_sciany_dane = self.wrogowie_dane = self.dzialka_dane = self.strzelcy_dane = ()

		self.gracz_dane = (-300, 0)

		self.meta_dane = (450, 0, 200, 700)

		self.przeszkody_dane = (
			(-self.srodek_ekranu[0] + 25, 0, 50, self.srodek_ekranu[1] * 2),
			(self.srodek_ekranu[0] - 25, 0, 50, self.srodek_ekranu[1] * 2),
			(0, self.srodek_ekranu[1] - 25, self.srodek_ekranu[0] * 2, 50),
			(0, -self.srodek_ekranu[1] + 25, self.srodek_ekranu[0] * 2, 50))

	def get_kordynaty_gracza(self):
		return self.gracz_dane

class Poziom12:

	def __init__(self, plat):
		self.plat = plat
		self.srodek_ekranu = self.plat.srodek_ekranu

		self.gracz_dane = (0,0)
		self.meta_dane = (0,0,1,1)
		
		self.przeszkody_dane = self.klucze_drzwi_dane = self.monety_dane = self.gwiazdki_dane = self.teleportery_dane = self.zle_sciany_dane = self.wrogowie_dane = self.dzialka_dane = self.strzelcy_dane = ()

		self.gracz_dane = (-300,0)

		self.meta_dane = (450, 0, 200, 700)

		self.przeszkody_dane = (
		 	(-self.srodek_ekranu[0]+25,0,50,self.srodek_ekranu[1]*2),
			(self.srodek_ekranu[0]-25,0,50,self.srodek_ekranu[1]*2),
		   	(0,self.srodek_ekranu[1]-25,self.srodek_ekranu[0]*2,50),
		   	(0,-self.srodek_ekranu[1]+25,self.srodek_ekranu[0]*2,50))

		self.dzialka_dane = (tuple((320,y) for y in range(-350,351,10)))

	def get_kordynaty_gracza(self):
		return self.gracz_dane


class PoziomYouWin:

	def __init__(self, plat):
		self.plat = plat
		self.srodek_ekranu = self.plat.srodek_ekranu

		self.gracz_dane = (0,0)
		self.meta_dane = (0,0,1,1)
		
		self.przeszkody_dane = self.klucze_drzwi_dane = self.monety_dane = self.gwiazdki_dane = self.teleportery_dane = self.zle_sciany_dane = self.wrogowie_dane = self.dzialka_dane = self.strzelcy_dane = ()

		self.gracz_dane = (0,-300)

		self.meta_dane = (self.srodek_ekranu[0]*2, 0, 1, 1)

		self.przeszkody_dane = (
		 	(-self.srodek_ekranu[0]+25,0,50,self.srodek_ekranu[1]*2),
			(self.srodek_ekranu[0]-25,0,50,self.srodek_ekranu[1]*2),
		   	(0,self.srodek_ekranu[1]-25,self.srodek_ekranu[0]*2,50),
		   	(0,-self.srodek_ekranu[1]+25,self.srodek_ekranu[0]*2,50))

		self.dzialka_dane = ((-460,75),(-438,75),(-416,75),(-394,75),(-372,75),(-350,75),(-406,55),(-406,35),(-406,15),(-406,-5),(-406,-25),(-406,-45),(-406,-65),(-406,-85),(-308,75),(-308,55),(-308,35),(-308,15),(-308,-5),(-308,-25),(-308,-45),(-308,-65),(-308,-85),(-208,75),(-208,55),(-208,35),(-208,15),(-208,-5),(-208,-25),(-208,-45),(-208,-65),(-208,-85),(-258,4),(-238,4),(-218,4),(-258,4),(-278,4),(-298,4),(-143,75),(-123,75),(-103,75),(-83,75),(-63,75),(-143,-75),(-123,-75),(-103,-75),(-83,-75),(-63,-75),(-143,5),(-123,5),(-103,5),(-83,5),(-63,5),(-143,25),(-142,40),(-142,60),(-142,-55),(-142,-35),(-142,-15),(48,75),(68,75),(88,75),(108,75),(128,75),(48,-75),(68,-75),(88,-75),(108,-75),(128,-75),(48,5),(68,5),(88,5),(108,5),(128,5),(48,25),(48,40),(48,60),(48,-55),(48,-35),(48,-15),(178,75),(178,55),(178,35),(178,15),(178,-5),(178,-25),(178,-45),(178,-65),(178,-85),(284,75),(284,55),(284,35),(284,15),(284,-5),(284,-25),(284,-45),(284,-65),(284,-85),(192,70),(200,57),(208,44),(216,31),(224,18),(232,3),(240,-13),(248,-27),(256,-40),(264,-55),(272,-70),(350,80),(350,60),(350,40),(350,20),(350,0),(350,-20),(350,-40),(350,-60),(350,-80),(370,75),(390,75),(370,-75),(390,-75),(407,-72),(425,-67),(442,-55),(450,-38),(407,72),(425,65),(442,55),(449,39),(455,25),(455,-25),(457,-15),(458,0),(457,15))

	def get_kordynaty_gracza(self):
		return self.gracz_dane
