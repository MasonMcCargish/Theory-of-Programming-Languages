from ast import *

e = AndExpr(NotExpr(BoolExpr(False)), OrExpr(NotExpr(BoolExpr(False)), BoolExpr(True)))

e = reduce(e)

print(e)
