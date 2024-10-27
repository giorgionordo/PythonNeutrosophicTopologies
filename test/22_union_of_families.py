"""
Package Python Neutrosophic Sets (PYNS)
----------------------------------------------------------------------------------
author: Giorgio Nordo - Dipartimento MIFT, Università di Messina, Italy
www.nordo.it   |  giorgio.nordo@unime.it
----------------------------------------------------------------------------------
union of families
"""
from NS.pyns.ns_universe import NSuniverse
from NS.pyns.ns_set import NSset
from NS.pyns.ns_family import NSfamily

U = NSuniverse("a,b,c")
A1 = NSset(U, "(0.4,0.4,0.3), (0.1,0.1,0.1), (0.2,0.2,0.2)")
A2 = NSset(U, "(0.1,0.2,0.9), (0.9,0.1,0.3), (0.5,0.3,0.4)")
A3 = NSset(U, "(0.7,0.3,0.1), (0.8,0.4,0.0), (0.1,0.1,0.9)")
A4 = NSset(U, "(0.2,0.2,0.8), (0.6,0.6,0.3), (0.5,0.4,0.5)")
A1.storeName()
A2.storeName()
A3.storeName()
A4.storeName()

L1 = NSfamily(A1, A2, A3)
L2 = NSfamily(A3, A4)

L1.storeName()
L2.storeName()

# L3 = L1.union(L2)
L3 = L1 + L2
print(f"{L3:lx}")
