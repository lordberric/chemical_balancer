from molecule import Molecule

class Equation:
	def __init__(self, reactants, products):
		self.reactants = reactants
		self.products = products	
	def error(self):
		reactants_count = self.counting(self.reactants)
		products_count = self.counting(self.products)
		error = 0
		for key in reactants_count:
			error += (abs(reactants_count[key]-products_count[key]))
		if error == 0:
			print("The Balanced Equation is " + str(self))
			exit()
		return error
	def counting(self, mols):
		mols_count = {}
		for mol in mols:
			for key in mol.counts:
				mol_times_coef = (mol.coef * mol.counts[key]) #multiplies the coefficient by the stuff
				if key in mols_count:
					mols_count[key] += (mol_times_coef)
				else:
					mols_count[key] = (mol_times_coef)
		return mols_count
	def clone(self):
		return Equation(self.deepcopy(self.reactants), self.deepcopy(self.products))	
	def deepcopy(self, array):
		newb_mols = []
		for molecule in array:
			m = Molecule(molecule.coef)
			for key in molecule.counts:
				m.append_atom(key, molecule.counts[key])
			newb_mols.append(m)
		return newb_mols
		
	def __str__(self):
		rtn = ""
		rtn += " + ".join(map(lambda x: str(x), self.reactants))
		rtn += " => "
		rtn += " + ".join(map(lambda x: str(x), self.products))
		return rtn
		
	
