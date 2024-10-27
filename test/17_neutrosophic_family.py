"""
Package Python Neutrosophic Sets (PYNS)
----------------------------------------------------------------------------------
author: Giorgio Nordo - Dipartimento MIFT, Università di Messina, Italy
www.nordo.it   |  giorgio.nordo@unime.it
----------------------------------------------------------------------------------
some examples of neutrosophic families
"""
from NS.pyns.ns_universe import NSuniverse
from NS.pyns.ns_set import NSset
from NS.pyns.ns_family import NSfamily

U = NSuniverse("a,b,c")
A1 = NSset(U, "(0.4,0.4,0.3), (0.1,0.1,0.1), (0.2,0.2,0.2)")
A2 = NSset(U, "(0.1,0.2,0.9), (0.9,0.1,0.3), (0.5,0.3,0.4)")
A3 = NSset(U, "(0.7,0.3,0.1), (0.8,0.4,0.0), (0.1,0.1,0.9)")

A1.storeName()
A2.storeName()
A3.storeName()


F = NSset.EMPTY(U)     # insieme neutrosofico vuoto
# F.storeName()

A = NSset.ABSOLUTE(U)   # insieme neutrosofico assoluto
A.storeName()

L = NSfamily(A1, A2, A3, A)
L.storeName()
print(f"{F:tl}")

print(f"l'insieme neutrosofico vuoto {F} appartiene alla famiglia? {F in L}")
print(f"l'insieme neutrosofico assoluto {A} appartiene alla famiglia? {A in L}")

print(L.getUniverse())



