"""
Package Python Neutrosophic Sets (PYNS)
----------------------------------------------------------------------------------
author: Giorgio Nordo - Dipartimento MIFT, Università di Messina, Italy
www.nordo.it   |  giorgio.nordo@unime.it
----------------------------------------------------------------------------------
complement of a family
"""
from NS.pyns.ns_universe import NSuniverse
from NS.pyns.ns_set import NSset
from NS.pyns.ns_family import NSfamily

U = NSuniverse("a,b,c")
A1 = NSset(U, "(0.412345555,0.4,0.3), (0.1,0.1,0.1), (0.2,0.2,0.2)")
A2 = NSset(U, "(0.1,0.2,0.9), (0.9,0.1,0.3), (0.5,0.3,0.4)")
A3 = NSset(U, "(0.7,0.3,0.1), (0.8,0.4,0.0), (0.1,0.1,0.9)")
A4 = NSset(U, "(0.2,0.2,0.8), (0.6,0.6,0.3), (0.5,0.4,0.5)")
A1.storeName()
A2.storeName()
A3 = ~A1
A4 = ~A3
print(f"{A4:lx}")

A3 = (A1 + ~A2) & (A1 - A2)
A4 = A1 & A2

L1 = NSfamily(A3, A4)
L1.storeName()
print(f"{L1:lx}")

# L3 = L1.complement()
L3 = ~L1
L3.storeName()
print(f"{L3:lx}")

