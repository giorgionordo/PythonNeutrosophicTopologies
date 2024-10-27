"""
Package Python Neutrosophic Sets (PYNS)
----------------------------------------------------------------------------------
author: Giorgio Nordo - Dipartimento MIFT, Università di Messina, Italy
www.nordo.it   |  giorgio.nordo@unime.it
----------------------------------------------------------------------------------
neutrosophic large mapping
"""
from NS.pyns.ns_universe import NSuniverse
from NS.pyns.ns_set import NSset
from NS.pyns.ns_mapping import NSmapping

lista = [(i,j) for i in range(1,4) for j in range(1,3)]
U = NSuniverse(lista)
V = NSuniverse("a,b,c,d")

f = NSmapping(U, V, "a, c, c, b, a, a")  # funzione con values assegnati
print("f =", f)

f.setValue((1,1),'d')
print("f =", f)

f.setValue((3,1),'d')
print("f =", f)

print(f"valore di (2,1) = {f.getValue((2,1))}")


# A = NSset(U)
# A.setElement((1,2),(0.8,0.1,0.2))
# A.setElement((2,3),(0.2,0.3,0.5))


