
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

def is_reducible(e):
	return not (type(e) is BoolExpr)

def step_not(e):

	if(not is_reducible(e.expr)):
		return(BoolExpr(not e.expr.value))

	else:
		e.expr = step(e.expr)
		return e

def step_and(e):

	if(is_reducible(e.lhs)):
		e.lhs = step(e.lhs)
		return e

	if(is_reducible(e.rhs)):
		e.rhs = step(e.rhs)
		return e

	else:
		return(BoolExpr(e.lhs.value and e.rhs.value))

def step_or(e):

	if(is_reducible(e.lhs)):
		e.lhs = step(e.lhs)
		return e

	if(is_reducible(e.rhs)):
		e.rhs = step(e.rhs)
		return e

	else:
		return(BoolExpr(e.lhs.value or e.rhs.value))

def step(e):

	assert is_reducible(e)

	if type(e) is NotExpr:
		return step_not(e)

	if type(e) is AndExpr:
		return step_and(e)

	if type(e) is OrExpr:
		return step_or(e)

def reduce(e):

	while(not (type(e) is BoolExpr)):
		e = step(e)

	return e

def height(e):

	i = 0
	while(not (type(e) is BoolExpr)):
		e = step(e)
		i += 1

	print(counter)