from mdl import Verbub

class Udvb(Verbub):
	def __init__(self, verb, mod="IND", vrm = "PRES", zan = "AFF", vop = False):
		self.verb = verb
		self.eid_edg = {'1SG': 'vde', '2SG': 'sxe', '3SG': 'u', '1PL': 'meï', '2PL': 'bdeï', '3PL': 'vi'}
		self.eid_edg = {i : self.uzan_bukvab_korniy(self.eid_edg[i]) for i in self.eid_edg}
		self.mod = mod
		self.vrm = vrm # Vreml akciyy
		self.zan = zan # Zanath lokutory e akciy, AFF (afirmatiuga) il NEG (negatiuga)
		self.vop = vop # Al prepozic voprosgusva ilei (True/False)
		self.udarath = []
		super().__init__(verb)
		self.determinat_udarathia()

	def __str__(self):
		return str([self.vospis_slova(i) for i in self.udarath])

	def determinat_udarathia(self):
		if self.vrm == "PRES":
			self.pres()
		elif self.vrm == "PAST":
			self.past()
		elif self.vrm == "EID":
			self.eid()


	def pres(self):
		if self.mod == "IND":
			k = list(self.koren_ind)
			k += ["u"]
			if self.zan == "NEG":
				k += ["n", "e"]
			for i in self.proimub:
				self.udarath.append(k+[(self.proimub[i] if i == "1SG" else self.pk[self.proimub[i]]), "a"*int(self.vop)])

	def past(self):
		if self.mod == "IND":
			k = list(self.koren_ind)
			k += ["u"]
			if self.zan == "NEG":
				k += ["n", "e"]
			for i in self.proimub:
				self.udarath.append(k+[(self.proimub[i] if i == "1SG" else self.pk[self.proimub[i]]), "e"] + ["y","a"]*int(self.vop))

	def eid(self):
		a = [self.koren_imp, self.koren_imppl]
		v = self.koren_imp[0] in self.vokalub
		if self.zan == "NEG":
			a = [i + ["e", "n"] for i in a]
		for i in self.eid_edg:
			self.udarath.append(self.eid_edg[i] + ["y"]*int(v) + (a[0] if i.endswith("SG") else a[1]))
