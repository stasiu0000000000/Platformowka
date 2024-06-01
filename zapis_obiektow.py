class ZapisObiektow:

	def __init__(self, plat, poziom):
		self.plat = plat

		self.monety_now = [[False, poziom.monety_dane[i]] for i in range(len(poziom.monety_dane))]
		self.gwiazdki_now = [[False, poziom.gwiazdki_dane[i][:2]] for i in range(len(poziom.gwiazdki_dane))]
		self.klucze_now = [[False, poziom.klucze_drzwi_dane[i][0][:2]] for i in range(len(poziom.klucze_drzwi_dane))]

	def zapis(self):
		self.zapis_monet()
		self.zapis_gwiazdek()
		self.zapis_kluczy()

	def zapis_monet(self):
		for m in self.plat.monety:
			if m.czy_zebrany:
				m_pos = (m.oryginal_x,m.oryginal_y)
				for i, d in enumerate(self.monety_now):
					if d != True:
						if d[1] == m_pos:
							self.monety_now[i][0] = True

	def zapis_gwiazdek(self):
		for g in self.plat.gwiazdki:
			if g.czy_zebrany:
				g_pos = (g.oryginal_x,g.oryginal_y)
				for i, d in enumerate(self.gwiazdki_now):
					if d != True:
						if d[1] == g_pos:
							self.gwiazdki_now[i][0] = True

	def zapis_kluczy(self):
		for k in self.plat.klucze:
			if k.czy_zebrany:
				k_pos = (k.oryginal_x,k.oryginal_y)
				for i, d in enumerate(self.klucze_now):
					if d != True:
						if d[1] == k_pos:
							self.klucze_now[i][0] = True
