
class Expr:
	pass

class BoolExpr():
	def __init__(self, val):
		self.value = val

	def __str__(self):
		return f"{self.value}"

class NotExpr():
	def __init__(self, e):
		self.expr = e

	def __str__(self):
		return f"(NOT {self.expr})"

class AndExpr():
	def __init__(self, lhs, rhs):
		self.lhs = lhs
		self.rhs = rhs

	def __str__(self):
		return f"({self.lhs} AND {self.rhs})"

class OrExpr():
	def __init__(self, lhs, rhs):
		self.lhs = lhs
		self.rhs = rhs

	def __str__(self):
		return f"({self.lhs} OR {self.rhs})"


def same(e1, e2):

	if type(e1) != type(e2):
		return False



	if type(e1) is BoolExpr:
		return e1.value == e2.value

	if type(e1) is NotExpr:
		return same(e1.expr, e2.expr)

	if type(e1) is AndExpr:
		return same(e1.lhs, e2.lhs) and same(e1.rhs, e2.rhs);

	if type(e1) is OrExpr:
		return same(e1.lhs, e2.lhs) and same(e1.rhs, e2.rhs);

#def is_reducible()

def step_not(e):


#def step_and()

#def step_or()

def step(e):
	
	#assert is_reducible(e)

	if type(e) is NotExpr:
		return step_not(e)

	if type(e) is AndExpr:
		return step_and(e)

	if type(e) is OrExpr:
		return step_or(e)
