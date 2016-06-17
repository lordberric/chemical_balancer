import re
from molecule import Molecule
from equation import Equation
from trainer import Trainer
import parse
eq = input()
	
e = parse.parse_equation(eq)
t = Trainer(e)
t.run()