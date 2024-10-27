"""
Package Python Neutrosophic Sets (PYNS)
----------------------------------------------------------------------------------
author: Giorgio Nordo - Dipartimento MIFT, Università di Messina, Italy
www.nordo.it   |  giorgio.nordo@unime.it
----------------------------------------------------------------------------------
neutrosophic difference
"""
from NS.pyns.ns_universe import NSuniverse
from NS.pyns.ns_set import NSset

U = NSuniverse(1,2,3)
A = NSset(U)
A.setElement(1,(0.4,0.3,0.4))
A.setElement(2,(0.2,0.2,1))
A.setElement(3,(0.1,0.1,0.9))
print(A)

# B = NSset("1,2,3,4") # darebbe errore perché gli insiemi universo sono diversi
B = NSset(U)
B.setElement(1,(0.7,0.3,0.1))
B.setElement(2,(0.4,0.6,0.8))
B.setElement(3,(0.2,0.2,0.9))
print("B=\n",B)


C = A.NSdifference(B)
print(f"differenza =\n{C}")

# verifica
D = B.NScomplement()
E = A.NSintersection(D)
E2 = A.NSdifference(B)
print(f"differenza2 =\n{E}")
print(f"differenza2 =\n{E2}")
print(f"differenza3 =\n{A - B}")  # con l'overloading degli operatori


