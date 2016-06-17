class Molecule: #BlazeBuddies
	def __init__(self, coef): 
		self.coef = int(coef)
		self.counts = {}
	
	def append_atom(self, type, subs):
		self.counts[type] = int(subs)
	
	def __str__(self): #defines the Molecule
		rtn = str(self.coef)
		rtn += "".join(map(lambda x: x + str(self.counts[x]), self.counts))
		return rtn