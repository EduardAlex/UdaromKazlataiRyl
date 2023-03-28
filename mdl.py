class Imub:
	def __init__(self, im):
		self.im = im
		self.bukvub_imy = []
		self.vokalub = [i for i in "aeiouýäüąëï"]
		self.pk = {"t" : "ť", "d" : "ď", "s" : "ś", "z" : "ź", "x" : "ħ", "xh" : "h", 
			"c" : "ć", "l" : "ĺ", "n" : "ń"}
		self.apk = {"t" : "tť", "d" : "dď", "s" : "sś", "z" : "zź", "l" : "lĺ", "c" : "cć"}
		self.ppk = [self.pk[i] for i in self.pk]
		self.papk = [self.apk[i] for i in self.apk]
		self.udarath_imy = {}
		self.uzan_bukvab_imy()
		self.udar_ima()

	def uzan_bukvab_imy(self):
		azuten = False
		for i,j in enumerate(self.im):
			if azuten:
				azuten = False
				continue
			if j == "x" and i != len(self.im)-1:
				if self.im[i+1] == "h":
					self.bukvub_imy.append("xh")
					azuten = True
			elif j == "i" and i != len(self.im)-1:
				if self.im[i+1] in self.vokalub:
					continue
			# elif j == "ï":
			# 	self.bukvub_imy.append("i")
			elif j in "tdszlc" and i != len(self.im)-1:
				if self.im[i+1] == self.pk[j]:
					self.bukvub_imy.append(j + self.pk[j])
					azuten = True
				else:
					self.bukvub_imy.append(j)
			else:
				self.bukvub_imy.append(j)

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

	def udar_ima(self):
		self.udarath_imy = {"Nominativgą" : self.im, "Akuzativgą" : self.akuzativga(), "Genitivgą" : self.genitivga(), "Dativgą" : self.dativga(), 
			"Lokativgą" : self.lokativga(), "Uńialtgą" : self.unialtga(), "Alativgą" : self.alativga(), "Ablativgą" : self.ablativga(), "Cipatgą" : self.cipatga()}

	def akuzativga(self):
		bk = list(self.bukvub_imy)
		bk.append("a")
		return self.vospis_slova(bk)

	def genitivga(self):
		bk = list(self.bukvub_imy)
		bk.append("ý")
		return self.vospis_slova(bk)

	def dativga(self):
		bk = list(self.bukvub_imy)
		bk.append("ë")
		return self.vospis_slova(bk)

	def lokativga(self):
		bk = list(self.bukvub_imy)
		bk.append("i")
		return self.vospis_slova(bk)

	def unialtga(self):
		bk = list(self.bukvub_imy)
		if bk[-1] in self.apk:
			bk[-1] = self.apk[bk[-1]]
		elif bk[-1] in self.pk:
			bk[-1] = self.pk[bk[-1]]
			bk += ["e", "h"]
		else:
			bk += ["e", "h"]
		bk.append("a")
		return self.vospis_slova(bk)

	def alativga(self):
		bk = list(self.bukvub_imy)
		bk += ["e", "š"]
		return self.vospis_slova(bk)

	def ablativga(self):
		bk = list(self.bukvub_imy)
		bk += ["i", "s"]
		return self.vospis_slova(bk)

	def cipatga(self):
		bk = list(self.bukvub_imy)
		print(bk)
		bk += ["x", "i"]
		print(bk)
		return self.vospis_slova(bk)


# a = input("")
# b = Imub(a)
# print(b.bukvub_imy, b.udarath_imy)