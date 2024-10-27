"""
Package Python Neutrosophic Sets (PYNS)
----------------------------------------------------------------------------------
author: Giorgio Nordo - Dipartimento MIFT, Università di Messina, Italy
www.nordo.it   |  giorgio.nordo@unime.it
----------------------------------------------------------------------------------
neutrosophic complement
"""
from NS.pyns.ns_universe import NSuniverse
from NS.pyns.ns_set import NSset

U = NSuniverse(1,2,3)
A = NSset(U)
A.setElement(1,(0.4,0.3,0.2))
A.setElement(2,(0.2,0.2,1))
A.setElement(3,(0.1,0.1,0.9))
print("A=\n", A)

C = A.NScomplement()
print("A^c=\n", C)
print("A^c=\n", ~A)   # con l'overloading degli operatori