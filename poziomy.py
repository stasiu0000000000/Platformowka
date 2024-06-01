class PoziomSzkielet:

	def __init__(self, plat):
		self.plat = plat
		self.srodek_ekranu = self.plat.srodek_ekranu

		self.gracz_dane = (0,0)
		self.meta_dane = (0,0,1,1)

		self.przeszkody_dane = self.klucze_drzwi_dane = self.monety_dane = self.gwiazdki_dane = self.teleportery_dane = self.zle_sciany_dane = self.wrogowie_dane = self.dzialka_dane = self.strzelcy_dane = ()

		self.gracz_dane = ("gracz_x","gracz_y")

		self.meta_dane = ("meta_x", "meta_y", "meta_width", "meta_height")

		"""Przeszkody ograniczające okno
		self.przeszkody_dane = (
		 	(-self.srodek_ekranu[0]+25,0,50,self.srodek_ekranu[1]*2),
			(self.srodek_ekranu[0]-25,0,50,self.srodek_ekranu[1]*2),
		   	(0,self.srodek_ekranu[1]-25,self.srodek_ekranu[0]*2,50),
		   	(0,-self.srodek_ekranu[1]+25,self.srodek_ekranu[0]*2,50))"""

		self.przeszkody_dane = (
		    ("przeszkoda1_x","przeszkoda1_y","przeszkoda1_width","przeszkoda1_height"),
		   	("przeszkoda2_x","przeszkoda2_y","przeszkoda2_width","przeszkoda2_height"),
		   	("przeszkoda3_x","przeszkoda3_y","przeszkoda3_width","przeszkoda3_height"))

		self.klucze_drzwi_dane = (
			 (("klucz1_x","klucz1_y","klucz1_kolor"),
			 (("drzwi11_x","drzwi11_y","drzwi11_width","drzwi11_height","klucz1_kolor"),
			  ("drzwi12_x","drzwi12_y","drzwi12_width","drzwi12_height","klucz1_kolor"))),

			 (("klucz2_x","klucz2_y","klucz2_kolor"),
			  ("drzwi21_x","drzwi21_y","drzwi21_width","drzwi21_height","klucz2_kolor"),
			  ("drzwi22_x","drzwi22_y","drzwi22_width","drzwi22_height","klucz2_kolor")))

		self.monety_dane = (
			("moneta1_x","moneta1_y"),
		   	("moneta2_x","moneta2_y"),
		   	("moneta3_x","moneta3_y"))

		self.gwiazdki_dane = (
			("gwiazdka1_x","gwiazdka1_y"),
		   	("gwiazdka2_x","gwiazdka2_y"),
		   	("gwiazdka3_x","gwiazdka3_y"))

		self.teleportery_dane = (
			 (("teleporter1a_x","teleporter1a_y"),("teleporter1b_x","teleporter1b_y"),"teleportery1_kolor", "teleportery1_czas_resetowania"),
			 (("teleporter2a_x","teleporter2a_y"),("teleporter2b_x","teleporter2b_y"),"teleportery2_kolor", "teleportery2_czas_resetowania"))

		self.zle_sciany_dane = (
		    ("zla_sciana1_x","zla_sciana1_y","zla_sciana1_width","zla_sciana1_height"),
		   	("zla_sciana2_x","zla_sciana2_y","zla_sciana2_width","zla_sciana2_height"),
		   	("zla_sciana3_x","zla_sciana3_y","zla_sciana3_width","zla_sciana3_height"))

		self.wrogowie_dane = (
			("wrog1_x","wrog1_y"),
		   	("wrog2_x","wrog2_y"),
		   	("wrog3_x","wrog3_y"))

		self.dzialka_dane = (
			("dzialko1_x","dzialko1_y"),
		   	("dzialko2_x","dzialko2_y"),
		   	("dzialko3_x","dzialko3_y"))

		self.strzelcy_dane = (
			("strzelec1_x","strzelec1_y"),
		   	("strzelec2_x","strzelec2_y"),
		   	("strzelec3_x","strzelec3_y"))

	def get_kordynaty_gracza(self):
		return self.gracz_dane

class Poziom11:

	def __init__(self, plat):
		self.plat = plat
		self.srodek_ekranu = self.plat.srodek_ekranu

		self.gracz_dane = (0,0)
		self.meta_dane = (0,0,1,1)

		self.przeszkody_dane = self.klucze_drzwi_dane = self.monety_dane = self.gwiazdki_dane = self.teleportery_dane = self.zle_sciany_dane = self.wrogowie_dane = self.dzialka_dane = self.strzelcy_dane = ()

		self.gracz_dane = (0,350)

		self.meta_dane = (0, -358, 90, 69)

		self.przeszkody_dane = (
		 	(-self.srodek_ekranu[0]+5,0,10,self.srodek_ekranu[1]*2),
			(self.srodek_ekranu[0]-5,0,10,self.srodek_ekranu[1]*2),
		   	(0,self.srodek_ekranu[1]-5,self.srodek_ekranu[0]*2,10),
		   	(0,-self.srodek_ekranu[1]+5,self.srodek_ekranu[0]*2,10),
			(-436,351,10,79),(-119,351,10,79))

	def get_kordynaty_gracza(self):
		return self.gracz_dane
