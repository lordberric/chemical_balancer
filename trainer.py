import random
class Trainer:
	def __init__(self, equation):
		self.initial_equation = equation
	def mutate(self, equation):		
		self.mutation(equation.reactants)
		self.mutation(equation.products)
		return equation
	def epoch(self, ancestors):
		new_generation = []
		for ancestor in ancestors:
			for i in range(0, 100):
				new_generation.append(self.mutate(ancestor.clone()))
		new_generation.sort(key=lambda x: x.error())
		return new_generation[:int(len(new_generation) * 0.1)]
	def run(self):
		alive = [self.initial_equation]
		for i in range(1000):
			alive = self.epoch(alive)
		print ("Unable to find solution. Ted Cruz is the Zodiac Killer")
	def mutation(self, molecules):
		for molecule in molecules:
			molecule.coef += random.randint(-3,3)
			if molecule.coef < 1:
				molecule.coef = 1
				