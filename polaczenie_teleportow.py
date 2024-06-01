import pygame as pg

class PolaczenieTeleportow:

	def __init__(self, plat, teleport_a, teleport_b, czas_oczekiwania):
		self.plat = plat
		self.delta_time = self.plat.delta_time
		self.teleport_a = teleport_a
		self.teleport_b = teleport_b
		self.czas_oczekiwania = czas_oczekiwania
		self.czas_do_naladowania = 0

		self.gracz_wszedl_teleport_a = False
		self.gracz_wszedl_teleport_b = False

	def update(self):
		self.gracz_wszedl_teleport_a = self.teleport_a.czy_teleportacja()
		self.gracz_wszedl_teleport_b = self.teleport_b.czy_teleportacja()

		if self.gracz_wszedl_teleport_a and self.czas_do_naladowania == 0:
			self.plat.gracz.pos.x = self.teleport_b.x
			self.plat.gracz.pos.y = self.teleport_b.y
			self.czas_do_naladowania = self.czas_oczekiwania

		if self.gracz_wszedl_teleport_b and self.czas_do_naladowania == 0:
			self.plat.gracz.pos.x = self.teleport_a.x
			self.plat.gracz.pos.y = self.teleport_a.y
			self.czas_do_naladowania = self.czas_oczekiwania

		if self.czas_do_naladowania > self.delta_time:
			self.czas_do_naladowania -= self.delta_time
		else:
			self.czas_do_naladowania = 0

		self.teleport_a.ile_do_naladowania = self.czas_do_naladowania/self.czas_oczekiwania
		self.teleport_b.ile_do_naladowania = self.czas_do_naladowania/self.czas_oczekiwania
