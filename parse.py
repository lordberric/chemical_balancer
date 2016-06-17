import re
from molecule import Molecule
from equation import Equation

def parse_molecule(string): #The Method that parses a molecule
	if re.search(r'[a-zA-Z]', string[0]): #Adds a one coefficient if necessary
		string = "1" + string
	digit_search = re.search(r'^\d+', string)
	coef = digit_search.group(0) #Defines the first number as the coefficient of our molecule
	atoms_only = string.replace(coef, "", 1) #Creates a variable w/o the coefficient
	if re.search(r'[a-zA-Z]', atoms_only[-1]):
		atoms_only = atoms_only + "1" #Adds a 1 to the end
	m = Molecule(coef) #Spawns our molecule object
	pattern = re.compile(r'([a-z]+)(\d+)', re.I) #Defines what an atom is (a letter then a number )
	for (type, count) in re.findall(pattern, atoms_only):
		atom_split_pattern = re.compile(r'[A-Z][a-z]?') #Defines what a type is (Capital and then possibly a a lowercase)
		sub_atom_matches = re.findall(atom_split_pattern, type)
		last_sub_atom = ""
		for (i, element) in enumerate(sub_atom_matches):
			if (i < len(sub_atom_matches) - 1):
				m.append_atom(element, 1)
			last_sub_atom = element
		m.append_atom(last_sub_atom, int(count))
	return m
	
def parse_equation(item):
	parsed_reactants = [] #The array of different molecules
	parsed_products = []
	items = item.split("->")
	reactants = items[0].split("+")
	products = items[1].split("+")
	for reactant in reactants:
		string = reactant.strip()
		parsed_reactants.append(parse_molecule(string))
	for product in products:
		string = product.strip()
		parsed_products.append(parse_molecule(string))
	return (Equation(parsed_reactants, parsed_products))		
		