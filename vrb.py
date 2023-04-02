from mdl import Verbub

class Udvb(Verbub):
	def __init__(self, verb, mod="IND", vrm = "PRES", zan = "AFF", vop = "EI"):
		self.verb = verb
		self.mod = mod
		self.vrm = vrm # Vreml akciyy
		self.zan = zan # Zanath lokutory e akciy, AFF (afirmatiuga) il NEG (negatiuga)
		self.vop = vop # Al prepozic voprosgusva ilei (KEN/EI)
		self.udarath = []
		super().__init__(verb)
		self.determinat_udarathia()

	def __str__(self):
		return str(self.udarath)

	def determinat_udarathia(self):
		if self.vrm == "PRES":
			self.pres()

	def pres(self):
		if self.mod == "IND":
			for i in self.proimub:
				self.udarath.append(self.vospis_slova(self.koren_ind+["u", self.proimub[i] if i == "1SG" else self.pk[self.proimub[i]]]))
