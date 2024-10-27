"""
Package Python Neutrosophic Sets (PYNS)
----------------------------------------------------------------------------------
author: Giorgio Nordo - Dipartimento MIFT, Università di Messina, Italy
www.nordo.it   |  giorgio.nordo@unime.it
----------------------------------------------------------------------------------
image of a neutrosophic set by a mapping
"""
from NS.pyns.ns_universe import NSuniverse
from NS.pyns.ns_set import NSset
from NS.pyns.ns_mapping import NSmapping

U = NSuniverse("a,b,c,d,e")
V = NSuniverse(1,2,3,4)

A = NSset(U)
A.setElement('a',(0.7,0.3,0.1))
A.setElement('b',(0.4,0.6,0.9))
A.setElement('c',(0,0,1))
A.setElement('d',(0.1,0.4,0.5))
A.setElement('e',(0.2,0.2,0.3))
print("A =",A)

f = NSmapping(U, V, (1,3,1,2,1))  # funzione con values assegnati
f = NSmapping("a,b,c,d,e", (1,2,3,4), (1,3,1,2,1))  # funzione definita esplicitamente
print("dominio = ", f.getDomain())
print("codominio = ", f.getCodomain())
print("f =", f)

B = f.NSimage(A)
print("f(A)=", B)


