"""
Package Python Neutrosophic Sets (PYNS)
----------------------------------------------------------------------------------
author: Giorgio Nordo - Dipartimento MIFT, Università di Messina, Italy
www.nordo.it   |  giorgio.nordo@unime.it
----------------------------------------------------------------------------------
counterimage of a neutrosophic set by a mapping
"""
from NS.pyns.ns_universe import NSuniverse
from NS.pyns.ns_set import NSset
from NS.pyns.ns_mapping import NSmapping

U = NSuniverse("a,b,c,d,e")
V = NSuniverse(1,2,3,4)

B = NSset(V)
B.setElement(1,(0.7,0.3,0.1))
B.setElement(2,(0.4,0.6,0.9))
B.setElement(3,(0,0,1))
B.setElement(4,(0.1,0.4,0.5))
print("B =",B)

f = NSmapping(U, V, (1,3,1,2,1))  # funzione con values assegnati
print("dominio = ", f.getDomain())
print("codominio = ", f.getCodomain())
print("f =", f)

A = f.NScounterimage(B)
print("f^-1(B)=", A)


