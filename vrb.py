from mdl import Verbub
from mdl import UdaratgaEror

class Udvb(Verbub):
	def __init__(self, verb, mod="IND", vrm = "PRES", zan = True, vop = False, subj = False):
		self.verb = verb
		self.eid_edg = {'1SG': 'vde', '2SG': 'sxe', '3SG': 'u', '1PL': 'meï', '2PL': 'bdeï', '3PL': 'vi'}
		self.eid_edg = {i : self.uzan_bukvab_korniy(self.eid_edg[i]) for i in self.eid_edg}
		self.mod = mod
		self.vrm = vrm # Vreml akciyy
		self.zan = not zan # Zanath lokutory e akciy, AFF (afirmatiuga) il NEG (negatiuga)
		self.vop = vop # Al prepozic voprosgusva ilei (True/False)
		self.subj = subj # Es yer a -va kapti verby azutusva
		if self.vop and self.subj:
			raise UdaratgaEror("I subzonktiugeu verb ides voprosgath!")
		self.udarath = []
		super().__init__(verb)
		self.imp_f()
		self.determinat_udarathia()

	def __str__(self):
		return str([self.vospis_slova(i) for i in self.udarath])

	def determinat_udarathia(self):
		if self.vrm == "PRES":
			self.pres()
		elif self.vrm == "PRES_PRD":
			self.presprd()
		elif self.vrm == "PAST":
			self.past()
		elif self.vrm == "EID":
			self.eid()
		elif self.vrm == "FUT":
			self.fut()

	def imp_f(self):
		# Gerundga
		self.ger = list(self.verb)
		if self.ger[0] == "t":
			self.ger[0] = "ts'"
		elif self.ger[0] == "d":
			self.ger[0] = "dz"

	def pres(self):
		if self.mod == "IND":
			k = list(self.koren_ind)
			if self.koren_ind[-1] not in self.vokalub: k += ["u"]
			if not self.zan:
				k += ["n", "e"]
			for i in self.proimub:
				self.udarath.append(k+[(self.proimub[i] if i == "1SG" or self.subj else self.pk[self.proimub[i]]), "a"*int(self.vop)])
				if self.subj:
					self.udarath[-1] = self.udarath[-1] + ["v", "a"]

	def presprd(self):
		if self.mod == "IND":
			k = self.abgepraugathiub(self.ger)
			if k[-1] not in self.vokalub: k += ["i"]
			if not self.zan:
				k += ["n", "e"]
			for i in self.proimub:
				self.udarath.append(k+[(self.proimub[i] if i == "1SG" or self.subj else self.pk[self.proimub[i]]), "a"*int(self.vop)])
				if self.subj:
					self.udarath[-1] = self.udarath[-1] + ["v", "a"]

	def fut(self):
		if self.mod == "IND":
			k = list(self.koren_ind)
			if self.koren_ind[-1] not in self.vokalub: k += ["u"]
			if not self.zan:
				k += ["n", "e"]
			for i in self.proimub:
				self.udarath.append((["ť"] if k[0] in self.vokalub else ["t", "e", " "])+k+
					[(self.proimub[i] if i == "1SG" or self.subj else self.pk[self.proimub[i]]), "a"*int(self.vop)])
				if self.subj:
					self.udarath[-1] = self.udarath[-1] + ["v", "a"]

	def past(self):
		if self.mod == "IND":
			k = list(self.koren_ind)
			if self.koren_ind[-1] not in self.vokalub: k += ["u"]
			if not self.zan:
				k += ["n", "e"]
			for i in self.proimub:
				self.udarath.append(k+[(self.proimub[i] if i == "1SG" or self.subj else self.pk[self.proimub[i]]), "e"] + ["y","a"]*int(self.vop))
				if self.subj:
					self.udarath[-1] = self.udarath[-1] + ["v", "a"]

	def eid(self):
		a = [self.koren_ind if self.verb.endswith("t") and not self.dmwi else self.koren_imp, self.koren_imppl]
		v = self.koren_imp[0] in self.vokalub
		if not self.zan:
			a = [i + ["e", "n"] for i in a]
		for i in self.eid_edg:
			self.udarath.append(self.eid_edg[i] + ["y"]*int(v) + (a[0] if i.endswith("SG") else a[1]))
			if self.subj:
				self.udarath[-1] = self.udarath[-1] + ["v", "a"]
