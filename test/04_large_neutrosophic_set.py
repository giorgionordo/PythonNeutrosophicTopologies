"""
Package Python Neutrosophic Sets (PYNS)
----------------------------------------------------------------------------------
author: Giorgio Nordo - Dipartimento MIFT, Università di Messina, Italy
www.nordo.it   |  giorgio.nordo@unime.it
----------------------------------------------------------------------------------
an example of an hardcoded large neutrosophic set
"""
from NS.pyns.ns_universe import NSuniverse
from NS.pyns.ns_set import NSset
from random import random

lst = [(i, j) for i in range(1, 6) for j in range(1, 4)]
U = NSuniverse(lst)
A = NSset(U)
for u in U.get():
    triple = [round(random(), 2) for k in range(3)]
    A.setElement(u, triple)

print(f"The following SVNS-set has cardinality {A.cardinality()}: {A}")