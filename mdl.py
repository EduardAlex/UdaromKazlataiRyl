class Udar:
	def __init__(self, faqer):
		self.faqer = faqer
		self.bukvub_korniy = []
		self.vokalub = [i for i in "aeiouýäüąëï"]
		self.pk = {"t" : "ť", "d" : "ď", "s" : "ś", "z" : "ź", "x" : "ħ", "xh" : "h",
			"c" : "ć", "l" : "ĺ", "n" : "ń"}
		self.apk = {"t" : "tt", "d" : "dd", "s" : "ss", "z" : "zz", "l" : "ll", "c" : "cc"}
		self.ppk = [self.pk[i] for i in self.pk]
		self.papk = [self.apk[i] for i in self.apk]
		self.bukvub_korniy = self.uzan_bukvab_korniy(self.faqer)

	def uzan_bukvab_korniy(self, a):
		res = []
		azuten = False
		for i,j in enumerate(a):
			if azuten:
				azuten = False
				continue
			if j == "x" and i != len(a)-1:
				if a[i+1] == "h":
					res.append("xh")
					azuten = True
			elif j == "i" and i != len(a)-1:
				if a[i+1] in self.vokalub:
					# print(a[i+1])
					continue
				else:
					res.append(j)
			# elif j == "ï":
			# 	res.append("i")
			elif j in "tdszlc" and i != len(a)-1:
				if a[i+1] == j:
					res.append(2*j)
					azuten = True
				else:
					res.append(j)
			else:
				res.append(j)
		return res

	def abgepraugathiub(self, ltd):
		# Stsi izmenathiub faqriskengai slucusez
		try:
			if ltd[-2] == "ë":
				del ltd[-2]
				if ltd[-2] == "v":
					ltd[-2] = "ŭ"
		except:
			pass # ayaye meci mai prost
		if ltd[-1] == "ŭ":
			ltd[-1] = "v"
		if ltd[-1] == "u":
			del ltd[-1]
			if ltd[-1] == "v":
				ltd[-1] = "ŭ"
		return ltd

		# Paukalga nomber stsi pridus
		# if self.nomber == "PA":
		# 	self.bukvub_korniy += ["ä", "k"]

	def vospis_slova(self, bk):
		vospisuna = ""
		for i,j in enumerate(bk):
			if j in self.ppk or j in self.papk:
				if bk[i+1] in self.vokalub:
					if bk[i+1] == "i":
						bk[i+1] = "ï"
					elif bk[i+1] != "ï":
						vospisuna += j + "i"
						continue
			vospisuna += j
		return vospisuna

class Imub(Udar):
	def __init__(self, im, num="SG"):
		self.im = im
		self.nomin = False # Islo rezultathi is nominatiugas bezen is y yer inputis razgusva
		if num != "SG":
			self.nomin = True
		self.nomber = num # SG (edga), PL (aunogen) il PA (numeruna)
		super().__init__(im)
		self.bukvub_korniy = self.abgepraugathiub(self.bukvub_korniy)
		if num == "PA":
			self.bukvub_korniy += ["ä", "k"]
		self.udar_ima()

	def udar_ima(self):
		self.udarath_imy = {"Nominatiŭgą" : self.nominatiuga(), "Akuzatiŭgą" : self.akuzatiuga(), "Genitiŭgą" : self.genitiuga(), "Datiŭgą" : self.datiuga(),
			"Lokatiŭgą" : self.lokatiuga(), "Uńialtgą" : self.unialtga(), "Alatiŭgą" : self.alatiuga(), "Ablatiŭgą" : self.ablatiuga(), "Cipatgą" : self.cipatga()}

	def nominatiuga(self):
		bk = list(self.bukvub_korniy)
		print(self.nomin)
		if self.nomin:
			if self.nomber == "PL":
				bk += ["u","b"]
			return self.vospis_slova(bk)

		else:
			return self.im

	def akuzatiuga(self):
		bk = list(self.bukvub_korniy)
		bk.append("a")
		if self.nomber == "PL":
			bk.append("b")
		return self.vospis_slova(bk)

	def genitiuga(self):
		bk = list(self.bukvub_korniy)
		bk.append("ý")
		if self.nomber == "PL":
			bk.append("b")
		return self.vospis_slova(bk)

	def datiuga(self):
		bk = list(self.bukvub_korniy)
		bk.append("ë")
		if self.nomber == "PL":
			bk.append("b")
		return self.vospis_slova(bk)

	def lokatiuga(self):
		bk = list(self.bukvub_korniy)
		bk.append("i")
		if self.nomber == "PL":
			bk.append("b")
		return self.vospis_slova(bk)

	def unialtga(self):
		bk = list(self.bukvub_korniy)
		if bk[-1] in self.apk:
			bk[-1] = self.apk[bk[-1]]
		elif bk[-1] in self.pk:
			bk[-1] = self.pk[bk[-1]]
			bk += ["e", "h"]
		elif self.nomber == "PA":
			bk.append("ħ")
		else:
			bk += ["e", "h"]
		bk.append("a")
		if self.nomber == "PL":
			bk.append("b")
		return self.vospis_slova(bk)

	def alatiuga(self):
		bk = list(self.bukvub_korniy)
		bk += ["e", "š"]
		if self.nomber == "PL":
			del bk[-1]
			bk += ["k", "s"]
		return self.vospis_slova(bk)

	def ablatiuga(self):
		bk = list(self.bukvub_korniy)
		bk += ["i", "s"]
		if self.nomber == "PL":
			del bk[-1]
			bk += ["p", "s"]
		return self.vospis_slova(bk)

	def cipatga(self):
		bk = list(self.bukvub_korniy)
		if bk[-1] == "v":
			bk[-1] = "ŭ"
		# print(bk)
		bk += ["x", "i"]
		if self.nomber == "PL":
			bk.append("b")
		# print(bk)
		return self.vospis_slova(bk)


# a = input("")
# b = Imub(a)
# print(b.bukvub_korniy, b.udarath_imy)


class Verbub(Udar):
	def __init__(self, verb, mod="IND", vrm = "PRES", zan = "AFF", vop = "KEN"):
		self.verb = verb
		self.mod = mod
		self.vrm = vrm # Vreml akciyy
		self.zan = zan # Zanath lokutory e akciy, AFF (afirmatiuga) il NEG (negatiuga)
		self.vop = vop # Al prepozic voprosgusva ilei (KEN/EI)
		self.koren_ind = [] # Koren indikatiugai mody
		self.koren_imp = [] # Koren imperatiugai mody
		self.koren_imppl = [] # Koren pluralathiy eidelunai vremliy
		self.ip_izmenathiub = {}
		self.ip_eidelunai = {}
		with open("vi", "r") as f: # List yb eidelunau infinitiugau
			self.vi = f.read().split(" ")
		self.naid_eidel()
		super().__init__(verb)
		self.naid_kornia_verby()
		print(str(self.koren_imp) + "\n" + str(self.koren_ind) + "\n" + str(self.koren_imppl))


	def naid_kornia_verby(self):
		hdp = list(self.bukvub_korniy)
		if self.verb.startswith("ti"):
			del hdp[0:2]
		elif self.verb.startswith("d"):
			del hdp[0]
		# IMPERATIUGA
		self.koren_imp = list(hdp)
		# INDIKATIUGA
		if hdp[-1] == "t":
			if False: # !!!!!! STSI ABIT LISTE EIREGULATAU VERBYB !!!!!!
				pass
			elif hdp[-2] == "a":
				del hdp[-2:]
			else:
				del hdp[-1]
		hdp = self.abgepraugathiub(hdp)
		self.koren_ind = list(hdp)
		# EIDELUNA VREML
		for i in self.ip_eidelunai:
			if self.vospis_slova(self.koren_imp) == i:
				self.koren_imppl = self.uzan_bukvab_korniy(self.ip_eidelunai[i])
				print(self.ip_eidelunai[i])
				break
		if self.koren_imppl == []:
			for i in self.ip_izmenathiub:
				if self.verb.endswith(i):
					self.koren_imppl = self.koren_imp[:-len(self.uzan_bukvab_korniy(i))] + self.uzan_bukvab_korniy(self.ip_izmenathiub[i])
					break

	def naid_eidel(self):
		izm = []
		eid = []
		with open("kimpp", "r", encoding="utf8") as f:
			i1, e1 = f.read()[:-1].split("&")
			izm = i1.split(",")
			eid = e1.split(",")
		self.ip_izmenathiub = {i.split("-")[0] : i.split("-")[1] for i in izm}
		self.ip_eidelunai = {i.split("-")[0] : i.split("-")[1] for i in eid}
		print(self.ip_izmenathiub, self.ip_eidelunai)
