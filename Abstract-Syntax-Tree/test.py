from ast import *

e = AndExpr(NotExpr(True), OrExpr(NotExpr(False), True))

print (e)