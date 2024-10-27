"""
Package Python Neutrosophic Sets (PYNS)
----------------------------------------------------------------------------------
author: Giorgio Nordo - Dipartimento MIFT, Università di Messina, Italy
www.nordo.it   |  giorgio.nordo@unime.it
----------------------------------------------------------------------------------
fibre by a neutrosophic mapping
"""
from NS.pyns.ns_universe import NSuniverse
from NS.pyns.ns_set import NSset
from NS.pyns.ns_mapping import NSmapping

U = NSuniverse("a,b,c,d,e")
V = NSuniverse(1,2,3,4)

f = NSmapping(U, V, (1,3,1,2,1))  # funzione con values assegnati
print("f =", f)

print(f"La fibra di 1 mediante la f è {f.getFibre(1)}")
print(f"La fibra di 3 mediante la f è {f.getFibre(3)}")
print(f"La fibra di 4 mediante la f è {f.getFibre(4)}")